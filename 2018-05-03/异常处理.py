# Author： ninuxer
# Date： 2018/05/04 9:34
# File： 异常处理.py


try:
    inp = input('请输入：')
    inp = int(inp)

    i = [1,2,3]
    a = i[inp]
    print('{} >>> {}'.format(inp, a))
    raise Exception("我大错特错了。。。")
except ValueError as e:
    inp = 999
    print(inp)
    print(e)
except IndexError as e:
    a = 888
    print(a)
    print(e)
except Exception as e:
    print('BOSS')
    print(e)
else:
    print('没发生异常就执行else')
finally:
    print('无论是否发生异常都会执行finally')

# print('{} >>> {}'.format(inp,a))
