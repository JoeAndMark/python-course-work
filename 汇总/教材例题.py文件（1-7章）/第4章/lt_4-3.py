tot = 0
n = 0

while True:
    sco = eval(input("请输入学生成绩（）输入-1结束:"))
    if sco == -1 and n == 0:
        print("班级内共有0个学生")
        break
    elif sco == -1:
        print("学生平均成绩为{:.2f}.format(tot / n)")
        break
    else:
        tot += sco 
        n += 1
    