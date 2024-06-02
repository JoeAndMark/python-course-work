import csv


with open("E:\\python\\stu1.csv", 'w', newline = '') as csv_file:
    writer1 = csv.writer(csv_file)
    writer1.writerow(["学号", "姓名", "高数", "英语", "计算机"])
    writer1.writerow(['201901', '张明', 83, 80, 89])
    writer1.writerow(['201902', '李亮', 90, 94, 97])
    writer1.writerow(['201903', '赵青', 75, 70, 83])