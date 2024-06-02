f1 = open("E: \\python\\test.txt", "r", encoding = 'utf-8')
a = f1.readline()
n = 0
while a != "":
    n += 1
    s = f1.read