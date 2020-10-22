def largest_digit(num):
    largest_digit = -1          
    if 100 <= num <= 999:          
       while num > 0:
            digit = num % 10
            if digit > largest_digit:
               largest_digit = digit
            num = int(num/10)
    return largest_digit
