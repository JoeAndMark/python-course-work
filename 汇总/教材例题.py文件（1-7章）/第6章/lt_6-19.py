def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

for i in range(1, 20 + 1):
    print("{:>6}".format(fibo(i)), end = " ")
    if i % 5 == 0: print()