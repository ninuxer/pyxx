# Author： ninuxer
# Date： 2018/05/07 17:32
# File： socket_client2.py


import socket


sk = socket.socket()

srvaddr = ('10.200.11.110', 59977)
sk.connect(srvaddr)

while True:
    inp = input('请输入执行的命令：')
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))
    data = sk.recv(1024)
    print(str(data, 'utf8'))
sk.close()