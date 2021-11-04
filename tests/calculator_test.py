"""Testing the Calculator"""
import pytest
# import pprint

from calculator.calculator import Calculator


@pytest.fixture
def zero_history_fixture():
    """ This FIXTURE will clear the history cache"""
    # This runs each time it is passed to a test
    Calculator.clear_history()


def test_clear_history(zero_history_fixture):
    """ Testing that history cache has been cleared"""
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 3) == 6
    assert Calculator.add_numbers(5, 2) == 7
    assert Calculator.clear_history() is True
    assert Calculator.count_history() == 0


def test_calculator_add(zero_history_fixture):
    """Testing the Add function of the calculator AND the count in history cache"""
    # Arrange by calling the calc method and Assert that results are correct
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 3) == 6
    assert Calculator.add_numbers(5, 2) == 7
    assert Calculator.count_history() == 3


def test_first_and_last_result(zero_history_fixture):
    """Testing the get first and last history results"""
    # Arrange by calling the calc method and Assert that results are correct
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 3) == 6
    assert Calculator.add_numbers(5, 2) == 7
    assert Calculator.get_first_result() == 4
    assert Calculator.get_history_result() == 7


def test_calculator_subtract():
    """Testing the subtract function of the calculator"""
    assert Calculator.subtract_numbers(2, 1) == 1


def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(2, 4) == 8


def test_calculator_divide():
    """ tests division of two numbers"""
    assert Calculator.divide_numbers(10, 2) == 5


def test_calculator_dividebyzero():
    """ tests division by zero Exception"""
    with pytest.raises(Exception):
        assert Calculator.divide_numbers(10, 0)


def test_calculator_power():
    """ tests calculation of one number to the power of another"""
    assert Calculator.power_numbers(10, 0) == 1
