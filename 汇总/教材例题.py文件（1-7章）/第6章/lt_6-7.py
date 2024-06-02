def palindrome(n):
    p = False
    string1 = str(n)
    string2 = string1[-1:-(len(string1) + 1):-1]

    if string1 == string2:
        p = True
    
    return p

def prime(n):
    p = True

    for i in range(2, int(n / 2)):
        if n % i == 0:
            p = False
            break
    
    return p

for n in range(100, 1001):
    if prime(n) == True and palindrome(n) == True:
        print(n, end = " ")