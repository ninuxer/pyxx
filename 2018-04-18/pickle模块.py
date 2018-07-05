# Author： ninuxer
# Date： 2018/04/18 16:36
# File： pickle模块.py


import pickle

##----------------------------序列化
import pickle

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}

print(type(dic))  # <class 'dict'>

j = pickle.dumps(dic)
print(j)
print(type(j))  # <class 'bytes'>

f = open('序列化对象_pickle', 'wb')  # 注意是w是写入str,wb是写入bytes,j是'bytes'
f.write(j)  # -------------------等价于pickle.dump(dic,f)

f.close()




# -------------------------反序列化
import pickle

f = open('序列化对象_pickle', 'rb')

data = pickle.loads(f.read())  # 等价于data=pickle.load(f)

print(data)
print(data['age'])
print(type(data))

f.close()