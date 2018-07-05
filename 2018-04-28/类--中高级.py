# Author： ninuxer
# Date： 2018/05/03 9:43
# File： 类--中高级.py


#### 类的成员修饰符(公有、私有)
#### 私有字段和方法只能在类内部调用，无法在外部调用，且无法继承
# class F1:
#     __country = 'china'   # 私有字段
#     work = 'ops'    # 公有字段
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__id = '429008XXXX1122'
#
#     def show(self):   # 公有方法
#         print('show方法,私有字段__country为：%s' % self.__country)
#         print('ID为{}'.format(self.__id))
#
#     def __showinfo(self):  # 私有方法
#         print(self.__country,'==>',self.work)
#
#
# class S1(F1):
#     def __init__(self,name,age,gender):
#         self.gender = gender
#         super(S1,self).__init__(name,age)
#
#
# obj = S1('nwc',23,'M')
# # print(obj.__country)  # 报错，因为__country是父类的私有字段，无法继承
# # obj.__showinfo() # 报错，因为__showinfo是父类的私有方法，无法继承
# print(obj.work)
# print(obj.name)
# obj.show()


### 类的一些常用的特殊成员

# class F:
#     '''
#     描述信息，在py中用  类.__doc__进行调用
#     '''
#
#     def __init__(self,name):  #构造方法，用 类() 创建对象时，调用此方法
#         self.name = name
#
#     def __del__(self):  # 析构方法，在对象被销毁时会自动执行此方法，但对象何时被销毁是由python解释器决定的
#         pass
#
#     def __call__(self, *args, **kwargs):  #实例化出来的对象使用  对象()  方式时，调用此方法
#         print('11223344 ==> %s' % self.name)
#
#     # __dict__方法，用于获取类或对象中的所有成员，一般不需要定义，是自带的
#
#     def __str__(self):  # 使用str(对象) 或 print(对象)  时调用此方法
#         return 'nwc'
#
#     def __getitem__(self, item):  # 使用类似列表索引取值或切片 对象[X] 时调用，当取值时，item类型为int、当切片时，item类型为slice
#         print(type(item))
#         if isinstance(item,slice):
#             print("切片处理")
#             print('起始位置为：{}，终止位置为：{}，步长为：{} '.format(item.start,item.stop,item.step))
#         else:
#             print('索引取值处理，索引为{}'.format(item))
#
#     def __setitem__(self, key, value):  # 使用类似列表索引设置值或切片赋值  对象[X] = Y  时调用
#         if isinstance(key,slice):
#             print("切片处理--set")
#             print('起始位置为：{}，终止位置为：{}，步长为：{} '.format(key.start,key.stop,key.step))
#         else:
#             print('索引取值处理--set，索引为{}'.format(key))
#
#     def __delitem__(self, key):  # 使用类似列表索引删除或切片删除  del 对象[X]  时调用
#         if isinstance(key,slice):
#             print("切片处理--del")
#             print('起始位置为：{}，终止位置为：{}，步长为：{} '.format(key.start,key.stop,key.step))
#         else:
#             print('索引取值处理--del，索引为{}'.format(key))
#
#     def __iter__(self):   # 当定义了此方法后，对象就是可迭代对象
#         return iter([11,22,33])
#
#     # for循环内部，如果for遍历的目标是迭代器，则直接用其next()进行遍历；
#     # 如果for的目标是可迭代对象，则利用其__iter__方法将其转换为迭代器，然后进行遍历
#
#     def __add__(self, other):   # 当两个对象相加时，会利用第一个对象的__add__方法，将第二个对象当做参数传入；类似的还有加减乘除等
#         print('两个对象相加')
#
#
# obj = F('ninuxer')
# obj()
# str(obj)
# print(F.__dict__)
# print(obj.__dict__)
# obj[8]
# obj[1:10:2]
# obj[8]='aaa'
# obj[1:10:2]='bbb'
# del obj[8]
# del obj[1:10:2]
# for i in obj:
#     print("my name is : {}".format(i))
#
# obj1 = F('newbee')
# obj + obj1











