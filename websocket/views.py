from django.shortcuts import render
from dwebsocket.decorators import accept_websocket
from django.http import HttpResponse
from auto import models
import time


@accept_websocket
def echo(request):
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'index.html')

    else:
        global ws
        ws = request.websocket
        print("websocket连接成功")
        for message in request.websocket:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))), 'websocket 接受的信息是：', message)
            m = str(message, encoding="utf-8")
            print(m, 'mmmmmmm')
            st(m)  # 发送消息到客户端


def st(s):
    ws.send(bytes(s, encoding="utf8"))


def send(request):
    s = request.GET.get('str')
    print('websocket接收到的数据', s)
    st(s)
    print('发送到 websocket')
    save_or_update(s)
    return HttpResponse()


def save_or_update(s):
    config_data = eval(s)
    # 保存到数据库
    server_num = config_data["server_num"]
    server_exist = models.AutoConfigInfos.objects.filter(server_num=server_num)
    if len(server_exist) == 0:
        models.AutoConfigInfos.objects.create(**config_data)
        print('数据保存成功')
    server_exist.update(
        server_num=config_data["server_num"],
        board=config_data["board"],
        cpu=config_data["cpu"],
        memory_bank=config_data["memory_bank"],
        hard_disk=config_data["hard_disk"],
        raid=config_data["raid"],
        vga=config_data["vga"],
        gpu=config_data["gpu"],
        hba=config_data["hba"],
        net_card=config_data["net_card"],
        fc_card=config_data["fc_card"],
        inspect_time=config_data["inspect_time"],
        ip_info=config_data["ip_info"],
        checkstate=config_data["checkstate"],
        state=config_data["state"],
        status=config_data["status"]
    )
    print('数据库更新成功')
    return HttpResponse()