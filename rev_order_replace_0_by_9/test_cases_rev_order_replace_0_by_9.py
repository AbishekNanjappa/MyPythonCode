import utility
def test_case_1():
    assert utility.rev_order(123) == [3,2,1]
def test_case_2():
    assert utility.rev_order(397) == [7,0,3]
def test_case_3():
    assert utility.rev_order(965) == [5,6,0] 
def test_case_4():
    assert utility.rev_order(859) == [0,5,8]
def test_case_5():
    assert utility.rev_order(98) == [8,0]
def test_case_6():
    assert utility.rev_order(79) == [0,7]
def test_case_7():
    assert utility.rev_order(7) == [7]
def test_case_8():
    assert utility.rev_order(9) == [0]