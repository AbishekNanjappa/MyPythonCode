def reverse(num):
    result = -1
    if len(str(num)) == 2:
        number = str(num)
        a = number[0]
        b = number[1]
        rev_num = int(b+a)
        result = rev_num
    return result