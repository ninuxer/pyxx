# Author： ninuxer
# Date： 2018/04/20 16:14
# File： subprocess模块.py


import subprocess


ret = subprocess.Popen(r'dir C:\\', shell=True, stdout=subprocess.PIPE)
print(ret.stdout.read().decode('gbk'))


















