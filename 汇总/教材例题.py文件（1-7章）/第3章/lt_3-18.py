sum = 0
for num in range(1, 101):
    if num % 2 != 0:
        sum += num
    else:
        sum -= num

print("1-2+3-4+···+100=", sum)