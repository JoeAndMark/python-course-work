list = [
    ["001", 12.4],
    ["009", 10.4],
    ["095", 11.1],
    ["021", 14.4],
    ["061", 15.1],
    ["070", 12.1],
    ["006", 15.4],
    ["008", 12.4],
    ["004", 11.4]
]

print("排序之前的数据为:", list)

n = len(list)

for i in range(n - 1):
    k = i
    for j in range(i + 1, n):
        if list[k][1] < list[j][1]:
            k = j
    list[i], list[k] = list[k], list[i]
    
print("按成绩由高到低排序之后的数据为:", list)