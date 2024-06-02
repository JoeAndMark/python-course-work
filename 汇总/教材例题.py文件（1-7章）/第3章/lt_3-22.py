gs = 0

for num in range(100, 201):
    if num % 3 == 0:
        gs += 1
        print(num, end = " ")
        if gs % 8 == 0:
            print()