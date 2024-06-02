def frequence(lst):
    x = [0] * 8

    for i in lst:
        k = i % 75
        x[k] = x[k] + 1
    
    print("统计结果如下:")