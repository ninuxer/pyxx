# Author： ninuxer
# Date： 2018/04/18 14:01
# File： hashlib模块.py


import hashlib


print(hashlib.md5("salt".encode('utf-8')).hexdigest())

print(hashlib.md5(b'salt').hexdigest())

print(hashlib.md5(b'password').hexdigest())
