str = input("请输入一串字符:")
s = str.upper()
x = [0] * 26

for c in s:
    if c >= "A" and c <= "Z":
        i = ord(c)
        j = i - 65
        x[j] = x[j] + 1

for j in range(0, 26):
    if x[j] > 0:
        print(chr(j + 65) + "=", x[j], " ", end = " ")