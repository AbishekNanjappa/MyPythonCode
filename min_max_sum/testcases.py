import utility
def test_case_1():
    assert utility.min_max_sum(1,2,3,4) == 5
def test_case_2():
    assert utility.min_max_sum(-1,-2,-3,-4) == -5
def test_case_3():
    assert utility.min_max_sum(0,100,99,98) == 100
def test_case_4():
    assert utility.min_max_sum(-90,100,0,90) == 10