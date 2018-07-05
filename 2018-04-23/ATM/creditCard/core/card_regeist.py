# Author： ninuxer
# Date： 2018/04/23 10:27
# File： card_regeist.py


import datetime, json
from datahandler import handler


def regeister(sfzid):
    name = input("请输入您的姓名：")
    password = input("请输入您的密码：")

    filepath = handler.main(sfzid, 'post')

    info = {
        'sfzid': sfzid,
        'name': name,
        'password': password,
        'regeistTime': str(datetime.datetime.now()),
        'expireTime': str(datetime.datetime.now() + datetime.timedelta(days=3650)),
        'payback': 22,
        'balance': 0,
        'quota': 15000,
        'status': 0
        # 0 正常；1 锁定；
    }

    print(filepath)
    print(info)
    print(type(info))
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(info, f)

        print("{} 注册成功，注册信息为: {}".format(sfzid,info))

        return info





