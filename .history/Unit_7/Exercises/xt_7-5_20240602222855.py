import random

random.seed(5)
students = []
nord = ord('A')

for i in range(0, 20):
    sname = chr(nord)
    grade1 = random.randint(50, 100)
    grade2 = random.randint(50, 100)
    grade3 = random.randint(50, 100)
    grade4 = random.randint(50, 100)
    grade5 = random.randint(50, 100)

    student = [
        sname,
        grade1,
        grade2,
        grade3,
        grade4,
        grade5
    ]

    students.append(student)
    nord = ord
