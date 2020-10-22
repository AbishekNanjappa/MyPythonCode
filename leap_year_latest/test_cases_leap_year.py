import utility
def test_case_1():
    assert utility.check_leap_year(2016) == "Leap year"
def test_case_2():
    assert utility.check_leap_year(2002) == "Not a leap year"
def test_case_3():
    assert utility.check_leap_year(2000) == "Leap year"
def test_case_4():
    assert utility.check_leap_year(1998) == "Not a leap year"
def test_case_5():
    assert utility.check_leap_year(1600) == "Leap year"
def test_case_6():
    assert utility.check_leap_year(1700) == "Not a leap year"
def test_case_7():
    assert utility.check_leap_year(1900)  == "Not a leap year"