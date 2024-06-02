# 递归
def calFactorial(n: int) -> int:
    if n == 1:
        return 1
    return n * calFactorial(n - 1)

def calE() -> float:
    e = 1
    index = 1
    while True:
        tmp = 1 / calFactorial(index)
        e += tmp
        index += 1
        if tmp < 1e-4:
            break
    return e
