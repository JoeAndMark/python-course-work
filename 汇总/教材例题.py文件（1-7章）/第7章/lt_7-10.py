file2 = open("E:\\python\\testfile1.txt", 'r')
s = file2.readline()

while s != '':
    print(s, end = '')
    s = file2.readline()
    file2.close()