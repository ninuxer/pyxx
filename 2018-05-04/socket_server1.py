# Author： ninuxer
# Date： 2018/05/04 15:57
# File： socket_server1.py


import socket

sk = socket.socket()

addr = ('127.0.0.1', 53306)

sk.bind(addr)

sk.listen(5)

print('服务器端启动')

while True:
    conn, ad = sk.accept()
    print(ad)
    while True:
        try:
            data = conn.recv(1024)
        except Exception as e:
            print(e)
            break

        if not data:
            break
        print(str(data, 'utf-8'))

        inp = input('>>> ')
        conn.send(bytes(inp, 'utf-8'))

sk.close()

