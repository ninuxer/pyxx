# Author： ninuxer
# Date： 2018/04/28 15:07
# File： card_withdraw.py


import json
from datahandler import handler


def withdraw(sfzid):
    money = input('请输入您要取款的金额：')
    money = int(money)
    info = handler.main(sfzid, 'get')
    info['balance'] -= money
    f = handler.main(sfzid, 'post')
    with open(f, 'w') as fd:
        json.dump(fd, info)
    print("{} 的账户余额为 {}".format(sfzid, info['balance']))
    return info