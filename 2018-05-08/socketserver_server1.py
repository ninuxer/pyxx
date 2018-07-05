# Author： ninuxer
# Date： 2018/05/08 15:17
# File： socketserver_server1.py


import socketserver


class MySocket(socketserver.BaseRequestHandler):

    def handle(self):
        conn = self.request
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

if __name__ == '__main__':
    sk = socketserver.ThreadingTCPServer(('127.0.0.1', 59977), MySocket)
    sk.serve_forever(5)