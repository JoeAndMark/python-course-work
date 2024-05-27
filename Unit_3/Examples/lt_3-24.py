m = 1
kx_num = 538
print("1月份的开行量为538列")

while m <= 9:
    kx_num = kx_num * (1 + 0.1)
    m += 1
    print("{}月份的开行量为{}列".format(m, kx_num))