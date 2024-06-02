import csv


data = [
    ['姓名', '手机', 'QQ', '微信号'],
    ['张三', '13125000001', 'zs001', '75177001'],
    ['李四', '13125000002', '13125000002', '75177002'],
    ['王五', '13125000003', 'w555', '75177003'],
    ['赵六', '13125000004', 'Liu666', '75177004'],
    ['刘七', '13125000005', '13125000005', '75177005']
]

with open('通讯录.csv', 'r', newline = '') as file1:
    writer1 = csv.writer(file1)
    writer1.writerows(data)


with open('通讯录.csv', 'r', newline = '') as file1:
    reader1 = csv.reader(file1)
    for row in reader1:
        if row[0] == '赵六':
            print(row[1], row[2], row[3])
            break
