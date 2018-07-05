# Author： ninuxer
# Date： 2018/04/17 17:16
# File： 生成器_1.py


def producer(name):
    print("{} 开始做包子".format(name))
    xfz = consumer("nwc","mw")
    xfz.send(None)
    for i in range(1,11):
        print("{} 做了第 {} 号包子".format(name,i))
        xfz.send(i)

def consumer(a,b):
    print("{} 和 {} 吃包子 ！！！".format(a,b))
    while True:
        aa = yield 1
        print("{} 号包子被 {} 吃了".format(aa,a))
        bb = yield 2
        print("{} 号包子被 {} 吃了".format(bb,b))


producer("tom")