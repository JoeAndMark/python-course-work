def sumEveryCarry(integer: int) -> int:
    everyCarry = []
    for i in range(0, 3):
        everyCarry.append(integer % 10)
        integer //= 10
    total = sum(everyCarry)
    return total

integer = int(input("请输入一个三位数的整数：\n"))
print(sumEveryCarry(integer))
