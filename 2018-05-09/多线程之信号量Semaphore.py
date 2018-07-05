# Author： ninuxer
# Date： 2018/05/10 14:28
# File： 多线程之信号量Semaphore.py


"""
信号量semaphore：也是一种锁机制，
Semaphore管理一个内置的计数器，每当调用acquire()时内置计数器-1；调用release() 时内置计数器+1；
计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。

相当于定义的时候实现限定锁的个数，然后加锁时计数器-1，释放锁时计数器+1

类似停车场的模型，事先只有多少个车位，加锁就类似入口放车进来，可用车位数-1，
释放锁就像车子出去，可用车位+1
"""
import threading
import time

semp = threading.BoundedSemaphore(5)   # 实例化锁对象，大小为5个
def func(n):
    semp.acquire()
    print('{} ==> 当前线程：{}  获取到了semaphore, 当前时间：{}'.format(n, threading.current_thread().getName(),time.ctime()))
    time.sleep(n+10)
    semp.release()

thead_list = []
for i in range(10):  # 创建10个线程，并启动
    t = threading.Thread(target=func,args=(i,))
    thead_list.append(t)
    t.start()

for th in thead_list:  # 为了所有线程结束后，打印主线程结束的时间
    th.join()

print('主线程结束，当前时间为：{}'.format(time.ctime()))

