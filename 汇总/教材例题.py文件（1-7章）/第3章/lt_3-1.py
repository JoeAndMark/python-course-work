import math

a = 3
b = 4
c = 5

p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("三角形面积S=", S)