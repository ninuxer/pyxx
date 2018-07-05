# Author： ninuxer
# Date： 2018/04/23 10:24
# File： auth.py


from datahandler import handler


def auth(sfzid, password):
    auth_status = 0  # 0失败、1成功、2锁定、3未注册

    info = handler.main(sfzid, 'get')
    if isinstance(info,dict):
        if sfzid == info['sfzid'] and password == info['password'] and info['status'] == 0:
            print('认证成功!')
            auth_status = 1
            return auth_status
        elif sfzid == info['sfzid'] and password == info['password'] and info['status'] == 1:
            print('认证成功，但账户被锁定！！')
            auth_status = 2
            return auth_status
        else:
            print('认证失败！')
            return auth_status
    else:
        print('{} 该用户尚未注册！'.format(sfzid))
        auth_status = 3
        return auth_status

# import sys
#
# def auth_zsq(uid, p):
#     def login(fn):
#         def inner(*args, **kwargs):
#             info = handler.main(uid,'get')
#             if isinstance(info, dict):
#                 if uid == info['sfzid'] and p == info['password'] and info['status'] == 0:
#                     print('认证成功!')
#                     fn(*args, **kwargs)
#             else:
#                 print("用户不存在或密码不正确")
#
#         return inner
#
#     return login




