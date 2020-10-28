import utility
def test_g1():
    l1 = [1,2,3]
    assert utility.greatest_num(l1) == 3
def test_g2():
    l2 = [3,2,1]
    assert utility.greatest_num(l2) == 3
def test_g3():
    l3 = [2,3,1]
    assert utility.greatest_num(l3) == 3