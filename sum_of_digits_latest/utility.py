def sum_of_digits(num):
    sum = -1
    if 100 <= num <= 999:          
        ones_digit = num % 10
        num = int(num / 10)
        tens_digit = num % 10
        num = int(num / 10)
        hundreds_digit = num
        sum = hundreds_digit + tens_digit + ones_digit
    return sum
