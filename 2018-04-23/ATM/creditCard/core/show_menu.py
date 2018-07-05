# Author： ninuxer
# Date： 2018/04/25 17:22
# File： show_menu.py


import sys


def show():
    showinfo = '''
    1: 查看菜单
    2: 查询信息
    3: 充值
    4: 提现
    5: 还款
    6: 账单查询
    7: 退出
    '''
    # d = {
    #     '1': card_query,
    #     '2': card_recharge,
    #     '3': card_withdraw,
    #     '4': card_payback,
    #     '5': card_log
    # }
    while True:
        print(showinfo)
        cho = input("请输入您要执行的操作：")
        if cho in [str(i) for i in range(1, 8)]:
            return cho
        else:
            print('您所输入的业务不存在，请重新输入！')
            continue

if __name__ == '__main__':
    show()

