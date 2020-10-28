import utility
def test_case_1():
    assert utility.sum_of_digits(95) == 14
def test_case_2():
    assert utility.sum_of_digits(1) == 1
def test_case_3():
    assert utility.sum_of_digits(0) == 0
def test_case_4():
    assert utility.sum_of_digits(999) == 27
def test_case_5():
    assert utility.sum_of_digits(100) == 1
def test_case_6():
    assert utility.sum_of_digits(-199) == -1        #return -1 when input is negative  