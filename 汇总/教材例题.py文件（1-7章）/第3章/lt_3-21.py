jsh = 0
osh = 0
num = 1

while num <= 100:
    if num % 2 == 1:
        osh += num
    else:
        jsh += num
    num += 1

print("1-100中所有的奇数和为:", jsh)
print("1-100中所有偶数和为:", osh)