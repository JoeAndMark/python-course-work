def canBeDividedBy3(num: int) -> bool:
    if num % 3 == 0:
        return True
    return False
def canBeDividedBy5(num: int) -> bool:
    if num % 5 == 0:
        return True
    return False
def canBeDividedBy7(num: int) -> bool:
    if num % 7 == 0:
        return True
    return False

num = int(input("请输入一个整数："))
if canBeDividedBy3(num) and canBeDividedBy5(num) and canBeDividedBy7(num):
    print("可以同时被 3、5、7 整除")
else:
    print("无法同时被 3、5、7 整除")
