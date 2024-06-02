def insert(string, c):
    l = list(string)
    inserted = False

    for char in l:
        if (not inserted) and char >= c:
            print("%s" % (c), end = '')
            inserted =True
        print("%s" % (char), end = '')
    
    if not inserted:
        print("%s" % (c), end = '')


string = input