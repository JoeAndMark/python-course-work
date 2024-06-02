import math

a = eval(input('a = '))
b = eval(input('b = '))
c = eval(input('c = '))

p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("三角形面积 3S=", S)