# Author： ninuxer
# Date： 2018/04/28 10:01
# File： 类--初级.py

###### ATM项目的信用卡业务类的实现实例
# import os
# import json
#
#
# class CreditCard:
#     def __init__(self, sfzid, passwd):
#         self.sfzid = sfzid
#         self.password = passwd
#         self.file = os.path.join(r'D:\工作相关文档\python-study\oldboy\2018-04-23\ATM\creditCard\files', id)
#
#     def auth(self):
#         auth_status = 0
#         if os.path.isfile(self.file):
#             with open(self.file, 'r') as f:
#                 info = json.load(f)
#                 if self.sfzid == info['sfzid'] and self.password == info['password']:
#                     auth_status = 1
#                     return auth_status
#                 else:
#                     return auth_status
#         else:
#             auth_status = 2
#             return auth_status
#
#     def query(self):
#         with open(self.file, 'r') as f:
#             info = json.load(f)
#             return info
#
# id = input("请输入您的账号：")
# pwd = input("请输入您的密码：")
# mycard = CreditCard(id, pwd)
#
# if mycard.auth() == 1:
#     print(mycard.query())




########## 多继承

# class D():
#     def bar(self):
#         print('D.bar')
#
# class C(D):
#     def bar(self):
#         print('C.bar')
#
#     def foo(self):
#         print('C.foo')
#
# class B(D):
#     def bar(self):
#         print('B.bar')
#
#     def foo(self):
#         self.fooX()
#         print('B.foo')
#
#     def fooX(self):
#         print('B.fooX')
#
# class A(B, C):
#     def bar(self):
#         print('A.bar')
#
#     def fooX(self):
#         print('A.fooX')
#
#
# a = A()
# a.foo()
# 当执行a.foo()时，会找到B这个父类中的foo方法，执行，因为self不管在父类还是子类中始终都是代指调用方法的对象，因此self始终都是代表a这个对象，故在执行B中的foo方法中的self.fooX()
# 方法时，相当于执行了a.fooX(),因此此处不会执行B中的fooX()方法，而是会重新按照A中定义的父类的查找持续，进行查找，因此此处执行的是A中的fooX()方法；



######## 字段、方法的类型

### 静态字段和普通字段
# class F1:
#     country = 'china'   # 静态字段，保存在类的内存中
#
#     def __init__(self, name):
#         self.name = name   # 普通字段，保存在对象的内存中
#
# f = F1('nwc')
# print(F1.country)
# print(id(F1.country))
# print(f.country)  # 通过对象中的类对象指针寻找到的类中的字段
# print(id(f.country))

### 方法的类型

# class F1:
#     def __init__(self, name):
#         self.name = name
#
#     def func1(self):
#         print('普通方法：%s' % self.name)
#
#     @classmethod   # 表示此方法是类方法
#     def func2(cls):  # 需传入cls这个默认参数，指代当前类
#         print('类方法func2')
#
#     @staticmethod   # 表示此方法是静态方法
#     def func3():   # 无需传入self、cls这种默认参数
#         print('静态方法func3')
#
#
# obj = F1('nwc')
# obj.func1()
# obj.func2()
# obj.func3()
# print('#########')
# F1.func2()  # 静态方法和类方法可以直接用类名进行调用
# F1.func3()




### 属性（定义时以方法的语法进行定义，调用时以字段的语法进行调用）

# class F1:
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def mytest(self):  #  可以没有返回值，因为只是声明mytest为属性
#         print('声明并获取mytest为属性')
#
#     @mytest.setter
#     def mytest(self, value):  # 一般需要接受额外的参数，因为接受参数才能设定新的值
#         print('setter属性，使用=时调用此方法：==> {}'.format(value))
#         return value
#
#     @mytest.deleter
#     def mytest(self):  # 可以没有返回值，因为进作为删除时调用
#         print('del方法，使用del XXX时调用')
#
#
# obj = F1('nwc')
# obj.mytest  # 调用@property装饰器装饰的方法
# obj.mytest = 123  # 调用@mytest.setter装饰器装饰的方法，123作为参数传入此方法
# del obj.mytest  # 调用@mytest.deleter装饰器装饰的方法

# 定义属性的第二种方法
# class F1:
#     def __init__(self, name):
#         self.name = name
#
#     def func1(self):  #  可以没有返回值，因为只是声明mytest为属性
#         print('声明并获取mytest为属性')
#
#     def func2(self, value):  # 一般需要接受额外的参数，因为接受参数才能设定新的值
#         print('setter属性，使用=时调用此方法：==> {}'.format(value))
#         return value
#
#     def func3(self):  # 可以没有返回值，因为进作为删除时调用
#         print('del方法，使用del XXX时调用')
#
#     mytest = property(func1, func2, func3, '描述')
#     """mytest1 = property(fget=func1,fset=func2,fdel=func3)  功能与上述定义方式一致"""
#     # property支持4个参数，第一个为get属性时调用的方法名，第二个为设置属性时调用的方法名，
#     # 第三个为删除属性时调用的方法名，第四个为描述信息(可以没有)
#
#
# obj = F1('nwc')
# obj.mytest  # 调用func1方法
# obj.mytest = 123  # 调用func2方法，123作为参数传入此方法
# del obj.mytest  # 调用func3方法