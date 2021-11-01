"""Testing the Calculator"""
import pytest

from calculator.calculator import Calculator


def test_calculator_add():
    """Testing the Add function of the calculator"""
    # Arrange by calling the calc method and Assert that results are correct
    assert Calculator.add_numbers(2, 2) == 4


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
    """ tests power calculation of two numbers"""
    assert Calculator.power_numbers(10, 0) == 1
