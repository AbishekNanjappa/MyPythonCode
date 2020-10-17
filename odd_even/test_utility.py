import utility

def test_case1_both_odd():
    assert utility.odd_even(1,3) == 4
def test_case2_both_even1():
    assert utility.odd_even(2,4) == -2
def test_case3_both_even2():
    assert utility.odd_even(6,4) == 2
def test_case4_odd_and_even():
    assert utility.odd_even(5,6) == -1
def test_case5_both_even3():
    assert utility.odd_even(0,2) == -2