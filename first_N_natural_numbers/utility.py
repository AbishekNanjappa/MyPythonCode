def first_N_numbers(N):
    num = 1
    List = []
    while num <= N:
        List.append(num)
        num += 1
        if num <= N:
            List.append("#")
        else:
            continue
    return List