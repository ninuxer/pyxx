# Author： ninuxer
# Date： 2018/04/23 11:08
# File： card_recharge.py


import json
from datahandler import handler



def recharge(sfzid):
    money = input('请输入您要充值的金额：')
    money = int(money)
    info = handler.main(sfzid,'get')
    info['balance'] += money
    f = handler.main(sfzid, 'post')
    with open(f, 'w') as fd:
        json.dump(fd, info)
    print("{} 的账户余额为 {}".format(sfzid, info['balance']))
    return info


