import csv


with open("E:\\python\\stu1.csv", 'r') as csv_file:
    reader1 = csv.reader(csv_file)
    for row in reader1:
        print(row)