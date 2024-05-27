resistance = [int(input("请输入一个电阻值：")) for i in range(3)] # 列表推导式


def calShuntValue(resistance: list) -> float:
    return sum(1 / r for r in resistance)


print("并联电阻值为：%f" % calShuntValue(resistance))
