n = 0
for i in range(100, 999 + 1):
    a = i // 100
    c = i % 10
    if a == c:
        n += 1
        print(i, end=" ")
        if n % 10 == 0:
            print("\n")
print("100~999 之间的水仙花数共有{}".format(n))