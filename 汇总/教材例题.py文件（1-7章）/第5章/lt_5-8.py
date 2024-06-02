m = eval(input("请输入要判断的整数m:"))
flag = True

for x in range(2, m):
    if m % x == 0:
        flag = False
        break

if flag == True:
    print("是质数")
else:
    print("不是质数")