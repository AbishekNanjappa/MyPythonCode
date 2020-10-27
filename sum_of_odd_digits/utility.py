def odd_digit_sum(N):
    sum_odd = 0
    while N > 0:
        digit = N % 10
        N = int(N / 10)
        if digit % 2 == 0:
            continue
        else:
            sum_odd += digit
       
    return sum_odd
        
