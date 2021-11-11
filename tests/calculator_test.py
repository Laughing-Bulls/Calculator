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
    """Testing the addition feature of the calculator"""
    # pylint: disable=redefined-outer-name,unused-argument
    # Arrange by calling the Calculator method and Assert that results are correct
    input_tuple = (2.0, 3.0, 4.0)
    assert Calculator.add_numbers(input_tuple) == 9.0


def test_calculator_subtract(clear_history_fixture):
    """Testing the subtract feature of the calculator"""
    # pylint: disable=redefined-outer-name,unused-argument
    # Arrange by calling the Calculator method and Assert that results are correct
    input_tuple = (2.0, 1.0)
    assert Calculator.subtract_numbers(input_tuple) == -3.0


def test_calculator_multiply(clear_history_fixture):
    """ tests multiplication feature"""
    # pylint: disable=redefined-outer-name,unused-argument
    input_tuple = (2.0, 4.0, 2.0)
    assert Calculator.multiply_numbers(input_tuple) == 16.0


def test_calculator_divide(clear_history_fixture):
    """ tests division of two numbers"""
    # pylint: disable=redefined-outer-name,unused-argument
    input_tuple = (10.0, 2.0)
    assert Calculator.divide_numbers(input_tuple) == 5.0


def test_calculator_dividebyzero(clear_history_fixture):
    """ tests division by zero Exception"""
    # pylint: disable=redefined-outer-name,unused-argument
    with pytest.raises(Exception):
        input_tuple = (10.0, 0)
        assert Calculator.divide_numbers(input_tuple)


def test_calculator_power(clear_history_fixture):
    """ tests calculation of one number to the power of another"""
    # pylint: disable=redefined-outer-name,unused-argument
    input_tuple = (10.0, 0)
    assert Calculator.power_numbers(input_tuple) == 1.0
