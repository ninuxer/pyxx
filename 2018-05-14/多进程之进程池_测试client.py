# Author： ninuxer
# Date： 2018/05/15 15:15
# File： 多进程之进程池_测试client.py


import socket


conn = socket.socket()
conn.connect(('127.0.0.1', 59977))

while True:
    inp = input('>>> ')
    if not inp:
        break
    conn.send(bytes(inp, 'utf8'))
    data = conn.recv(1024)
    print(str(data, 'utf8'))