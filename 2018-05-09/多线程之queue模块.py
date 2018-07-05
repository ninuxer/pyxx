# Author： ninuxer
# Date： 2018/05/11 10:00
# File： 多线程之queue模块.py


"""
quque模块是用于多线程场景下的，实现多线程同时操作公有数据时的有效解决方案
在此前没有queue时，多线程操作公有数据时，我们根据应用场景不同，要对应的加不同类型的锁
而有了queue模块，则无需我们手动加锁，因为queue内部封装了锁的功能，我们只需关注业务逻辑即可
"""

# import threading
# import queue
# import time
# import random
#
#
# class MyThread(threading.Thread):
#     def __init__(self, name, n):
#         super(MyThread, self).__init__()
#         self.name = name
#         self.n = n
#
#     def producer(self):
#         while True:
#             if not Q.full():
#                 num = random.randint(1, 100)
#                 Q.put(num)  # put支持第2个参数，0或1，表示当队列满时，是否阻塞
#                 print('>>> {}-{} 将 {} 包子加入队列,当前队列长度 {}'.format(self.name,self.n,num,Q.qsize()))
#             time.sleep(1)
#
#     def customer(self):
#         while True:
#             if not Q.empty():
#                 num = Q.get()   # get支持参数，0或1，表示当队列空时，是否阻塞
#                 print('### {}-{} 将 {} 包子取出队列,当前队列长度 {}'.format(self.name,self.n,num,Q.qsize()))
#             time.sleep(1)
#
#     def run(self):
#         if self.name == 'producer':
#             self.producer()
#         else:
#             self.customer()
#
#
# if __name__ == '__main__':
#     # 括号内可填数字，代表队列最大长度;Queue创建的默认是先进先出的队列，其还可以用queue模块的其他类创建先进后出、优先级队列
#     Q = queue.Queue(5)
#     for i in range(1, 6):
#         tp = MyThread('producer', i)
#         tp.start()
#
#     for i in ['I', 'II', 'III']:
#         tc = MyThread('consumer', i)
#         tc.start()


# # queue实践：
# 一个线程不断向队列里插入随机数
# 一个线程不断从队列里取出奇数
# 一个线程不断从队列里取出偶数
import threading
import queue
import random
import time


Q = queue.Queue(10)


def producer(t_name):
    while True:
        if not Q.full():
            num = random.randint(1, 100)
            Q.put(num)
            print('{} 将 {} 加入了队列,队列长度：{}'.format(t_name, num, Q.qsize()))

def choice_o(t_name):
    while True:
        if not Q.empty():
            num = Q.get()
            if num%2 == 0:
                print('偶数线程：{} 将 {} 取出了队列,队列长度：{}'.format(t_name, num, Q.qsize()))
            else:
                Q.put(num)


def choice_j(t_name):
    while True:
        if not Q.empty():
            num = Q.get()
            if num%2 != 0:
                print('奇数线程：{} 将 {} 取出了队列,队列长度：{}'.format(t_name, num, Q.qsize()))
            else:
                Q.put(num)


for i in range(5):
    t = threading.Thread(target=producer,args=('生产者',))
    j = threading.Thread(target=choice_j,args=(i,))
    o = threading.Thread(target=choice_o,args=(i,))

    t.start()
    j.start()
    o.start()


