num1, num2, num3 = eval(input("请输入任意三个数字:"))

if num1 > num2:
    num1, num2 = num2, num1

if num1 > num3:
    num1, num3 = num3, num1

if num2 > num3:
    num2, num3 = num3, num2

print("三个数由小到大排序后为:{},{},{}".format(num1, num2, num3))