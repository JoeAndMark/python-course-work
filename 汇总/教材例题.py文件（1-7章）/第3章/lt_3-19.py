import random


num = random.randint(10, 100)
n = 1


while n <= 10:
    cai_num = int(input("请输入你猜的整数:"))
    if cai_num > num:
        print("大了点!")
    elif cai_num < num:
        print("小了点")
    elif cai_num == num:
        print("恭喜您第{}次就猜中了!".format(n))
        break
    n += 1


if n > 10:
    print("很遗憾，您没有猜中，这个数是:", num)