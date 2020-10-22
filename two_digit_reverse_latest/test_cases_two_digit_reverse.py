import utility
def test_cases_1():
    assert utility.reverse(12) == 21
def test_cases_2():
    assert utility.reverse(99) == 99
def test_cases_3():
    assert utility.reverse(7) == -1          #return -1 if input is not a two digit number       
def test_cases_4(): 
    assert utility.reverse(121) == -1        #return -1 if input is not a two digit number 