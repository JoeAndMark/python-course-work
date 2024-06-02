file1 = open('E:\\python\\file1.txt', 'r')
ls = []
s = file1.readline()

while s != '':
    num = eval(s.strip('\n'))
    gw = num % 10
    hw = num // 100 % 10
    if gw % 2 == 0 and bw % 2 == 0:
        ls.append(str(num))
