def check_for_prime(N):
    result = "Prime"
    if N == 0:
        result = "Neither prime nor composite"
    else:
        for factor in range(1,N,1):
            if factor == 1 or factor == N:
                continue
            else:
                if N % factor == 0:
                    result = "Composite"
                    break
                else:
                    continue
    return result