# Author： ninuxer
# Date： 2018/05/07 17:32
# File： socket_server2.py


import socket
import subprocess


bind_addr = ('127.0.0.1', 59977)
sk = socket.socket()
sk.bind(bind_addr)
sk.listen(3)

print('服务器启动成功，地址：{} 端口：{}'.format(*bind_addr))
while True:
    conn, client_addr = sk.accept()
    print('客户端已连接，客户端地址为{}'.format(client_addr))

    while True:
        try:
            data = conn.recv(1024)
        except Exception as e:
            print(e)
            break
        if not data:
            break
        cmd = str(data, 'utf8')
        data = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        stdata = str(data.stdout.read(), 'gbk')
        conn.send(bytes(stdata, 'gbk'))

sk.close()
