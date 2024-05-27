def money(p, n, r = 0.04):
    m = 0

    for i in range(1, n + 1):
        m = p * r
        p = p * (1 + r)

    return m, p

print(money(n = 10, p = 10000))