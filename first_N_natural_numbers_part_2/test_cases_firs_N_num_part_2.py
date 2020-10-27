import utility
def test_cases_1():
    assert utility.first_N_num_2(5) == [5,"#",4,"#",3,"#",2,"#",1]
def test_cases_2():
    assert utility.first_N_num_2(1) == [1]
def test_cases_3():
    assert utility.first_N_num_2(3) == [3,"#",2,"#",1]