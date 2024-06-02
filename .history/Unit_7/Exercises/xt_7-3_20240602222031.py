file1 = open('E:\\python\\file1.txt', 'r')
ls = []
s = file1.readline()

while s != '':
    num = eval(s.strip('\n'))
    gw = num % 10
    
