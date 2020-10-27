import utility
def test_case_1():
    assert utility.check_for_prime(2) == "Prime"
def test_case_2():
    assert utility.check_for_prime(4) == "Composite"
def test_case_3():
    assert utility.check_for_prime(5) == "Prime"
def test_case_4():
    assert utility.check_for_prime(9) == "Composite"
def test_case_5():
    assert utility.check_for_prime(0) == "Neither prime nor composite"
