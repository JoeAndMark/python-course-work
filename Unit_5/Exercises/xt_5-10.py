# 用列表 cj 存放数据，gs 表示数据个数（即列表长度）

n = int(input("请输入班级人数:"))
cj = []

for i in range(n):
    x = eval(input("请输入成绩:"))
    cj.append(x)

print("排序之前的数据为:", cj)

gs = len(cj)

for i in range(gs - 1):
    k = i
    for j in range(i + 1, gs):
        if cj[k] > cj[j]:
            k = j
    cj[i], cj[k] = cj[k], cj[i]

print("排序之后的数据为:", cj)