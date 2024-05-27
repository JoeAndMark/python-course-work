def palindrome(n):
    p = False
    string1 = str(n)
    string2 = string1[-1:-(len(string1) + 1):-1]

    if string1 == string2:
        p = True
    
    return p