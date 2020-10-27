def first_N_even(N):
    num = 0
    counter = 0
    List = []
    while True:
        List.append(num)
        num += 2
        counter += 1
        if counter == N:
            break
    return List