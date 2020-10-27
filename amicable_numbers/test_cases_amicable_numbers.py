import utility
def test_case_1():
    assert utility.amicable_num_check(220,284) == "True"
def test_case_2():
    assert utility.amicable_num_check(1184,1210) == "True"
def test_case_3():
    assert utility.amicable_num_check(2620,2924) == "True"
def test_case_4():
    assert utility.amicable_num_check(5020,5564) == "True"
def test_case_5():
    assert utility.amicable_num_check(300,320) == "False"
def test_case_6():
    assert utility.amicable_num_check(450,496) == "False"
def test_case_7():
    assert utility.amicable_num_check(566,589) == "False"
def test_case_8():
    assert utility.amicable_num_check(890,891) == "False"