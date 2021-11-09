"""Testing the Calculator"""
import pytest
# import pprint: allows print during test
from calc.calculator import Calculator
from calc.history.calculations import Calculations


@pytest.fixture()
def clear_history_fixture():
    """FIXTURE to clear the history cache"""
    Calculations.clear_history()


def test_calculator_add(clear_history_fixture):
    """Testing the addition function of the calculator"""
    # pylint: disable=redefined-outer-name,unused-argument
    # Arrange by calling the Calculator method and Assert that results are correct
    assert Calculator.add_numbers(2.0, 3.0, 4.0) == 9.0


def test_calculator_subtract(clear_history_fixture):
    """Testing the subtract function of the calculator"""
    # pylint: disable=redefined-outer-name,unused-argument
    # Arrange by calling the Calculator method and Assert that results are correct
    assert Calculator.subtract_numbers(2.0, 1.0) == -3.0


def test_calculator_multiply(clear_history_fixture):
    """ tests multiplication of two numbers"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculator.multiply_numbers(2.0, 4.0) == 8.0


def test_calculator_divide(clear_history_fixture):
    """ tests division of two numbers"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculator.divide_numbers(10.0, 2.0) == 5.0


def test_calculator_dividebyzero(clear_history_fixture):
    """ tests division by zero Exception"""
    # pylint: disable=redefined-outer-name,unused-argument
    with pytest.raises(Exception):
        assert Calculator.divide_numbers(10.0, 0)


def test_calculator_power(clear_history_fixture):
    """ tests calculation of one number to the power of another"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculator.power_numbers(10.0, 0.0) == 1.0
