import random
import csv


with open('E:\\python\\student.csv', 'w', newline = '') as f1:
    w1 = csv.writer(f1)
    w1.writerow(['学号', '姓名', '高数', '英语', '计算机'])

    for i in range(1, 6):
        xh = input('请输入学号:')
        xm = input('请输入姓名:')
        gs = random.randint(0, 100)
        yy = random.randint(0, 100)
        jsj = random.randint(0, 100)
        rowdata = [xh, xm, gs, yy, jsj]
        w1.writerow(rowdata)


newdata = []
n = 0

with open('E:\\python\\student.csv', 'r') as f1:
    r1 = csv.reader(f1)
    for data in r1:
        n = n + 1
        if n > 1:
            aver = (eval(data[2]) + eval(data[3]) + eval(data[4])) / 3
            if aver >= 80:
                newdata.append(data)

print(newdata)

with open('E:\\python\\student2.csv', 'w', newline='') as f2:
    w1 = csv.writer(f2)
    w1.writerows(newdata)
