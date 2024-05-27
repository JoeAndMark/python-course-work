e = 0
n = 0
f = 1
x = 1

while x >= 10 ** (-4):
    e += x
    n += 1
    f *= n
    x = 1 / f

print("e 的近似值为:{:.6f}".format(e))