# Author： ninuxer
# Date： 2018/05/08 9:39
# File： socket_server3_FileServer.py


import socket
import os

bind_addr = ('127.0.0.1', 59977)
upload_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')

sk = socket.socket()
sk.bind(bind_addr)
sk.listen(3)
print('The File Server Start Success')
print('Server Address is : {}, Port is {}'.format(*bind_addr))


def post_func(conn, storage, filesize):
    has_recv = 0
    f = open(storage, 'ab')
    while has_recv != filesize:
        data = conn.recv(1024)
        if not data: break
        f.write(data)
        has_recv += len(data)
    print('has_recv:{}'.format(has_recv))
    f.close()
    ret = 'Upload {} Success'.format(os.path.basename(storage))
    print('ret is:{}'.format(ret))
    conn.sendall(bytes(ret, 'utf8'))



while True:
    conn, client_addr = sk.accept()
    print('Client {} Connect Success.'.format(client_addr))

    while True:
        try:
            file_meta = conn.recv(1024)
        except Exception:
            break
        if not file_meta: break
        method, filename, filesize = str(file_meta,'utf8').split('|')
        filesize = int(filesize)
        print('FILEsize:{}'.format(filesize))
        file_abs_path = os.path.join(upload_dir, filename)
        if method.lower() == 'post':
            post_func(conn, file_abs_path, filesize)
        elif method.lower() == 'get':
            pass
        else:
            notice = 'Method Not Support'
            print(notice)
            conn.sendall(bytes(notice, 'utf8'))
            break