import random


sccode = random.randint(20000, 99999)
print("校验码为:{}".format(sccode))

jycode = eval(input("请输入如图所示的 5 位校验码:"))

if jycode == sccode:
    s = "不负韶华不负青春，努力拥有终生学习能力!"
else:
    s = "校验码输入错误，请重新输入。"

print(s)