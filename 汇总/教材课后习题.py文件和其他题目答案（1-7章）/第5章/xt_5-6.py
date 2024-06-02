# 设男友为 m，女人为 f，小孩为 c
for m in range(1, 17):
    for f in range(1, 25):
        c = 30 - m - f
        s = 3 * m + 2 * f + c
        if s == 50:
            print("男人有{}人，女人有{}人，小孩有{}人".format(m, f, c))