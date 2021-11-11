"""Testing the Calculator - using ARRANGE, ACT, ASSERT"""
import pytest
from calc.calculator import Calculator
# import pprint: allows print during test
from calc.history.calculations import Calculations


def test_calculator_add():
    """Testing the addition feature of the calculator"""
    # Arrange by calling the Calculator method and Assert that results are correct
    test_tuple = (2.0, 3.0, 4.0)
    Calculator.add_numbers(test_tuple)
    assert Calculations.get_history_result() == 9.0


def test_calculator_subtract():
    """Testing the subtract feature of the calculator"""
    # Arrange by calling the Calculator method and Assert that results are correct
    test_tuple = (3.0, 1.0, 1.0)
    Calculator.subtract_numbers(test_tuple)
    assert Calculations.get_history_result() == 1.0


def test_calculator_multiply():
    """ tests multiplication feature"""
    test_tuple = (2.0, 4.0, 2.0)
    Calculator.multiply_numbers(test_tuple)
    assert Calculations.get_history_result() == 16.0


def test_calculator_divide():
    """ tests division of two numbers"""
    test_tuple = (20.0, 2.0, 2.0)
    Calculator.divide_numbers(test_tuple)
    assert Calculations.get_history_result() == 5.0


def test_calculator_dividebyzero():
    """ tests division by zero Exception"""
    with pytest.raises(Exception):
        test_tuple = (10.0, 0)
        assert Calculator.divide_numbers(test_tuple)


def test_calculator_power():
    """ tests calculation of one number to the power of another"""
    test_tuple = (3.0, 2.0, 2.0)
    Calculator.power_numbers(test_tuple)
    assert Calculations.get_history_result() == 81.0
