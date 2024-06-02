def fact(n):
    s = 1

    for i in range(1, n + 1):
        s *= i
    
    global m
    m = 8
    print(m)

    return s

m = 5
print(fact(m), m)