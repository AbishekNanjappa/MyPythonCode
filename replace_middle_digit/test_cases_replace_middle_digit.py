import utility
def test_cases_1():
    assert utility.replace(123) == 113
def test_cases_2():
    assert utility.replace(566) == 556
def test_cases_3():
    assert utility.replace(565) == 555
def test_cases_4():
    assert utility.replace(111) == 111
def test_cases_5():
    assert utility.replace(98) == -1        #returns -1 when input is not a three digit number