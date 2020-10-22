import utility
def test_case_1():
    assert utility.sum_of_digits(100) == 1
def test_case_2():
    assert utility.sum_of_digits(399) == 21
def test_case_3():
    assert utility.sum_of_digits(999) == 27
def test_case_4():
    assert utility.sum_of_digits(111) == 3
def test_case_5():
    assert utility.sum_of_digits(1000) == -1        #return -1 if number is not a three digit number