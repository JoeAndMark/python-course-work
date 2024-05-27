gs = 0

for num in range(1000, 10000):
    qws = num // 1000
    bws = num // 100 % 10
    sws = num // 10 % 10
    gws = num % 10

    if qws == gws and bws == sws:
        print(num, end=",")
        gs += 1
        if gs % 10 == 0:
            print()