file1 = open('E:\\python\\file1.txt', 'r')
ls = []
s = file1.readline()

while s != '':
    num = eval(s.strip('\n'))
    gw = num % 10
    bw = num // 100 % 10
    if gw % 2 == 0 and bw % 2 == 0:
        ls.append(str(num))
    s = file1.readline()

print(ls)

import csv


with open('E:\\python\\file2.csv', 'w', newline='') as f:
    w1 = csv.writer(f)
    for i in ls:
        writer.writerow([i])

