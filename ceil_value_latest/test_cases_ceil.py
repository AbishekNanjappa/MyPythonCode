import utility
def test_case1():
    assert utility.ceil_val(0) == 0
def test_case2():
    assert utility.ceil_val(1.2) == 2
def test_case3():
    assert utility.ceil_val(-2.9) == -2
def test_case4():
    assert utility.ceil_val(7) == 7