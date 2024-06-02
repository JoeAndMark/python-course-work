for a in range(1, 10):
    for b in range(10):
        for c in range(1, 10):
            for d in range(10):
                if (a * 1000 + b * 100 + c * 10 + d) - (c * 100 + d * 10 + c) == (a * 100 + b * 10 + c):
                    print(a, b, c, d)
