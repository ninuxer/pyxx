# Author： ninuxer
# Date： 2018/04/18 17:05
# File： configparser模块.py


import configparser


##  生成ini风格的文件

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'web1': '192.168.1.2',
    'web2': '10.200.1.1',
    'web3': '172.16.1.1'
}

config['SSH'] = {
    'Port': 8000,
    'Host': '10.200.11.110',
    'Service': ['http','php','python']
}

config['WEB'] = {
    'ServerName': 'www.suning.com',
    'DocumentRoot': '/data/www',
    'Port': 8080,
    'web1': '1.1.1.1',
    'web3': '2.2.2.2'
}

with open('example.ini','w') as f:
    config.write(f)


## 获取ini的内容

import configparser

config1 = configparser.ConfigParser()

config1.read('example.ini')

print(config1.sections())  # 只会显示非DEFAULT的配置段

print('SHH' in config1)
print('SSH' in config1)
print('web1' in config1)
print('Port' in config1)

if 'port' in config1['SSH']:
    print("###############yes")
else:
    print("###############no")


print(config1['DEFAULT'])
print(config1['DEFAULT']['web1'])
print(config1['SSH']['Service'])

for i in config1['WEB']:   # 会打印WEB配置段与DEFAULT配置段的并集的配置项
    print(i)


print(config1.items('WEB'))

print(config1.get('WEB','Servername'))


## 增删改ini文件

import configparser


config2 = configparser.ConfigParser()

config2.read('example.ini')

config2.add_section('NINUXER')
print(config2.sections())

config2.remove_section('NINUXER')
print(config2.sections())

print(config2.items('SSH'))
config2.remove_option('SSH','Port')
print(config2.items('SSH'))

print(config2.get('SSH','host'))
config2.set('SSH','host','8.8.8.8')
print(config2.get('SSH','host'))

config2.write(open('example_2.ini','w'))


