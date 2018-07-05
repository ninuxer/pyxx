# Author： ninuxer
# Date： 2018/05/17 15:45
# File： gevent实现的协程.py


"""
Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，
在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。
Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度

gevent 在遇到IO时会自动切换
"""
# import gevent
#
#
# def func1(a, b, c):
#     print('func1 >>> {}'.format(a))
#     gevent.sleep(2)
#     # gevent.sleep是gevent能识别的阻塞，其他如time.sleep、socket之类的阻塞，要在脚本开始处
#     # from gevent import monkey;monkey.patch_all()   进行声明
#     print('func1 >>> {}'.format(b))
#     gevent.sleep(2)
#     print('func1 >>> {}'.format(c))
#     return 'func1 success'
#
#
# def func2(d, e, f):
#     print('func2 >>> {}'.format(d))
#     gevent.sleep(2)
#     print('func2 >>> {}'.format(e))
#     gevent.sleep(2)
#     print('func2 >>> {}'.format(f))
#     return 'func2 success'
#
#
# g1 = gevent.spawn(func1, 11, 22, 33)  # 类似于进程池的apply_async,相当于执行指定的函数，后面的为参数
# g2 = gevent.spawn(func2, 44, 55, 66)
#
# g1.join()  # 等待g1结束
# g2.join()
# # g1.value可以获取func1的返回值
# print('======Main======\n{}\n{}\n======Done======'.format(g1.value, g2.value))


from gevent import spawn, joinall, monkey;monkey.patch_all()
import time


def task(pid):
    time.sleep(1)
    print('Task {} done {}'.format(pid, time.ctime()))


def task2(pid):
    time.sleep(15)
    print('Task {} done {}'.format(pid, time.ctime()))


def synchronous():
    for i in range(5):
        task(i)


def asynchronous():
    g_l = [spawn(task2, i) for i in range(5)]
    joinall(g_l)


if __name__ == '__main__':
    print('Synchronous:')
    synchronous()

    print('Asynchronous:')
    asynchronous()

