def prime(n):
    p = True

    for i in range(2, int(n / 2)):
        if n % i == 0:
            p = False
            break
    
    return p