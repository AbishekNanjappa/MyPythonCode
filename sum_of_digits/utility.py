def sum_of_digits(num):
    sum = 0
    if len(str(num)) == 3:
        while num > 0:
            digit = num % 10
            sum += digit
            num = int(num / 10)
    else:
        sum = -1
    return sum
