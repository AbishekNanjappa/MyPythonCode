import utility
def test_case1():
    assert utility.calculate(1,'+',2) == 3
def test_case2():
    assert utility.calculate(5,'-',4) == 1
def test_case3():
    assert utility.calculate(7,'-',8) == -1
def test_case4():
    assert utility.calculate(3,'*',4) == 12
def test_case5():
    assert utility.calculate(4,'/',2) == 2
def test_case6():
    assert utility.calculate(1,'/',2) == 0.5