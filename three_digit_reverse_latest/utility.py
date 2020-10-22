def three_digit_reverse(num):
    result = -1
    if 100 <= num <= 999:
        ones_digit = num % 10
        num = int(num /10)
        tens_digit = num % 10
        num = int(num/10)
        hundreds_digit = num
        result = ones_digit*100 + tens_digit*10 + hundreds_digit
    return result