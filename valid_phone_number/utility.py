def phone_no_check(N):
    result = "Invalid"
    digit_counter = 0
    digit = 0
    while N > 0:
        digit = N % 10
        N = int(N / 10)
        digit_counter += 1
    if 7 <= digit <= 9 and digit_counter == 10:
        result = "Valid"
    return result