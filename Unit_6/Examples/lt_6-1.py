sum = 0
s = 1

for i in range(1, 6):
    s *= i

sum = sum + s
s = 1

for i in range(1, 9):
    s *= i

sum = sum + s
s = 1

for i in range(1, 14):
    s *= i

sum = sum + s
print("5! + 8! + 14! =", sum)