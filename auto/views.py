import json
import queue
import django.core.serializers as serializers
from django.shortcuts import render
from auto.models import AutoConfigInfos
from django.http import HttpResponse
from django.http import JsonResponse
from client.c_client import Client
from logutils import django_log

q = queue.Queue()


def json_response_each(server_num):
    """
    search_history 方法的内部函数
    :param server_num:
    :return: 单个 server 对象数据
    """
    print('开始查找历史')
    server = AutoConfigInfos.objects.filter(server_num=server_num)
    if len(server) == 0:
        return {"response": "未找到相应的机器，请输入正确的序列号！"}
    infos_local = json.loads(serializers.serialize("json", server))[0]['fields']
    return infos_local


def search_history(request):
    """
    查询历史的视图函数
    :param request:
    :return: 采集到的数据
    """
    if request.method == 'POST':
        server_num = json.loads(request.body.decode()).get('server_num', '')
        print('server_num', server_num)
        # 前端传回的数据要么有，要么为空字符串
        if server_num != '':
            # 只返回 测试 数据，不返回 OA 数据
            response = json_response_each(server_num)
            return JsonResponse(response)
        else:
            feedback = {"feedback": "请输入正确的服务器序列号！"}
            return JsonResponse(feedback)
    else:
        return HttpResponse(status=403)


def begin_test(request):
    """
    用于向单独的每台机器发送 开始老化测试 命令
    :param request:
    :return: json字符串，判断是否开始测试
    """
    if request.method == 'POST':
        test_msg = json.loads(str(request.body, encoding="utf-8"))
        ip = test_msg.get('ip', None)
        start_msg = test_msg.get('opr', None)
        print(ip, '老化测试的 ip 地址')
        if ip is None or start_msg is None:
            return JsonResponse({"feedback": "没有发现 ip，请检查网络是否正常！"})
        try:
            client = Client(ip, 5000)
            client.send_msg_to_c(bytes(start_msg, encoding='utf-8'))
            feedback = {"feedback": "连接成功！老化测试中......"}
            return JsonResponse(feedback)
        except:
            feedback = {"feedback": "服务器连接失败，ip为:{}，请检查网络是否正常!".format(ip)}
            return JsonResponse(feedback)
    else:
        return HttpResponse(status=403)


def start_running(request):
    """
    C程序 开始运行 信号,把所有的连接上的 ip 遍历，调用 client 去连接, 发送数据
    :param request:
    :return:
    """
    if request.method == 'POST':
        start_msg = str(request.body, encoding='utf-8')
        print('开始测试的信号', start_msg)
        error_server_list = []
        while not q.empty():
            print('当 ip 队列不为空')
            ip_and_servernum = q.get()
            server_num = ip_and_servernum.split(':')[0]
            ip = ip_and_servernum.split(':')[1]
            print('receive ip info for start testing', ip)
            try:
                client = Client(ip, 5000)
                client.send_msg_to_c(bytes(start_msg, encoding='utf-8'))
                print('已经发送 开始测试 到 服务器：{}'.format(ip))
            except:
                # 如发现连接失败，
                # 无法根据 ip 去数据库里查找出对应的机器序列号
                error_server_list.append(server_num)
                print('服务器：{} 连接失败！'.format(server_num), error_server_list)

        print('发送开始测试信息结束', error_server_list)

        if len(error_server_list) == 0:
            feedback = {"feedback": []}
            return JsonResponse(feedback)

        feedback = {"feedback": error_server_list}
        return JsonResponse(feedback)
    else:
        return HttpResponse(status=403)


def restart_running(request):
    """
    重测 功能接口
    :param request:
    :return:
    """
    ip_lists = json.loads(str(request.body, encoding="utf-8"))
    print(ip_lists, 'restart sssss')
    ip_dict = ip_lists[0]
    print('restart info', ip_dict)
    if len(ip_lists) == 0:
        feedback = {"feedback": "重测失败，请勾选需要重测的服务器！"}
        return JsonResponse(feedback)

    error_server_list = []
    for ip in ip_dict:
        try:
            client = Client(ip, 5000)
            client.send_msg_to_c(bytes('test_restart', encoding='utf-8'))
            print('已经发送 开始测试 到 服务器：{}'.format(ip))
        except:
            # 如发现连接失败restart info，
            # 根据 ip 去找出对应的机器，将 序列号 发送给前端
            server_num = ip_dict.get(ip)
            print('提取的序列number', server_num)
            error_server_list.append(server_num)
            print('重测服务器：{} 连接失败！'.format(ip), error_server_list)
    print('发送开始测试信息结束', error_server_list)

    if len(error_server_list) == 0:
        feedback = {"feedback": []}
        return JsonResponse(feedback)

    feedback = {"feedback": error_server_list}
    return JsonResponse(feedback)


