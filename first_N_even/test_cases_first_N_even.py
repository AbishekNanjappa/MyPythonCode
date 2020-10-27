import utility
def test_case_1():
    assert utility.first_N_even(5) == [0,2,4,6,8]
def test_case_2():
    assert utility.first_N_even(1) == [0]
def test_case_3():
    assert utility.first_N_even(10) == [0,2,4,6,8,10,12,14,16,18]
def test_case_4():
    assert utility.first_N_even(3) == [0,2,4]