def fact(n):
    s = 1
    
    for i in range(1, n + 1):
        s *= i
    
    return s

n1, n2, n3 = 5, 8, 13
sum = fact(n1) + fact(n2) + fact(n3)
print(sum)