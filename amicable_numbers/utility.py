def amicable_num_check(N1,N2):
    result = "False"
    factor_N1 = 1
    factor_sum_N1 = 0
    for factor_N1 in range(1,N1,1):
        if N1 % factor_N1 == 0:
            factor_sum_N1 += factor_N1
    factor_N2 = 1
    factor_sum_N2 = 0
    for factor_N2 in range(1,N2,1):
        if N2 % factor_N2 == 0:
            factor_sum_N2 += factor_N2
    if factor_sum_N1 == N2 and factor_sum_N2 == N1:
        result = "True"
    return result