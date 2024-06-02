def tel_find(tel_number):
    name = input("联系人姓名:")

    if name == "":
        return
    
    tel_find = []

    for tel in tel_number:
        if name == tel[0]:
            tel_find.append(tel)
    
    if len(tel_find) == 0:
        print("查无此人")
    
    return tel_find