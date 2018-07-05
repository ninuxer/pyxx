# Author： ninuxer
# Date： 2018/05/10 9:59
# File： 多线程之同步锁(普通锁).py

# # 没加锁的情况
# import threading
#
#
# def func():
#     global n
#     tmp = n
#     print('OK')
#     n = tmp - 1
#
#
# if __name__ == '__main__':
#     n = 100
#     thread_list = []
#     for i in range(100):
#         t = threading.Thread(target=func)
#         thread_list.append(t)
#         t.start()
#
#     for th in thread_list:
#         th.join()  # 主要是为了让print('n的最终的值: {}'.format(n))在所有线程执行完成后再执行
#
#     print('n的最终的值: {}'.format(n))  # 最终结果可能不是0


import threading


def func():
    global n
    lock.acquire()   # 调用创建的锁对象，在操作公共数据的地方加锁
    tmp = n
    print('OK')
    n = tmp - 1
    lock.release()  # 操作完公共数据，释放锁


if __name__ == '__main__':
    n = 100

    lock = threading.Lock()    # 创建一个 同步(普通)锁的对象

    thread_list = []
    for i in range(100):
        t = threading.Thread(target=func)
        thread_list.append(t)
        t.start()

    for th in thread_list:
        th.join()  # 主要是为了让print('n的最终的值: {}'.format(n))在所有线程执行完成后再执行

    print('n的最终的值: {}'.format(n))  # 最终结果一定是0



