import pytest

from myapp.mymodule.funcs import add, subtract, multiply, divide, square_area  # Include square_area

@pytest.mark.easy_operation
def test_add():
    # This test will fail. so i chnaged the output from 14 to 12
    assert add(4, 8) == 12

@pytest.mark.easy_operation
def test_subtract():
    assert subtract(3, 6) == -3

@pytest.mark.difficult_operation
def test_multiply():
    assert multiply(4, 5) == 20

@pytest.mark.difficult_operation
def test_divide():
    assert divide(56, 8) == 7

@pytest.mark.difficult_operation
def test_square_area():
    assert square_area(8.9) == pytest.approx(72, rel=1e-2)  # my specific output based on my student ID (100939472)
    assert square_area(9) == 81  # modified test case that will pass
    assert square_area(72) == 5184  #  modified test case that will pass
    