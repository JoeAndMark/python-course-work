a = eval(input("请输入 a 值:"))
x0 = a / 2
x1 = (x0 + a / x0) / 2

while abs(x0 - x1) > 10 ** (-6):
    x0 = x1
    x1 = (x0 + a / x0) / 2

print("a 的平方根为:", x1)