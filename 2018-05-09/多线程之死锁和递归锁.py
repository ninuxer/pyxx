# Author： ninuxer
# Date： 2018/05/10 11:04
# File： 多线程之死锁和递归锁.py


# # 死锁示例
# import threading
#
#
# def func1():
#     lockA.acquire()
#     print('func1 >>> lockA')
#     lockB.acquire()
#     print('func1 >>> lockB')
#     lockB.release()
#     lockA.release()
#
#
# def func2():
#     lockB.acquire()
#     print('func2 ##### lockB')
#     lockA.acquire()
#     print('func2 ##### lockA')
#     lockA.release()
#     lockB.release()
#
#
# if __name__ == '__main__':
#     lockA = threading.Lock()
#     lockB = threading.Lock()
#     for i in range(10):
#         t1 = threading.Thread(target=func1)
#         t2 = threading.Thread(target=func2)
#         t1.start()
#         t2.start()



# # 递归锁示例
# (递归锁内部维护了一个锁对象和一个计数器，每加锁一次，计数器+1，每释放锁一次，计数器-1，
# 锁内部嵌套锁，因此就叫递归锁)
import threading

def func1():
    lock.acquire()
    print('func1 >>> lockA')
    lock.acquire()
    print('func1 >>> lockB')
    lock.release()
    lock.release()

def func2():
    lock.acquire()
    print('func2 ##### lockB')
    lock.acquire()
    print('func2 ##### lockA')
    lock.release()
    lock.release()

if __name__ == '__main__':
    lock = threading.RLock()   # 把创建锁对象的Lock变为RLock即可
    for i in range(10):
        t1 = threading.Thread(target=func1)
        t2 = threading.Thread(target=func2)
        t1.start()
        t2.start()