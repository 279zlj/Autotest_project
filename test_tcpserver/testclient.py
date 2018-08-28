# transfer message from front to C
import socket


# socket.setdefaulttimeout(4)


class Client(object):
    # 从前端传回的数据中应包含 tcp server 的 ip 和 port
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_msg_to_c(self, data):
        """
        从前端发的数据直接通过这个方法转发到 c 程序，
        发送完成即主动关闭连接
        :param data: 要发送的数据
        :return:
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.sendall(data)
            print('send successfully!')
            print('receive data:', client_socket.recv(1024))
            client_socket.close()


c = Client('localhost', 3000)
c.send_msg_to_c(b'BoardName:Z97 Pro3/BisoVersion:P1.20#CpuNum:2/CpuCore:4/CpuInfo:8  Intel(R) Xeon(R) CPU E3-1230 v3 @ 3.30GHz#MemInfo:*ASRock*Intel*Transcend/MemSize:4096MB/MemFreq:1600MT/s#DiskInfo:WDC WD10EURX-73C /DiskNum:1/DiskVer:/ 01.01A01#NetBoardInfo:Intel Corporation Ethernet Connection (2) I218-V#Graphics:LeadTek Research Inc. GK107 [GeForce GT 640] [107d:2737]#server62')
# c.send_msg_to_c(b'old_test:Z97 Pro3/BisoVersion:P1.20#CpuNum:2/CpuCore:4/CpuInfo:8  Intel(R) Xeon(R) CPU E3-1230 v3 @ 3.30GHz#MemInfo:*ASRock*Intel*Transcend/MemSize:4096MB/MemFreq:1600MT/s#DiskInfo:WDC WD10EURX-73C /DiskNum:1/DiskVer:/ 01.01A01#NetBoardInfo:Intel Corporation Ethernet Connection (2) I218-V#Graphics:LeadTek Research Inc. GK107 [GeForce GT 640] [107d:2737]#server62')