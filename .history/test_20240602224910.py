f1 = open("E:\\python\\text.txt", "r", encoding = 'utf-8')
strTest = f1.read()
print(strTest)


f1 = open("E:\\python\\text.txt", "r", encoding = 'utf-8')
s = f1.readline()
strTest = ''
while s != '':
    strTest += s
    s = f1.readline()

print(strTest)


f1 = open("E:\\python\\test")