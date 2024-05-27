fl = open("E:\\python\\tx.txt", "w")
a = [
    "唐诗\n",
    "宋词\n",
    "元曲\n"
]

fl.writelines(a)
fl.close()