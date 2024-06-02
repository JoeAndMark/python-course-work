a = 2
b = 1
s = 0

for i in range(20):
    s += a / b
    b, a = a, a + b

print("数列前 20 项之和为:", s)