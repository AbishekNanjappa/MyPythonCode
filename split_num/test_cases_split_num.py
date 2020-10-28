import utility
def test_case_1():
    assert utility.split_num(324) == [3,"#",2,"#",4]
def test_case_2():
    assert utility.split_num(5987) == [5,"#",9,"#",8,"#",7]
def test_case_3():
    assert utility.split_num(1) == [1]
def test_case_4():
    assert utility.split_num(95) == [9,"#",5]
def test_case_5():
    assert utility.split_num(9876543) == [9,"#",8,"#",7,"#",6,"#",5,"#",4,"#",3]