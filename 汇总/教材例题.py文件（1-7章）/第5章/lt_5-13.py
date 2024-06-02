a = [
    89, 
    84,
    102,
    107,
    106,
    104,
    97,
    99
]

x = eval(input("请输入要查找的数:"))
p = False
n = 0

for i in a:
    n = n + 1
    if x == i:
        p = True
        break

if p == True:
    print("找到了，在第{}位。".format(n))
else:
    print("没找到!")