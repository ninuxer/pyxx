# Author： ninuxer
# Date： 2018/04/16 10:46
# File： 函数_1.py


# def action1(n):
#     print ('starting action1...')
#
#     with open('日志记录','a') as f:
#         f.write('end action%s\n'%n)
#
# def action2(n):
#     print ('starting action2...')
#
#     with open('日志记录','a') as f:
#         f.write('end action%s\n'%n)
#
# def action3(n):
#     print ('starting action3...')
#
#     with open('日志记录','a') as f:
#         f.write('end action%s\n'%n)
#
#
# action1(111)
# action2(2222)
# action3(33333)

# import time
#
# def logger(n):
#     time_format='%Y-%m-%d %X'
#     time_current=time.strftime(time_format)
#
#     with open('日志记录','a') as f:
#         f.write('%s end action%s\n'%(time_current,n))
#
# def action1():
#     print ('starting action1...')
#     logger(1)
#
#
# def action2():
#     print ('starting action2...')
#     logger(2)
#
#
# def action3():
#     print ('starting action3...')
#     logger(3)
#
#
# action1()
# action2()
# action3()



# python中的作用域分4种情况：
#
# L：local，局部作用域，即函数中定义的变量；
# E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的；
# G：globa，全局变量，就是模块级别定义的变量；
# B：built-in，系统固定模块里面的变量，比如int, bytearray等。 搜索变量的优先级顺序依次是：作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB。

# 在Python中，只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如if、try、for等）是不会引入新的作用域的

# 内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，嵌套作用域变量要使用nonlocal关键字。nonlocal是python3新增的关键字，有了这个 关键字，就能完美的实现闭包了。


#### 作用域实例
# x = int(2.9)  # int built-in
#
# g_count = 0  # global
#
#
# def outer():
#     o_count = 1  # enclosing
#
#     def inner():
#         i_count = 2  # local
#         print(o_count)
#
#     # print(i_count) 找不到
#     inner()
#
#
# outer()
#
# # print(o_count) #找不到


# count = 10
# def outer():
#     global count
#     print(count)
#     count = 100
#     print(count)
# outer()
#
# print(count)

# from functools import reduce
#
# number = [2, -5, 9, -7, 2, 5, 4, -1, 0, -3, 8]
#
# print(list(filter(lambda x:x>0,number)))
# print(reduce(lambda a,b: a+b,filter(lambda x:x>0,number))/len(list(filter(lambda x:x>0,number))))

user = ["nwc","mw","test"]
passwd = ["123456","111111","112233"]

# lguser="nwc"
# lgpass="123456"

def lgzsq(u,p):
    def login(fn):
        def inner(*args,**kwargs):
            if user.index(u)+1 > 0 and p == passwd[user.index(u)]:
                print("登陆成功")
                fn(*args, **kwargs)
            else:
                print("用户不存在或密码不正确")
        return inner
    return login



@lgzsq("mw","111111")
def foo(path):
    print("This is the {}".format(path))

foo("/adjht/index.html")