# Author： ninuxer
# Date： 2018/05/15 15:03
# File： 多进程之进程池_测试server.py


import multiprocessing
import socket
import random
import os


def func(cn, msg):
    while True:
        s_data = cn.recv(1024)
        if not s_data:
            break
        print('my pid: {}, ppid {} get {}'.format(
            os.getpid(),
            os.getppid(),
            str(s_data, 'utf8')
        ))
        print('will send {}'.format(msg))
        cn.send(bytes(msg, 'utf8'))


if __name__ == '__main__':
    p = multiprocessing.Pool(3)
    sk = socket.socket()
    sk.bind(('127.0.0.1', 59977))
    sk.listen(2)

    while True:
        conn, client_addr = sk.accept()
        s = random.choice([str(random.randint(0, 9)), chr(random.randint(65, 122))])
        p.apply_async(func=func, args=(conn, s))