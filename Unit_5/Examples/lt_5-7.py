m = int(input("请输入第1个数m:"))
n = int(input("请输入第2个数n:"))

if m < n:
    m, n = n, m

for x in range(m, m * n + 1):
    if x % m == 0 and x % n == 0:
        print("最小公倍数为:", x)
        break

for y in range(n, 0, -1):
    if m % y == 0 and n % y == 0:
        print("最大公约数为:", y)
        break