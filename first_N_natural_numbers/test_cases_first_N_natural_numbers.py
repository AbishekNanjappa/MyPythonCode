import utility
def test_case_1():
    assert utility.first_N_numbers(5) == [1,"#",2,"#",3,"#",4,"#",5]
def test_case_2():
    assert utility.first_N_numbers(1) == [1]
def test_case_3():
    assert utility.first_N_numbers(3) == [1,"#",2,"#",3]