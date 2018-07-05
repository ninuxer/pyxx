# Author： ninuxer
# Date： 2018/05/14 15:01
# File： 多进程之join和daemon方法.py


import multiprocessing
import os
import time


def func(n):
    for i in range(n):
        print('{} is run,pid is {},ppid is {}'.format(i, os.getpid(), os.getppid()))


if __name__ == '__main__':
    p = multiprocessing.Process(target=func, args=(100,))
    p.daemon = True   # daemon默认为false，将子进程的daemon属性设置为true，则主进程结束时，子进程也会随之结束
    p.start()

    time.sleep(0.17)  # 设置主进程的sleep是为了让子进程有结果出来，否则只会显示主进程的输出
    print('I an main,my pid is {}'.format(os.getpid()))