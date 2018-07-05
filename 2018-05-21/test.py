# Author： ninuxer
# Date： 2018/05/21 16:36
# File： test.py.py


with open('new', 'r') as f1:
    d1 = f1.readlines()
    d11 = [x.strip() for x in d1]

with open('old', 'r') as f2:
    d2 = f2.readlines()
    d22 = [x.strip() for x in d2]


# print(d11)
# print(len(d11))
# print(d22)
# print(len(d22))

for i in d22:
    try:
        d11.remove(i)
    except Exception as e:
        print(e)
        print(i)

print(d11)
print(len(d11))
for j in d11:
    print(j)

# print(d11.remove('ad_appname'))
# print(d11)
# print(len(d11))