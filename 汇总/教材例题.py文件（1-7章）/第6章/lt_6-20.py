def tel_menu(menu_str):
    print()
    print(menu_str)
    menu_index = eval(input("请选择操作功能:0-5"))
    
    if menu_index < 0 or menu_index > 6:
        menu_index = 1
    
    return menu_index