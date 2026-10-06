from calculator import add, multiply, subtract, divide, power

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

def test_subtract_positive():
    assert subtract(10, 4) == 6

def test_subtract_to_negative():
    assert subtract(3, 8) == -5

def test_subtract_zero():
    assert subtract(15, 0) == 15

def test_divide_clean():
    assert divide(10, 2) == 5.0

def test_divide_fraction():
    assert divide(1, 4) == 0.25

def test_divide_large():
    assert divide(100, 5) == 20.0

def test_power_two_cubed():
    assert power(2, 3) == 8

def test_power_three_squared():
    assert power(3, 2) == 9

def test_power_five_cubed():
    assert power(5, 3) == 125

def test_power_two_to_fourth():
    assert power(2, 4) == 16
