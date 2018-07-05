# Author： ninuxer
# Date： 2018/05/14 11:07
# File： 多进程之创建方式.py


"""
多进程multiprocess模块与多线程threading模块的接口基本一致
join()、setDeamon()等方法基本一致
"""

# # 创建进程方式一：
# import multiprocessing
# import os
#
#
# def func(n):
#     print('{} is run now,my PID is {}, parent_pid is {}'.format(n, os.getpid(), os.getppid()))
#
#
# if __name__ == '__main__':  # 在windows系统下，主进程的内容要加到main下，否则会报错
#     p_list = []
#
#     for i in range(5):
#         p = multiprocessing.Process(target=func, args=(i,))
#         p.start()
#         p_list.append(p)
#
#     # 有了join，因此主进程的此print会在所有子进程结束后才打印
#     for j in p_list:
#         j.join()
#     print('I am main process,my pid is {}'.format(os.getpid()))


# 创建进程的方式二

import multiprocessing
import os


class MyProcess(multiprocessing.Process):
    def __init__(self, n):
        super(MyProcess, self).__init__()
        self.name = n

    def run(self):
        print('{} is run now,my PID is {}, parent_pid is {}'.format(self.name, os.getpid(), os.getppid()))


if __name__ == '__main__':

    for i in range(5):
        name = 'nwc'+str(i)
        p = MyProcess(name)
        p.start()

    print('I am main process,my pid is {}'.format(os.getpid()))

