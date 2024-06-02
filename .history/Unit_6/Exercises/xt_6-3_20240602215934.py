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
    