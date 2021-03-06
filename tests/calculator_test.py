"""Testing the Calculator - using ARRANGE, ACT, ASSERT"""
from calc.calculator import Calculator
from calc.history.calculations import Calculations


def test_calculator_add():
    """Testing the addition feature of the calculator"""
    # Arrange by calling the Calculator method and Assert that results are correct
    test_tuple = (2.0, 3.0, 4.0)
    Calculator.addition(test_tuple)
    assert Calculations.get_history_result() == 9.0


def test_calculator_subtract():
    """Testing the subtract feature of the calculator"""
    # Arrange by calling the Calculator method and Assert that results are correct
    test_tuple = (3.0, 1.0, 1.0)
    Calculator.subtraction(test_tuple)
    assert Calculations.get_history_result() == 1.0


def test_calculator_multiply():
    """ tests multiplication feature"""
    test_tuple = (2.0, 4.0, 2.0)
    Calculator.multiplication(test_tuple)
    assert Calculations.get_history_result() == 16.0


def test_calculator_divide():
    """ tests division of numbers"""
    test_tuple = (20.0, 2.0, 2.0)
    Calculator.division(test_tuple)
    assert Calculations.get_history_result() == 5.0


def test_calculator_dividebyzero():
    """ tests division by zero"""
    test_tuple = (10.0, 0)
    Calculator.division(test_tuple)
    assert Calculations.get_history_result() is None


def test_calculator_average():
    """ tests average feature of calculator"""
    test_tuple = (10.0, 2.0, 3.0)
    Calculator.average(test_tuple)
    assert Calculations.get_history_result() == 5.0


def test_calculator_power():
    """ tests calculation of one number to the power of another"""
    test_tuple = (3.0, 2.0, 2.0)
    Calculator.exponent(test_tuple)
    assert Calculations.get_history_result() == 81.0


def test_calculator_power_too_high():
    """ tests calculation of one number to the power of another"""
    test_tuple = (30.0, 20.0, 20.0)
    Calculator.exponent(test_tuple)
    assert Calculations.get_history_result() is None


def test_get_last_result_value():
    """ tests calculation of one number to the power of another"""
    Calculations.add_to_history(5.0)
    assert Calculator.get_last_result_value() == 5.0
