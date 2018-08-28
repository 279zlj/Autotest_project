# 测试用例，模仿c程序的监听
import socket
import _thread
from client.c_client import Client


def process_request(connection):
    data = connection.recv(2048)
    data = data.decode('utf-8')
    print('接收到的数据', data)
    client = Client('192.168.1.221', 3000)
    client.send_msg_to_c(b'BoardName:Z97 Pro3/BisoVersion:P1.20#CpuNum:2/CpuCore:4/CpuInfo:8  Intel(R) Xeon(R) CPU E3-1230 v3 @ 3.30GHz#MemInfo:*ASRock*Intel*Transcend/MemSize:4096MB/MemFreq:1600MT/s#DiskInfo:WDC WD10EURX-73C /DiskNum:1/DiskVer:/ 01.01A01#NetBoardInfo:Intel Corporation Ethernet Connection (2) I218-V#Graphics:LeadTek Research Inc. GK107 [GeForce GT 640] [107d:2737]#server_number50')
    print('发送数据成功')
    connection.close()
    print('socket关闭')


def run(host='', port=4000):
    """
    启动服务器
    """
    print('socket server start at', '{}:{}'.format(host, port))
    with socket.socket() as s:
        s.bind((host, port))
        s.listen(60)
        while True:
            connection, address = s.accept()
            print('区分', connection.getpeername()[1])
            print('连接成功, 使用多线程处理请求', address)
            _thread.start_new_thread(process_request, (connection,))


if __name__ == '__main__':
    config = dict(
        host='',
        port=5000,
    )
    run(**config)
