import math

a, b, c = 3, 4, 5
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("三角形面积S=", S)