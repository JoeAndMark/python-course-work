n = 0
for m in range(1000, 1100):
    flag = True
    for i in range(2, m):
        if m % i == 0:
            flag = False
            break

    if flag == True:
        n += 1
        print(m, end=" ")
        if n % 6 == 0:
            print("\n")
