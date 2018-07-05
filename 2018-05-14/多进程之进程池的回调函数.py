# Author： ninuxer
# Date： 2018/05/16 11:02
# File： 多进程之进程池的回调函数.py


# # 进程池之回调函数
"""
需要回调函数的场景：
进程池中任何一个任务一旦处理完了，就立即告知主进程：
我好了额，你可以处理我的结果了。
主进程则调用一个函数去处理该结果，该函数即回调函数

我们可以把耗时间（阻塞）的任务放到进程池中，
然后指定回调函数（主进程负责执行），
这样主进程在执行回调函数时就省去了I/O的过程，直接拿到的是任务的结果。

如果在主进程中等待进程池中所有任务都执行完毕后，再统一处理结果，则无需回调函数
"""
import multiprocessing
import random
import time
import os
import json


# 子进程执行的函数
def func1(msg):
    num = random.randint(1, 10)
    print('子进程 pid<{}> ppid<{}> 执行 {} 操作，阻塞 {} 秒'.format(
        os.getpid(),
        os.getppid(),
        msg, num
    ))
    time.sleep(num)
    return {'name': 'nwc', 'age': 28, 'info': msg}


# 回调函数,一般情况下，回调函数要使用子进程的返回值,
# 回调函数在主进程中执行
def func2(ret):
    print('回调进程 pid <{}> 执行 {} 的写磁盘操作'.format(os.getpid(),ret['info']))
    with open('json.test', 'a') as f:
        json.dumps(ret, f)


if __name__ == '__main__':
    p = multiprocessing.Pool(3)
    for c in ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']:
        p.apply_async(func=func1, args=(c,), callback=func2)

    p.close()
    p.join()
