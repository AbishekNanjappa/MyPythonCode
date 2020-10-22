def reverse(num):
    result = -1
    if 10 <= num <=99 :          
        ones_digit = num % 10
        tens_digit = int(num / 10) 
        result = ones_digit*10 + tens_digit
    return result