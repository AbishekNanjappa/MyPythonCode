def rev_num(N):
    List = []
    while N > 0:
        digit = N % 10
        N = int(N / 10)
        List.append(digit)
    for i in range(len(List)):
        temp = List[i]
        List[i] = List[len(List) - i - 1]
        List[len(List) - i - 1] = temp
    return List