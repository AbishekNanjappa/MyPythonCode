def split_num(N):
    digit = 0
    List = []
    while N > 0:
        digit = N % 10
        N = int(N/10)
        List.append(digit)
        List.append("#")
    rev_List = List[::-1]
    return_val = rev_List[1:]
    return return_val