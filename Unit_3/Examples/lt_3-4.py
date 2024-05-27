score = eval(input("请输入您的成绩:"))

if score >= 90:
    print("优秀")
elif 80 <= score < 90:
    print("良好")
elif 60 <= score < 80:
    print("及格")
elif 0 < score < 60:
    print("不及格")
elif score == 0:
    print("缺考")