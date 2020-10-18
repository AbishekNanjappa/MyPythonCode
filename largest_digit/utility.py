def largest_digit(num):
    if len(str(num)) == 3:
        largest_digit = num % 10
        digit = 0
        while num > 0:
            num = int(num / 10)
            digit = num % 10
            if digit > largest_digit:
                largest_digit = digit
    else:
        largest_digit = -1
    
    return largest_digit
