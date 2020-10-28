def sum_of_digits(N):
    sum_of_digits = 0
    digit = 0
    if N < 0:
        sum_of_digits = -1
    else:
        while N > 0:
            digit = N % 10
            sum_of_digits += digit
            N = int(N / 10)
    return sum_of_digits