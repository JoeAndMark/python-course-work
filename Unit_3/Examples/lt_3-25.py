dz_num = 0
hd_paper = 0.0001

while hd_paper <= 8844.43:
    hd_paper = 2 * hd_paper
    dz_num += 1

print("当对折{}次之后，纸的厚度为{}m".format(dz_num, hd_paper))