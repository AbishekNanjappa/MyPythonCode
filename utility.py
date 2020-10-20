def search(A,N,S):
    result = "False"
    for i in range(N):
        if A[i] == S:
            result = "True"
            break
    return result
        