# Author： ninuxer
# Date： 2018/04/23 14:36
# File： main.py


from . import auth, show_menu, card_recharge, card_regeist, card_query, card_withdraw, card_log, getout

def main():
    d = {
        '1': show_menu.show,
        '2': card_query.query,
        '3': card_recharge.recharge,
        '4': card_withdraw.withdraw,
        # '5': card_payback,
        '6': card_log.log,
        '7': getout
    }


    while True:
        sfzid = input('请输入您的身份证ID(q 退出): ')

        if sfzid in ['q', 'Q']:
            break

        password = input('请输入您的密码：')


        flag = auth.auth(sfzid, password)
        if flag == 0:
            print('您所输入的用户或密码不正确，请重新输入！')
            continue
        elif flag == 2:
            print('账户被锁定')
            break
        elif flag == 3:
            cho = input("是否要注册？(Y or N, Q for quit)")
            if cho in ['Y', 'y', 'Yes', 'YES', 'yes']:
                card_regeist.regeister(sfzid)
            elif cho in ['N', 'n', 'No', 'NO', 'no']:
                continue
        elif flag == 1:
            cho = show_menu.show()
            if cho == '1':
                show_menu.show()
            elif cho in d.keys():
                d[cho](sfzid)






