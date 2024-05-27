n = int(input("请输入梳理项数:"))
a = 1
b = 1
count = 1
print("{:>8}{:>8}".format(a, b), end = " ")

for i in range(3, n + 1):
    c = a + b
    print("{:^8}".format(c), end = " ")
    count += 1

    if count % 4 == 0: print()
    
    a = b
    b = c