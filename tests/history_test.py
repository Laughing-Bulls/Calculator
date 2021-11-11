"""Testing the functions of the History cache"""
import pytest
# import pprint: allows print during test
from calc.history.calculations import Calculations
from calc.calculator import Calculator


@pytest.fixture
def clear_history_fixture():
    """ This FIXTURE will clear the history cache - it runs each time it is passed to a test """
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


@pytest.fixture
def make_list_of_calculations():
    """ This FIXTURE adds 3 entries to the history cache. It runs each time it's passed to a test"""
    # pylint: disable=redefined-outer-name
    Calculations.add_to_history(3.0)
    Calculations.add_to_history(5.0)
    Calculations.add_to_history(7.0)
    # values = (1, 2)
    # addition = Addition(values)
    # Calculations.add_to_history(addition)


def test_clear_history(clear_history_fixture, make_list_of_calculations):
    """ Testing that history cache has been cleared"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.count_history() == 3
    Calculations.clear_history()
    assert Calculations.clear_history() is True
    assert Calculations.count_history() == 0


def test_count_history(clear_history_fixture, make_list_of_calculations):
    """Testing the count in history cache"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.count_history() == 3


def test_get_history_result(clear_history_fixture, make_list_of_calculations):
    """Testing the add to history results"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.get_history_result() == 7.0


def test_first_result(clear_history_fixture, make_list_of_calculations):
    """Testing the get first history results"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.get_first_result() == 3.0


def test_add_to_history(clear_history_fixture, make_list_of_calculations):
    """Testing the add to history results"""
    # pylint: disable=redefined-outer-name,unused-argument
    values = (2, 6)
    Calculations.add_to_history(Calculator.add_numbers(values))
    assert Calculations.get_history_result() == 8.0


def test_specified_result(clear_history_fixture, make_list_of_calculations):
    """Testing a count of history results"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.get_specified_result(1) == 5.0
