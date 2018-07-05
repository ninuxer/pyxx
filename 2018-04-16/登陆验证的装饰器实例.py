# Author： ninuxer
# Date： 2018/04/16 11:53
# File： 登陆验证的装饰器实例.py

user = ["nwc", "mw", "test"]
passwd = ["123456", "111111", "112233"]


# lguser="nwc"
# lgpass="123456"

def lgzsq(u, p):
    def login(fn):
        def inner(*args, **kwargs):
            if user.index(u) + 1 > 0 and p == passwd[user.index(u)]:
                print("登陆成功")
                fn(*args, **kwargs)
            else:
                print("用户不存在或密码不正确")

        return inner

    return login


@lgzsq("mw", "111111")
def foo(path):
    print("This is the {}".format(path))


foo("/adjht/index.html")
