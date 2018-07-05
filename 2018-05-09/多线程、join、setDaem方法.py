# Author： ninuxer
# Date： 2018/05/09 10:14
# File： 并发编程之--多线程(threading模块).py


"""
对于IO密集型应用，推荐使用多线程
对于cpu(计算)密集型应用，推荐使用多进程、协程等方案
"""


# import threading
# import time
#
# def f1(n):
#     for i in [1, 2]:
#         print('现在第 {} 次运行：{}'.format(i, n))
#         time.sleep(2)   # sleep的操作，类似IO，因此cpu会切换到其他线程执行
#         print('停止 {} 第 {} 次'.format(n, i))
#
#
# def f2(n):
#     for i in ['I', 'II']:
#         print('now start {} run：{}'.format(i, n))
#         time.sleep(3)     # sleep的操作，类似IO，因此cpu会切换到其他线程执行
#         print('stop {} run {} times'.format(n, i))
#
#
# if __name__ == '__main__':
#     stime = time.time()
#     # 实例化一个线程对象，target是该线程要运行的任务对象，args是以元组形式传递给任务对象的参数
#     thread1 = threading.Thread(target=f1, args=('吃饭',))
#     # 实例化另一个线程对象
#     thread2 = threading.Thread(target=f2, args=('睡觉',))
#     thread1.start()  # 启动对应的线程
#     thread2.start()
#     print('我是主线程~~~')
#     etime = time.time()
#     print(etime-stime)
#
# """
# 执行顺序：
# 先执行f1的第一个print，然后由于有sleep类似有IO操作，因此cpu此时执行f2
# 然后执行f2的第一个print，然后sleep，然后执行主线程的print和print时间，由于此时f1、f2都在sleep，但f2的sleep时间长，
# 当到达f1的sleep时间后，执行f1的第二个print
# 然后执行f1的for循环的第二次循环中的第一个print，然后sleep，此时,f2和f1都在sleep，当达到f2的sleep时，执行f2的第二次print
# 然后执行f2的for循环的第二次循环中的第一个print，然后执行sleep，然后执行f1的第二次循环的第二个print，然后等f2的sleep时间到了
# 就执行f2的第二次循环的第二个print
# """
# """
# 现在第 1 次运行：吃饭
# now start I run：睡觉
# 我是主线程~~~
# 0.0009999275207519531
# 停止 吃饭 第 1 次
# 现在第 2 次运行：吃饭
# stop 睡觉 run I times
# now start II run：睡觉
# 停止 吃饭 第 2 次
# stop 睡觉 run II times
# """


# # 线程创建的第二种方式：
#
# import threading
# import time
#
#
# class MyThread1(threading.Thread):
#     def __init__(self, n):
#         super(MyThread1, self).__init__()
#         self.n = n
#
#     def run(self):
#         for i in [1, 2]:
#             print('现在第 {} 次运行：{}'.format(i, self.n))
#             time.sleep(2)   # sleep的操作，类似IO，因此cpu会切换到其他线程执行
#             print('停止 {} 第 {} 次'.format(self.n, i))
#
#
# class MyThread2(threading.Thread):
#     def __init__(self, n):
#         super(MyThread2, self).__init__()
#         self.n = n
#
#     def run(self):
#         for i in ['I', 'II']:
#             print('now start {} run：{}'.format(i, self.n))
#             time.sleep(3)     # sleep的操作，类似IO，因此cpu会切换到其他线程执行
#             print('stop {} run {} times'.format(self.n, i))
#
#
# if __name__ == '__main__':
#     stime = time.time()
#     thread1 = MyThread1('吃饭')
#     thread2 = MyThread2('睡觉')
#     thread1.start()  # 启动对应的线程
#     thread2.start()
#
#     print('我是主线程。。。。。')
#     etime = time.time()
#     print(etime-stime)


# join方法
# import threading
# import time
#
#
# def f1(n):
#     for i in [1, 2]:
#         print('现在第 {} 次运行：{}'.format(i, n))
#         time.sleep(2)   # sleep的操作，类似IO，因此cpu会切换到其他线程执行
#         print('停止 {} 第 {} 次'.format(n, i))
#
#
# def f2(n):
#     for i in ['I', 'II']:
#         print('now start {} run：{}'.format(i, n))
#         time.sleep(3)     # sleep的操作，类似IO，因此cpu会切换到其他线程执行
#         print('stop {} run {} times'.format(n, i))
#
#
# if __name__ == '__main__':
#     stime = time.time()
#     # 实例化一个线程对象，target是该线程要运行的任务对象，args是以元组形式传递给任务对象的参数
#     thread1 = threading.Thread(target=f1, args=('吃饭',))
#     # 实例化另一个线程对象
#     thread2 = threading.Thread(target=f2, args=('睡觉',))
#     thread1.start()  # 启动对应的线程
#     thread2.start()
#
#     # thread1.join()  # 相当于阻塞，只有当thread1完成后，才能继续往下执行
#     thread2.join()
#
#     print('我是主线程~~~')
#     etime = time.time()
#     print(etime-stime)


# # setDaemon方法
"""
无论是进程还是线程，都遵循：守护xxx会等待主xxx运行完毕后被销毁

需要强调的是：运行完毕并非终止运行
#1.对主进程来说，运行完毕指的是主进程代码运行完毕
#2.对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程统统运行完毕，主线程才算运行完毕

详细解释：
#1 主进程在其代码结束后就已经算运行完毕了（守护进程在此时就被回收）,然后主进程会一直等非守护的
子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束，

#2 主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。因为主线程的结束意味着
进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束。
"""

import time
from threading import Thread

def sayhi(name):
    time.sleep(2)
    print('%s say hello' %name)

if __name__ == '__main__':
    t=Thread(target=sayhi,args=('egon',))
    t.setDaemon(True)  #必须在t.start()之前设置
    t.start()
    print('主线程')
    print(t.is_alive())


# 让人误解的setDaemon方法
# from threading import Thread
# import time
# def foo():
#     print(123)
#     time.sleep(1)
#     print("end123")
#
# def bar():
#     print(456)
#     time.sleep(3)
#     print("end456")
#
#
# t1=Thread(target=foo)
# t2=Thread(target=bar)
#
# t1.daemon=True
# t1.start()
# t2.start()
# print("main-------")