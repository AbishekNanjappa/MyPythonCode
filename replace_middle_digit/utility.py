def replace(num):
    result = -1
    if len(str(num)) == 3:
        number = str(num)
        a = number[0]
        c = number[2]
        new_num = int(a+a+c)
        result = new_num
    return result