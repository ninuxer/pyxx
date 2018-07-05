
product_list = [
    ("Mac",9000),
    ("Kindle",1888),
    ("Pad",2888),
    ("Iphone",8288)
]

shopcar = []

while True:
    money = input("请输入你现有余额： ")
    if money.isdigit():
        money = int(money)
        break
    elif money == "q" or money == "Q":
        exit(2)
    else:
        print("输入错误，请重新输入[q 退出]")
    continue

while True:
    for i,j in enumerate(product_list,1):
        print('{} >> {}'.format(i,j))
    choice = input("请输入你想购买的商品编号(退出：q)：")
    if choice.isdigit():
        choice = int(choice)
        if choice in range(1, len(product_list) + 1) and money >= product_list[choice - 1][1]:

            shopcar.append(product_list[choice - 1][0])
            money -= product_list[choice - 1][1]
            print("您已购买如下商品：{}".format(shopcar))
            print("您目前余额为：{}".format(money))
        else:
            print("选择的商品ID不存在或余额不足！[退出请按 q]")
    elif choice == "q" or choice == "Q":
        print("您已购买如下商品：{}".format(shopcar))
        print("您目前余额为：{}".format(money))
        break
    else:
        print("非法输入！")

