# Author： ninuxer
# Date： 2018/05/04 11:24
# File： 反射.py


# 反射是通过字符串的形式操作(has、get、set、del)对象相关的成员

# class F:
#     country = 'china'
#
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         return self.name
#
# # 通常我们引用对象中的成员的方式：
# obj = F('nwc')
# print(obj.country)
# ret = obj.show()
# print(ret)
#
# # 使用反射的应用方式：
# obj1 = F('nwc')
# a = hasattr(obj1,'country')
# print(a)
# b = getattr(obj1,'show')
# c = b()
# print(c)
# setattr(obj1,'age',28)
# print(obj1.age)
# delattr(obj1,'name')
#
# # 由于py中一切皆对象，因此可以对类、模块、等使用反射
# f = hasattr(F,'show')
# print(f)
#
# fn = getattr(F,'country')
# print(fn)

# import sys
# print(sys.path)

import wokers

while True:
    cho = input("想要的页面：")
    if hasattr(wokers,cho):
        fn = getattr(wokers,cho)
        fn()
    else:
        print("404 not found")
