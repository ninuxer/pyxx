# Author： ninuxer
# Date： 2018/05/08 15:17
# File： socketserver_client1.py


import socket

sk = socket.socket()
srvaddr = ('127.0.0.1',59977)
sk.connect(srvaddr)
print('客户端启动')

while True:
    inp = input('>>>>> ')
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf-8'))

    data = sk.recv(1024)
    if data == 'exit':
        break
    print(str(data, 'utf-8'))

sk.close()