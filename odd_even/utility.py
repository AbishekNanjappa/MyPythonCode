def odd_even(n1,n2):
    result = -1
    remainder_1 = n1 % 2
    remainder_2 = n2 % 2 
    if remainder_1 == 0 and remainder_2 == 0:
        result =  n1 - n2
    elif remainder_1 != 0 and remainder_2 != 0:
        result = n1 + n2
    return result