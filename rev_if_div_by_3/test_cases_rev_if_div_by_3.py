import utility
def test_case_1():
    assert utility.rev(333) == [3,3,3]
def test_case_2():
    assert utility.rev(27) == [7,2]
def test_case_3():
    assert utility.rev(108) == [8,0,1]
def test_case_4():
    assert utility.rev(57) == [7,5]
def test_case_5():
    assert utility.rev(92) == [-1]
def test_case_6():
    assert utility.rev(76) == [-1]