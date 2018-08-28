import time
import socket
import _thread
import urllib.request
import pymysql
import json

con = pymysql.connect(host="134.175.50.186", user="root", password="123456", db="Autotest", port=3306)
cur = con.cursor()

def save_aging_data(server_num, data):
    """
    将抓取到的配置信息保存到数据库里
    :param data_response: 进行格式化之后的数据
    :return:
    """
    try:
        params = (data, server_num)
        cur.execute('UPDATE auto_autoconfiginfos SET aging_data = %s WHERE server_num = %s', params)
        con.commit()
        print('老化测试数据保存成功')
        cur.close()
    except:
        print('序列号为:{}的服务器还没有经过本地数据抓取'.format(server_num))
        pass


def ensure_response(data, index):
    """
    防止数据格式不对导致程序崩溃
    :param data: 接收到的数据
    :param index: 切分后列表的索引
    :return: 实际值或者空值
    """
    try:
        value = data.split('#')[index]
        return value
    except:
        return ''


def reformat_data(data, address):
    """
    将数据 格式化成 字典
    :param data:接收到的数据
    :param address:客户端的 ip 地址
    :return:
    """
    data_response = {
        "server_num": "",#服务器序列号
        "board": "",#主板
        "cpu": "",#CPU
        "memory_bank": "",#内存
        "hard_disk": "",#硬盘
        "raid": "",#阵列卡
        "vga": "",#显卡
        "gpu": "",#GPU
        "hba": "",#hba卡
        "net_card": "",#网卡
        "fc_card": "",#光纤卡
        "inspect_time": "",#检查时间
        "ip_info": "",#ip地址信息
        "checkstate": 0,
        "state": "success",#测试是否成功
        "aging_data": "",#老化测试结果
        "status": 1 #数据是否有误
    }

    # data_response["server_num"] = data.split('#')[0]
    data_response["board"] = ensure_response(data, 0)
    data_response["cpu"] = ensure_response(data, 1)
    data_response["memory_bank"] = ensure_response(data, 2)
    data_response["hard_disk"] = ensure_response(data,  3)
    data_response["net_card"] = ensure_response(data, 4)
    data_response["vga"] = ensure_response(data, 5)
    data_response["server_num"] = ensure_response(data, 6)
    # data_response["raid"]
    # data_response["gpu"]
    # data_response["hba"]
    # data_response["fc_card"]
    data_response["inspect_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time())))
    data_response["ip_info"] = address
    return data_response


def recv_data(connection, buff_size):
    """
    接收 tcp 传输的数据
    :param connection:客户端连接的管道对象
    :param buff_size:缓冲区
    :return:接收后的数据
    """
    data = connection.recv(buff_size)
    data = data.decode('utf-8')
    return data


def send(data):
    """
    将数据发送到websocket的方法
    :param data:抓取到的配置信息，并格式化之后的数据
    :return:None
    """
    url = "http://127.0.0.1:8000/send?str=" + data
    urllib.request.urlopen(url)


def sendip(ip):
    """
    将数据发送到消息队列的方法
    :param ip:接收到的客户端 ip 地址
    :return:
    """
    url = "http://127.0.0.1:8000/auto/sendip?ip=" + ip
    urllib.request.urlopen(url)


def judge_ip(data):
    """
    判断 接收的数据 是否是 ip 地址
    是：返回True, 否则 False
    :param data: 接收到的数据
    :return:
    """
    ip_split_list = data.strip().split('.')
    # 切割后列表必须有4个元素
    if len(ip_split_list) != 4:
        return False
    for i in range(4):
        try:
            # 每个元素必须为数字
            ip_split_list[i] = int(ip_split_list[i])
        except:
            print("IP invalid:" + data)
            return False
    for i in range(4):
        # 每个元素值必须在0-255之间
        if ip_split_list[i] <= 255 and ip_split_list[i] >= 0:
            pass
        else:
            print("IP invalid:" + data)
            return False
    return True


def handle_data(connection, address):
    """
    对接收的数据进行处理
    :param connection: C 与 tcp 连接实例
    :param address: 客户端 ip地址
    :return: None
    """
    # 测试 websocket 数据
    # test_json = '[{"num":"001","cpu":"hg57","memory":"ytrthy5676","disk":"hgfut6768","board":"gyu75567","array":"tyu876","Videocar":"56ytrty","GPU":"67tytu7","HBA":"675tyhg","network":"78tujghhjg","opticalcar":"8tyutyu78","state":"testdone","ip":"192.168.1.1","checkstate":"false"}]'
    # send(test_json)
    data = recv_data(connection, 4096)
    print('接收到的数据：', data)

    # 对数据做判断，
    # 如果是 ip 地址的格式，发送到消息队列
    if judge_ip(data.split(':')[1]):
        print('客户端发来的ip', data)
        ip = data.split(':')[1]
        sn = data.split(':')[0]
        data_response = {
            "server_num": "",  # 服务器序列号
            "board": "",  # 主板
            "cpu": "",  # CPU
            "memory_bank": "",  # 内存
            "hard_disk": "",  # 硬盘
            "raid": "",  # 阵列卡
            "vga": "",  # 显卡
            "gpu": "",  # GPU
            "hba": "",  # hba卡
            "net_card": "",  # 网卡
            "fc_card": "",  # 光纤卡
            "inspect_time": "",  # 检查时间
            "ip_info": "",  # ip地址信息
            "checkstate": 0,
            "state": "online",  # 测试是否成功
            "aging_data": "",  # 老化测试结果
            "status": 1  # 数据是否有误
        }
        data_response["server_num"] = sn
        data_response["ip_info"] = ip
        online_data = json.dumps(data_response).replace(' ', '').replace('\r\n', '')
        send(online_data)
        sendip(data)

    # 如果是配置信息，发送到 websocket
    elif data.split(':')[0] == 'BoardName':
        config_info = reformat_data(data, address)
        config_info = json.dumps(config_info).replace(' ', '').replace('\r\n', '')
        send(config_info)

    # todo:判断数据是否是老化测试数据，如果是保存到数据库,再发送到 websocket
    elif data.split(':')[0] == 'old_test':
        # 取出服务器的序列号
        server_num = data.split('#')[6]
        print(server_num, '服务器序列号', '老化数据', data)
        save_aging_data(server_num, data)
        print('老化测试数据保存成功')

    else:
        connection.sendall(b'connection has been rejected!')

    connection.close()
    print('完整响应, 成功关闭 socket 连接')


def tcp_run(host='', port=3000):
    """
    启动服务器
    """
    print('socket server start at', '{}:{}'.format(host, port))
    with socket.socket() as s:
        s.bind((host, port))
        s.listen(6)
        while True:
            connection, address = s.accept()
            print('区分', connection.getpeername()[1])
            print(' tcp 连接成功, 使用多线程处理请求', address)
            _thread.start_new_thread(handle_data, (connection, address[0]))


if __name__ == '__main__':
    config = dict(
        host='',
        port=3000,
    )
    tcp_run(**config)
