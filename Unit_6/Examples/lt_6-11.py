def sum(*s):
    sum_s = 0

    for i in s:
        sum_s = sum_s + i
    
    return sum_s

print(sum(1, 2, 3, 4))