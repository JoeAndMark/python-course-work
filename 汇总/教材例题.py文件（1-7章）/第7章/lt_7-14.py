import csv


with open("E:\\python\\stu1.csv", 'r') as csv_file:
    writer1 = csv.reader(csv_file)
    writer1.writerow(['201904', '王强', '65', '69', '68'])
    writer1.writerow(['201905', '李莉', '76', '79', '70'])
