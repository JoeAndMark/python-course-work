username = input("请输入您的用户名:")
passwd = input("请输入您的密码:")

if username == 'admin':
    if passwd == '123456':
        print("请稍后，正在登录")
    else :
        print("密码输入有误")
else:
    print("用户名输入有误")