def rev_order(N):
    List = []
    while N > 0:
        digit = N % 10
        if digit == 9:
            List.append(0)
        else:
            List.append(digit)
        N = int(N / 10)
    for i in range(len(List)):
        temp = List[i]
        List[i] = List[len(List) - i -1]
        List[len(List) - i - 1] = temp
    return List