import math


a, b = 0, 1 # 设置区间
n = 100 # 设置区间等分数
h = (b - a) / n # 计算宽度为 h
x = a # 设置第 1 区间等分坐标
s = 0

for i in range(n):
    si = math.exp(- x ** 2) * h
    s += si
    x += h

print("用矩形求得的定积分为:", s)
