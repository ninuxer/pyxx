# Author： ninuxer
# Date： 2018/04/17 16:06
# File： 生成器.py

# example 1


def bar():
    print("step1...")
    sendtest1 = yield "aaa"
    print("send1 is : {}".format(sendtest1))
    print("step2...")
    sendtest2 = yield "bbb"
    print("send2 is : {}".format(sendtest2))
    print("step3...")
    yield "ccc"
    print("step4...")

#### next的用法
# g=bar()
# s1 = next(g)
# print("AAAAAA {}".format(s1))
# s2 = next(g)
# print("AAAAAAAAAA {}".format(s2))
# s3 = next(g)


# send的用法
h = bar()
s1 = h.send(None)
print("AAAAAA {}".format(s1))
s2 = h.send("mw")
print("AAAAAA {}".format(s2))
s3 = h.send('nwc')
print(s3)


