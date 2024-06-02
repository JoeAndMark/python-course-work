def comb(a, b):
    l = list()
    l.append(a[1])
    l.append(b[1])
    l.append(a[0])
    l.append(b[0])
    s = int(''.join(l))
    return s

a, b = map(list, input().split())
print(comb(a, b))