tel_list = []
tel_default = [
    "机主",
    "12345678900",
    "本机号码"
]

tel_list.append(tel_default)
menu = "1——显示，2——查询，3——添加，4——修改，5——删除，0——退出"

while True:
    num = tel_menu(menu)

    if num == 0:
        print("退出程序")
        break
    elif num == 1:
        tel_view(tel_list)
    elif num == 2:
        info = tel_find(tel_list)
        tel_view(info)
    elif num == 3:
        info = tel_append()
        tel_list.append(info)
    elif num == 4:
        info = tel_edit(tel_list)
        tel_view(info)
    elif num == 5:
        info = tel_delete(tel_list)
        tel_view(info)
