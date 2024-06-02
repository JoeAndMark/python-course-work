import math


a, b = 0, 1
n = 100
h = (b - a) / n
x = a
s = 0

for i in range(n):
    si = math.sin(x) * h
    s = s + si
    x = x + h

print("用矩形法求得的定积分为:", s)