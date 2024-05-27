a = [
    89, 
    84,
    102,
    107,
    106,
    104,
    97,
    99
]
n = len(a)
print("排序前:", a)

for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print("排序后:", a)
