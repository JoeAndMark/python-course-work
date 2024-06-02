import csv


header = [
    '学号',
    '姓名',
    '高数',
    '英语',
    '计算机'
]

ls = [
    ['201901', '张明', 83, 80, 89],
    ['201902', '李亮', 90, 94, 97],
    ['201903', '赵青', 75, 70, 83]
]

with open("E:\\python\\stu1.csv", 'w', newline = '') as csv_file:
    writer1 = csv.writer(csv_file)
    writer1.writerow(header)
    writer1.writerows(ls)