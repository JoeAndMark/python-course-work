def money(p, n, r):
    m = 0

    for i in range(1, n + 1):
        m = p * r
        p = p * (1 + r)
    
    return m, p

a, b, c = 10000, 10, 0.04
print(money(a, b, c))
