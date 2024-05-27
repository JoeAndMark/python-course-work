num = eval(input("请输入一个非0整数:"))
sum = 0

while num != 0:
    sum += num
    num = eval(input("请再次输入一个非0整数:"))

print("sum = ", sum)