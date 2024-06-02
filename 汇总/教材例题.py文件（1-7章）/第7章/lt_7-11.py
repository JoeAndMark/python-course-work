file1 = open("E:\\python\\student1.txt", 'w')

for i in range(1, 31):
    xh = input("请输入学号:")
    xm = input("请输入姓名:")
    gs = input("请输入高数成绩:")
    yy = input("请输入英语成绩:")
    jsj = input("请输入计算机成绩:")
    s = xh + "," + xm + "," + gs + "," + yy + "," + jsj + "\n"
    file1.write(s)

file1.close()

file1 = open("E:\\python\\student1.txt", 'r')
file2 = open("E:\\python\\student2.txt", 'w')

s = file1.readline()

while s != '':
    s = s.strip("\n")
    lst = s.split(",")
    aver = (eval(lst[2]) + eval(lst[3]) + eval(lst[4])) / 3
    if aver >= 80:
        file2.write(s)
        s = file1.readline()

file2.close()
file1.close()
