def rev(N):
    result = [-1]
    List = []
    if N % 3 == 0:
        while N > 0:
            digit = N % 10
            List.append(digit)
            N = int(N / 10)
        for i in range(len(List)):
            temp = List[i]
            List[i] = List[len(List) - i - 1]
            List[len(List) - i - 1] = temp
        result = List
    return result