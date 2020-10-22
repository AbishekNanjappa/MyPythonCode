import utility
def test_case_1():
    assert utility.triangle_type(3,4,5) == "Scalene"
def test_case_2():
    assert utility.triangle_type(2,2,3) == "Iscoceles"
def test_case_3():
    assert utility.triangle_type(1,1,1) == "Equilateral"
def test_case_4():
    assert utility.triangle_type(0,0,0) == "NA"
def test_case_5():
    assert utility.triangle_type(5,0,5) == "NA"