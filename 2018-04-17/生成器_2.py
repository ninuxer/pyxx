# Author： ninuxer
# Date： 2018/04/17 17:49
# File： 生成器_2.py


def f():

    yield 5
    print("ooo")
    return
    yield 6
    print("ppp")
        # if str(tem)=='None':
        #     print("ok")

f=f()
print(f.__next__())
print(f.__next__())
# for i in f:
#     print(i)