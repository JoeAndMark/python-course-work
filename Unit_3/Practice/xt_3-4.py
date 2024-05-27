def isLeapYear(year: int) -> bool:
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return True
    else:
        return False

year = int(input("请输入年份："))
if isLeapYear(year):
    print("%d 是闰年" % year)
else:
    print("%d 不是闰年" % year)