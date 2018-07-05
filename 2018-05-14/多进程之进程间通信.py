# Author： ninuxer
# Date： 2018/05/15 10:04
# File： 多进程之进程间通信.py
# 进程间通信之queue和pipe，进程间共享数据manager

# # 进程的Queue
# import multiprocessing
# import random
# import time
# import os
#
#
# # 由于进程间不能共享主进程的数据，因此队列作为参数传入子进程，从而使得多个进程共享主进程的队列
# def func1(q, n):
#     while True:
#         if not q.full():
#             num = random.randint(1, 100)
#             q.put(num)
#             print('子进程：{}_{} 将 {} 加入了队列，当前队列长度 {}'.format(
#                 multiprocessing.current_process().name, n, num, q.qsize()
#             ))
#             time.sleep(0.1)
#
#
# def func2(q, m):
#     while True:
#         if not q.empty():
#             num = q.get()
#             print('子进程：{}_{} 将 {} 取出了队列，当前队列长度 {}'.format(
#                 os.getpid(), m, num, q.qsize()
#             ))
#             time.sleep(1)
#
#
# if __name__ == '__main__':
#     # 进程的Queue直接封装在multiprocess模块中了，而不是单独的模块
#     Q = multiprocessing.Queue(5)
#
#     p1 = multiprocessing.Process(target=func1, args=(Q, 'PRODUCER'))
#     p2 = multiprocessing.Process(target=func2, args=(Q, 'CUSTOM'))
#
#     p1.start()
#     p2.start()


# # 进程间通信之pipe
# """
# 进程的PIPE有点类似于socket的方式，pipe会创建一个管道，获取主进程和子进程之间的两个连接对象，然后主进程
# 和子进程分别调用自己的连接进行send和recv(send和recv时不需要转换为bytes类型，因为其内部已经做了封装)
# 从而实现了通信
# """
# import multiprocessing
# import random
# import time
#
#
# def func1(conn):
#     while True:
#         data = conn.recv()
#         print('### 子进程 收到了{}'.format(data))
#         conn.send(data+100)
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     parent_conn, sub_conn = multiprocessing.Pipe()
#     p1 = multiprocessing.Process(target=func1, args=(sub_conn,))
#     p1.start()
#     while True:
#         num = random.randint(1, 100)
#         print('>>> 父进程将发送 {}'.format(num))
#         parent_conn.send(num)
#         d = parent_conn.recv()
#         print('>>> 父进程 收到了 {}'.format(d))
#         time.sleep(1)


# # 进程间数据共享:Manager
"""
Queue和pipe只是实现了数据交互，并没实现数据共享，即一个进程去更改另一个进程的数据。
manager实际是创建了一种可以在进程间共享的数据结构
"""

import multiprocessing


def func(d, l, n):
    d[str(n)] = n + 10
    d["name"] = 'nwc'
    l[n] = n - 10
    l[0] = 'nnwwcc'


if __name__ == '__main__':
    with multiprocessing.Manager() as m:
        D = m.dict()
        L = m.list(range(20))

        p_list = []
        for i in range(10):
            p = multiprocessing.Process(target=func, args=(D, L, i))
            p.start()
            p_list.append(p)

        for x in p_list:
            x.join()

        print(D)
        print(L)
