import math


a, b, c = eval(input("请输入 a, b, c 的值:"))
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("三角形面积 s =", s)