# 追加写程序
f1 = open("E:\\python\\t2.txt", "a")
b = [
    "10",
    "20",
    "30"
]

# 覆盖写程序
f1.writelines(b)
f1.close()

f1 = open("E:\\python\\t2.txt", "w")
b = [
    "10",
    "20",
    "30"
]

f1.writelines(b)
f1.close()
