def my_gcd(m, n):
    if n == 0:
        g = m
    else:
        g = my_gcd(n, m % n)
    
    return g

m = int(input())