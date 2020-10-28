def greatest_num(n):
    greatest_number = n[0]
    for i in range(2):
        if n[i] > greatest_number:
            greatest_number = n[i]
    return greatest_number