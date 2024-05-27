def tel_delete(tel_number):
    if len(tel_number) == 0:
        return
    
    tel = tel_find(tel_number)

    if len(tel) > 0:
        for t in tel:
            num = tel_number.index(t)
            print(t)
            yn = input("是否输出（Y-删除，N-不删除）")

            if yn == "Y" or yn == "y":
                del(tel_number[num])

        return tel_number