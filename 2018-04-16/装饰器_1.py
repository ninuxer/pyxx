# Author： ninuxer
# Date： 2018/04/16 10:23
# File： 装饰器_1.py


import time


def zsq_1(fn):
    def inner(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print("运行时长为：{}".format(end-start))
    return inner


@zsq_1
def myfunc_1(a, b):
    print(a+b)
    time.sleep(2)


myfunc_1(2, 3)
