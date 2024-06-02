def tel_view(tel_number):
    print("{:<10}{:<15}{:<20}".format("姓名", "电话号码", "备注"))

    for tel in tel_number:
        print("{:<10}{:<15}{:<20}".format(tel[0], tel[1], tel[2]))