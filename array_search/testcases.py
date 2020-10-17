import utility
def test_case_1():
    l1 = [1,2,3,4,5]
    assert utility.search(l1,5,1) == "True" 
def test_case_2():
    l2 = [-2,-1,0,1,2]
    assert utility.search(l2,5,3) == "False"
def test_case_3():
    l3 = [100,98,95,89]
    assert utility.search(l3,4,95) == "True"
def test_case_4():
    l4 = [5,7,9,11,13,15,17,19]
    assert utility.search(l4,8,8) == "False"