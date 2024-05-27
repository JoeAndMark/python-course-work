def tel_edit(tel_number):
    tel = tel_find(tel_numer)
    
    if len(tel > 0):
        for t in tel:
            num = tel_number.index(t)
            name = input("姓名:")
            phone = input("电话号码:")
            remarks = input("备注:")
            t = [name, phone, remarks]

            tel_number[num] = t
    
    return tel_number
