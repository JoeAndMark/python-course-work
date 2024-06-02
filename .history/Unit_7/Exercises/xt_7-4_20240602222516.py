f3 = open('E:\\python\\file3.txt', 'r', encoding='utf-8')
f4 = open('E:\\python\\file4.txt', 'w', encoding='utf-8')

s = f3.read()

while s != '':
    n = ord(s) * 11 % 256
    if n > 32 and n < 130:
        s1 = chr(ord(s) * 11 % 256)
        f4.write(s1)
    else:
        f4.write(s)
    
    s = f3.read()
    

