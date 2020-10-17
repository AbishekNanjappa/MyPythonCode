import utility_positive
def test_sum1():
        assert utility_positive.sum_of_positive(1,2,3,4,5) == 15
def test_sum2():
        assert utility_positive.sum_of_positive(0,0,0,0,0) == 0
def test_sum3():  
        assert utility_positive.sum_of_positive(-1,-2,-3,-4,-5) == 0
def test_sum4():
        assert utility_positive.sum_of_positive(-2,-1,0,1,2) == 3  