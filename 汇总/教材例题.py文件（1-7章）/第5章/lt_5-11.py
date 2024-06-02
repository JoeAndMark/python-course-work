x0 = 0
n = 0

while n == 0 or abs(x0 - x1) > 0.000001:
    x1 = x0
    f = x1 ** 3 - 2 * x1 ** 2 + 4 * x1 + 1
    f1 = 3 * x1 ** 2 - 4 * x1 + 4
    x0 = x1 - f / f1
    print(n, x0)
    n = n + 1

print("*" * 20)
print(x0)
print("*" * 20)