import random


file1 = open("E:\\python\\num.txt", 'w')

for i in range(1, 201):
    x = random.randint(0, 100)
    s = str(x) + '\n'
    file1.write(s)

file1.close()