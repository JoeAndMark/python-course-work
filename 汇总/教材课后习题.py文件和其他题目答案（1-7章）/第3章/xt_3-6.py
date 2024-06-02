def is_narcissistic_number(num: int) -> bool:
    # 如果不是三位数，不满足水仙花数的定义
    if num < 100 or num >= 1000:
        return False
    digits = [None] * 3
    tmp = num
    for i in range(3):
        digits[i] = (tmp % 10) ** 3
        tmp //= 10
    return sum(digits) == num

for i in range(100, 1000):
    if is_narcissistic_number(i):
        print(i)
