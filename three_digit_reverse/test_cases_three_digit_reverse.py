import utility
def test_cases_1():
    assert utility.three_digit_reverse(123) == 321
def test_cases_2():
    assert utility.three_digit_reverse(682) == 286
def test_cases_3():
    assert utility.three_digit_reverse(121) == 121      #check for palindrome
def test_cases_4():
    assert utility.three_digit_reverse(999) == 999      #check for number with same digits
def test_cases_5():
    assert utility.three_digit_reverse(99) == -1        #return -1 when input is not a three digit number