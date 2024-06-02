def calSum(num: int) ->float:
    pi = 0
    while num > 0:
        pi += 1 / num
        num -= 1
    return pi

print(calSum(20))