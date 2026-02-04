from grade_calculator import calculate_grade

def test_A_plus():
    assert calculate_grade([95, 92, 93, 94, 96]) == "A+"

def test_A():
    assert calculate_grade([80, 78, 76, 75, 77]) == "A"

def test_B():
    assert calculate_grade([65, 62, 60, 63, 64]) == "B"

def test_C():
    assert calculate_grade([52, 50, 55, 53, 54]) == "C"

def test_Fail():
    assert calculate_grade([40, 45, 42, 38, 41]) == "Fail"