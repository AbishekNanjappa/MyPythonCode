import utility
def test_case_1():
    assert utility.rev_num(123) == [3,2,1]
def test_case_2():
    assert utility.rev_num(9857) == [7,5,8,9]
def test_case_3():
    assert utility.rev_num(98) == [8,9]
def test_case_4():
    assert utility.rev_num(7) == [7]
def test_case_5():
    assert utility.rev_num(121) == [1,2,1] 