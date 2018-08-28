import socket
import time

ANY = '0.0.0.0'
SENDERPORT = 1601
MCAST_ADDR = '224.0.2.111'
MCAST_PORT = 1600


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.bind((ANY, SENDERPORT))
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
    while True:
        time.sleep(2)
        local_ip = get_host_ip()
        sock.sendto(bytes(local_ip, encoding='utf-8'), (MCAST_ADDR, MCAST_PORT))
        print('本机ip: {}，广播发送成功!'.format(local_ip))
