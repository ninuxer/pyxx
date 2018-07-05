# Author： ninuxer
# Date： 2018/05/16 15:13
# File： yield实现的协程.py

"""
对于单线程下，我们不可避免程序中出现io操作，
但如果我们能在自己的程序中（即用户程序级别，而非操作系统级别）控制
单线程下的多个任务能在一个任务遇到io阻塞时就切换到另外一个任务去计算，
这样就保证了该线程能够最大限度地处于就绪态，即随时都可以被cpu执行的状态，
相当于我们在用户程序级别将自己的io操作最大限度地隐藏起来，
从而可以迷惑操作系统，让其看到：该线程好像是一直在计算，io比较少，
从而更多的将cpu的执行权限分配给我们的线程。
"""
# # yield生成器回顾
# def func(n):
#     for i in range(n):
#         print(i)
#         new = yield i
#         print('传入的值为 {}'.format(new))
#
#
# c = func(5)  # 此时并不能真正执行func函数，要调用next或send才能执行
# ret = next(c)
# # next与send方法都能让生成器进行下一次执行，直到下一个yield；
# # 如果yield前有变量接收值，则要用send
# # 当调用send时，第一次调用，只能用next或send(None)，
# # 因为第一次进入时，并不直到send的值传入哪里
# c.send('nnnwwwccc')
# c.send('mw')
# c.send('nnn')
# c.send('www')
# c.send('ccc')  # 由于迭代器已经结束，故会报StopIteration


# # yield实现的协程示例
def consumer(name):
    while True:
        print('====')
        baozi = yield
        print('>>>屁民<{}>开始吃<{}>号包子'.format(name, baozi))


def producer(name):
    c1 = consumer('LiLei')  # 创建consumer这个生成器的对象
    # c2 = consumer('HanMeiMei')

    next(c1)  # 调用yield前有变量接受值时，第一次调用需要用next或send(None)
    # next(c2)

    for i in range(3):
        print('###厨师<{}>开始做<{}>号包子'.format(name, i))
        c1.send(i)
        # c2.send(i)


producer('Ninuxer')


