# Author： ninuxer
# Date： 2018/04/18 16:19
# File： json模块.py




import json


# json.dump()
# json.dumps()
#
# json.load()
# json.loads()


# i = 10
# s = 'abc'
# t = (1,2,3)
# l = [4,5,6]
# d = {'name': 'nwc','age': 18, 11: 22, 'like': ["aa","bb"]}
#
# print(type(i))
# print(type(s))
# print(type(t))
# print(type(l))
# print(type(d))
#
#
# # ji1 = json.dumps(i)
# with open('test.log','w') as  f:
#     ji2 = json.dump(i,f)
#
# # print(ji1)
#     print(ji2)
#
# # print(type(ji1))
#     print(type(ji2))
#
# with open('test.log','r') as  f1:
#     ji3 = json.load(f1)
#     ji4 = json.loads(ji3)
#     print(ji3)
#     print(type(ji3))
#     print(ji4)
#     print(type(ji4))



#----------------------------序列化
import json

dic={'name':'alvin','age':23,'sex':'male'}
print(type(dic))#<class 'dict'>

data=json.dumps(dic)
print("type",type(data))#<class 'str'>
print("data",data)


f=open('序列化对象_json','w')
f.write(data)  #-------------------等价于json.dump(dic,f)
f.close()


#-----------------------------反序列化<br>
import json
f=open('序列化对象_json')
new_data=json.loads(f.read())  #  等价于data=json.load(f)

print(new_data)
print(type(new_data))