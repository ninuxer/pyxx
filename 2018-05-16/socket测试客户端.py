# Author： ninuxer
# Date： 2018/05/21 15:08
# File： socket测试客户端.py


import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 59977))
while True:
    inp = input('>>> ')
    if not inp:
        break
    sk.send(bytes(inp, 'utf8'))
    data = sk.recv(1024)
    print(str(data, 'utf8'))
