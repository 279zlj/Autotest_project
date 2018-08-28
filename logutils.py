import time
import os


def django_log(*args, **kwargs):
    """
    保存 log 日志信息
    :param args:
    :param kwargs:
    :return:
    """
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time())))
    path = os.path.join('log', 'django_logfile.txt')
    with open(path, 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def tcp_log(*args, **kwargs):
    """
    保存 log 日志信息
    :param args:
    :param kwargs:
    :return:
    """
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time())))
    # path = os.path.join('D:\Autotestproject\Autotest_project\log', 'tcp_logfile.txt')
    path = os.path.join('log', 'tcp_logfile.txt')
    with open(path, 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


