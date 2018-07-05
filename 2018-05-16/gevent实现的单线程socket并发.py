# Author： ninuxer
# Date： 2018/05/21 14:30
# File： gevent实现的单线程socket并发.py


from gevent import monkey;monkey.patch_all()
import gevent
import socket


def server(addr, port):
    sk = socket.socket()
    sk.bind((addr, port))
    sk.listen(5)
    while True:
        conn, cli_addr = sk.accept()
        gevent.spawn(talk, conn, cli_addr)
        # talk(conn, cli_addr)


def talk(conn, cli_addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print('{} <<< {}'.format(cli_addr, str(data, 'utf8')))
        info = 'You are {};You Send {}'.format(cli_addr, str(data, 'utf8'))
        print(info)
        conn.sendall(bytes(info, 'utf8'))


if __name__ == '__main__':
    server('127.0.0.1', 59977)