for x in range(0, 20 + 1):
    for y in range(0, 33 + 1):
        for z in range(0, 100 + 1):
            m = x + y + z
            n = 3 * x + 5 * y + z / 3
            
            if m == 100 and n == 100:
                print("可买公鸡:{}只, 母鸡:{}, 小鸡:{}".format(x, y, z))

print("求解结束")