def change_status(request):
    """
    当人工对比数据发现错误后，点击 “数据错误” 按钮会运行，将 status 改为 0
    :param request:
    :return: feedback
    """
    if request.method == 'POST':
        server_num = str(request.body, encoding="utf-8")
        if server_num is None:
            feedback = {"feedback": "没有找到这台服务器"}
            return JsonResponse(feedback)
        server = AutoConfigInfos.objects.filter(server_num=server_num)[0]
        server.status = 0
        server.save()
        feedback = {"feedback": "已在数据库里做好标记！"}
        return JsonResponse(feedback)
    else:
        return HttpResponse(status=403)


def open_pxelinux():
    """
    读取配置文件，返回内容
    :return:
    """
    # with open('/var/lib/tftpboot/pxelinux.cfg/default') as f:
    with open('pxelinux') as f:
        al = f.read()
        f.close()
    return al


def search_system_list(request):
    """
    搜索当前可用的系统
    :param request:
    :return: 可用系统列表
    """
    if request.method == 'GET':
        al = open_pxelinux()
        data_blcok = al.split('\n\n')[1:]
        sys_list = []
        for data in data_blcok:
            system_lable = data.strip().split('\n')[0]
            if "#" in system_lable:
                print('注释的系统', system_lable)
            else:
                sys_list.append(system_lable)
                for s in sys_list:
                    if s == '':
                        sys_list.remove(s)
        sys_name_list = []
        for sys in sys_list:
            sys_name = sys.split(' ')
            if sys_name[0] != 'LABEL':
                print('如果不是LABEL', sys_name)
            else:
                sys_name_list.append(sys_name[1])

        feedback_list = []
        for system in sys_name_list:
            f = {'sysname': system, 'val': system}
            feedback_list.append(f)
        feedback = {"feedback": feedback_list}
        print('系统列表', feedback_list)
        return JsonResponse(feedback)
    return HttpResponse(status=403)


def install_system(request):
    """
    安装系统功能，将 系统安装的默认配置文件更改为需要的版本
    :param request:
    :return:
    """
    if request.method == 'POST':
        front_data = eval(str(request.body, encoding='utf-8'))
        select_system = front_data.get('sel', None)
        ip_lists = front_data.get('ip', None)
        ip_list = ip_lists[0]
        print('安裝的系統', select_system, ip_list)
        if select_system is None or ip_list is None:
            return JsonResponse({"feedback": "没有选择系统或者ip列表为空"})
        # file = "/var/lib/tftpboot/pxelinux.cfg/default"
        file = "pxelinux"
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()
            print('指定行数', lines[1:])

        with open(file, "w", encoding="utf-8") as f_w:
            # 匹配第一行 default 位置后面的文字
            default_system = lines[0].split()[1]
            first_line = lines[0].replace(default_system, select_system)
            print('lines[0]', first_line)

            f_w.write(first_line)
            for line in lines[1:]:
                f_w.write(line)
            f.close()

        error_server_list = []
        for ip in ip_list:
            try:
                client = Client(ip, 5000)
                client.send_msg_to_c(b'reboot')
                print('已经发送 reboot 到 服务器：{}'.format(ip))
            except:
                server_num = ip_list.get(ip, None)
                if server_num is None:
                    print('发送重启时服务器的ip信息没有在数据库')
                error_server_list.append(server_num)
                print('服务器：{} 连接失败！'.format(ip), error_server_list)

        if len(error_server_list) == 0:
            feedback = {"feedback": []}
            return JsonResponse(feedback)

        feedback = {"feedback": error_server_list}
        return JsonResponse(feedback)
    return HttpResponse(status=403)


def search_aging_test(request):
    if request.method == 'POST':
        server_num = str(request.body, encoding='utf-8')
        print(server_num, 'aaaaaaaa')
        aging_server = AutoConfigInfos.objects.filter(server_num=server_num)
        if len(aging_server) == 0:
            return JsonResponse({"feedback": []})
        aging_test_data = aging_server[0].aging_data
        print(aging_test_data, 'aging test data')
        feedback = {"feedback": aging_test_data}
        return JsonResponse(feedback)
    else:
        return HttpResponse(status=403)


def command(request):
    return render(request, 'command_test.html')


def search_test(request):
    return render(request, 'search_test.html')


def sendip(request):
    print('get ip 地址')
    ip = request.GET.get('ip')
    q.put(ip)
    return HttpResponse()
