# Author： ninuxer
# Date： 2018/06/20 9:48
# File： test.py


import json
i = 10
s = 'hello'
t = (1, 4, 6)
l = [3, 5, 7]
d = {'name': 'yuan'}

json_str1 = json.dumps(i)
json_str2 = json.dumps(s)
json_str3 = json.dumps(t)
json_str4 = json.dumps(l)
json_str5 = json.dumps(d)

print(json_str1)   #'10'
print(json_str2)   #'"hello"'
print(json_str3)   #'[1, 4, 6]'
print(json_str4)   #'[3, 5, 7]'
print(json_str5)   #'{"name": "yuan"}'