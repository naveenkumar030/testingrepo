from calculator import add, multiply

def test_add():
    assert add(2, 3) == 5

def test_multiply_basic():
    assert multiply(3, 4) == 12

def test_multiply_two_by_three():
    assert multiply(2, 3) == 6

def test_multiply_four_by_five():
    assert multiply(4, 5) == 20

def test_multiply_ten_by_ten():
    assert multiply(10, 10) == 100

def test_multiply_five_by_five():
    assert multiply(5, 5) == 25

def test_multiply_six_by_seven():
    assert multiply(6, 7) == 42

def test_multiply_eight_by_nine():
    assert multiply(8, 9) == 72
