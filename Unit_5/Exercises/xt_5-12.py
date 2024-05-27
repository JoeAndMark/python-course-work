lst = [
    "范兴贵",
    "吴帅飞",
    "黄海燕",
    "刘亚会",
    "陆华丽",
    "郭峰伶",
    "张亚琼",
    "李先禄",
    "马四喜"
]

x = input("请输入同学姓名:")
f = False
i = 0
while i < len(lst):
    if x == lst[i]:
        f = True
        break
    else:
        i += 1
    
if f == True:
    print("找到", x, "位置为", i + 1)