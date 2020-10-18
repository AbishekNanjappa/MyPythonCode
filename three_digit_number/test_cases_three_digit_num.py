import utility
def test_case_1():
    assert utility.check(100) == "True"
def test_case_2():
    assert utility.check(99) == "False"
def test_case_3():
    assert utility.check(1001) == "False"
def test_case_4():
    assert utility.check(999) == "True"