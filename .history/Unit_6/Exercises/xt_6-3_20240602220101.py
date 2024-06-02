def is_prime(num):
    """
    判断一个数是否为质数
    """
    p = True

    for i in range(2, num):
        if num % i == 0:
            p = False
            break

    return p


def twin_prime(num):
    primes = []

    for i in range(2, num + 1):
        if is_prime(i):
            primes.append(i)
        
    # 判断是否为孪生素数
    index = 1
    while index < len(primes):
        if primes[index] - primes[index - 1] == 2:
            print()