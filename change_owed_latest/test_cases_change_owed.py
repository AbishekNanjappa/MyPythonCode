import utility
def test_case_1():
    assert utility.change_owed(1,0,5) == (1,0)
def test_case_2():
    assert utility.change_owed(3,3,16) == (3,1)
def test_case_3():
    assert utility.change_owed(0,1,1) == (0,1)
def test_case_4():
    assert utility.change_owed(0,0,20) == (-1,-1)
def test_case_5():
    assert utility.change_owed(5,5,21) == (4,1)
#one 5 re coin and multiple one re coins and possible amount