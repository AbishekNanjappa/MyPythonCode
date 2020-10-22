def replace(num):
    result = -1
    if 100 <= num <= 999:
        ones_digit = num % 10
        num = int(num/10)
        tens_digit = num % 10
        num = int(num/10)
        hundreds_digit = num
        result = tens_digit*100 + hundreds_digit*10 + ones_digit 
    return result