def MyGcd(m, n):
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    
    return n

print(MyGcd(MyGcd(1260, 198), 72))