# transfer message from front to C
import socket


class Client(object):
    # 从前端传回的数据中应包含 tcp server 的 ip 和 port
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_msg_to_c(self, data):
        """
        从前端发的数据直接通过这个方法转发到 c 程序，
        发送完成即主动关闭连接.设置连接超时为 6 秒
        :param data: 要发送的数据
        :return:
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.settimeout(6)
            client_socket.connect((self.host, self.port))
            client_socket.sendall(data)
            client_socket.close()
            client_socket.settimeout(None)
