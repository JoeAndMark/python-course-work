s = 0

for n in range(1, 10):
    x = eval(input("请输入:"))
    s = s + x

aver = s / n
print("共输入{}个数，平均值为:{:.2f}".format(n, aver))