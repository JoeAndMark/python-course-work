import random

random.seed(5)
students = []
nord = ord('A')

for i in range(0, 20):
    sname = chr(nord)
    grade1 = random.randint(50, 100)
    grade2 = random.randint(50, 100)
    grade3