# Author： ninuxer
# Date： 2018/05/10 16:45
# File： 多线程之条件变量同步Condition.py


"""
也是一种锁,可实现线程间通知机制
有一类线程需要满足条件之后才能够继续执行，Python提供了threading.Condition 对象用于条件变量线程的支持，
它除了能提供RLock()或Lock()的方法外，还提供了 wait()、notify()、notifyAll()方法。
lock_con=threading.Condition([Lock/Rlock])： 锁是可选选项，不传入锁，对象自动创建一个RLock()。
wait()：条件不满足时调用，线程会释放锁并进入等待阻塞；
notify()：条件创造后调用，通知等待池激活一个线程，括号内可填入整数，表示激活多少个线程；
notifyAll()：条件创造后调用，通知等待池激活所有线程。
"""

import threading
import random
import time


def product():
    global L
    while True:
        i = random.randint(1,100)
        if lk.acquire():
            L.append(i)
            print('>>厨师：{} 往队列里加入 {} 包子, 当前队列内容：{}'.format(threading.current_thread().getName(), i, L))
            lk.notify()
            lk.release()
        time.sleep(3)


def consumer():
    global L
    while True:
        lk.acquire()
        if not L:
            lk.wait()
        print('##屁民：{} 从队列里取出 {} 包子, 当前队列内容：{}'.format(threading.current_thread().getName(), L.pop(0), L))
        lk.release()
        time.sleep(0.25)


if __name__ == '__main__':
    L = []
    lk = threading.Condition()

    thead_list = []
    for i in range(3):
        t = threading.Thread(target=product)
        thead_list.append(t)

    tc = threading.Thread(target=consumer)
    thead_list.append(tc)

    for i in thead_list:
        i.start()



# import threading,time
# from random import randint
# class Producer(threading.Thread):
#     def run(self):
#         global L
#         while True:
#             val=randint(0,100)
#             print('生产者',self.name,":Append"+str(val),L)
#             if lock_con.acquire():
#                 L.append(val)
#                 lock_con.notify()
#                 lock_con.release()
#             time.sleep(3)
# class Consumer(threading.Thread):
#     def run(self):
#         global L
#         while True:
#                 lock_con.acquire()
#                 if len(L)==0:
#                     lock_con.wait()
#                 print('消费者',self.name,":Delete"+str(L[0]),L)
#                 del L[0]
#                 lock_con.release()
#                 time.sleep(0.25)
#
# if __name__=="__main__":
#
#     L=[]
#     lock_con=threading.Condition()
#     threads=[]
#     for i in range(5):
#         threads.append(Producer())
#     threads.append(Consumer())
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()