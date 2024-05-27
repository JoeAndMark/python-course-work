def calPiecewiseFunctionValue(x) :
    if x < 0:
        return 0
    elif 0 <= x < 5:
        return x + 1
    elif 5 <= x < 8:
        return 3 * x + 1
    elif 8 <= x < 20:
        return x ** 2 + 2
    else :
        return 0

print(calPiecewiseFunctionValue(int(input("请输入 x 的值："))))