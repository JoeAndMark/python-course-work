a = [167, 209, 217, 225, 230, 235, 238, 256]

x = eval(input("请输入要查找的数"))
find = False
t = 0
b = len(a) - 1

while (t <= b and find == False):
    m = (t + b) // 2

    if x == a[m]:
        find = True
        print("{}已找到，位置是:{}".format(x, m + 1))
    elif x < a[m]:
        b = m - 1
    else:
        t = m + 1
    
if find == False:
    print("{}没找到".format(x))