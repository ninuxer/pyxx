# Author： ninuxer
# Date： 2018/05/08 9:40
# File： socket_client3_FileClient.py


import socket
import os

srv_addr = ('127.0.0.1', 59977)
sk = socket.socket()
sk.connect(srv_addr)

while True:
    inp = input('请输入您要上传的文件的绝对路径：')
    if inp == 'exit':
        break
    if not os.path.isabs(inp):
        print('您要上传的文件路径不正确，请重新输入！')
        continue
    elif not os.path.isfile(inp):
        print('您要上传的文件不存在，请重新输入！')
        continue

    filesize = os.stat(inp).st_size
    filename = os.path.basename(inp)
    file_meta = 'post|{}|{}'.format(filename, filesize)
    print(file_meta)
    sk.sendall(bytes(file_meta, 'utf8'))
    f = open(inp, 'rb')
    has_sent = 0
    while has_sent != filesize:
        data = f.read(1024)
        dlen = len(data)
        sk.sendall(data)
        has_sent += dlen
    post_ret = sk.recv(1024)
    print(str(post_ret, 'utf8'))


