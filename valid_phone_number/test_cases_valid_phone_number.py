import utility
def test_case_1():
    assert utility.phone_no_check(9611402002) == "Valid"
def test_case_2():
    assert utility.phone_no_check(9845518812) == "Valid"
def test_case_3():
    assert utility.phone_no_check(8612309485) == "Valid"
def test_case_4():
    assert utility.phone_no_check(7890235489) == "Valid"
def test_case_5():
    assert utility.phone_no_check(5638902134) == "Invalid"
def test_case_6():
    assert utility.phone_no_check(984569275) == "Invalid"
def test_case_7():
    assert utility.phone_no_check(45783761) == "Invalid"
def test_case_8():
    assert utility.phone_no_check(21123) == "Invalid"