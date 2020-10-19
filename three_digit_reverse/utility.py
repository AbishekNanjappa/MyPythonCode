def three_digit_reverse(num):
    result = -1
    if len(str(num)) == 3:
        number = str(num)       #input in the form of a string
        a = number[0]
        b = number[1]
        c = number[2]
        rev_num = int(c+b+a)
        result = rev_num
    return result