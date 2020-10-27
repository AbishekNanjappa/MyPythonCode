def first_N_num_2(N):
    List = []
    while N > 0:
        List.append(N)
        N -= 1
        if N >= 1:
            List.append("#")
    return List