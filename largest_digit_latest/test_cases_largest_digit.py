import utility
def test_case_1():
    assert utility.largest_digit(190) == 9
def test_case_2():
    assert utility.largest_digit(200) == 2
def test_case_3():
    assert utility.largest_digit(999) == 9
def test_case_4():
    assert utility.largest_digit(0) == -1
def test_case_5():
    assert utility.largest_digit(99999) == -1
def test_case_6():
    assert utility.largest_digit(10) == -1
def test_case_7():
    assert utility.largest_digit(111) == 1