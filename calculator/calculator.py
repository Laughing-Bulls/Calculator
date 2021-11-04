""" This is a Python calculator"""
# import the namespaces
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division
from calc.exponent import Exponent


class Calculator:
    """ This is the static Calculator class"""
    # history is a static property
    history = []

    @staticmethod
    def clear_history():
        """ clears the history cache"""
        Calculator.history.clear()
        return True

    @staticmethod
    def count_history():
        """ returns how many calculations are in history"""
        return len(Calculator.history)

    @staticmethod
    def add_to_history(calculation):
        """ adds the result to history cache"""
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_first_result():
        """ 0 gets the first item added to the history cache"""
        return Calculator.history[0].getresult()

    @staticmethod
    def get_history_result():
        """ -1 gets the most recent item added to the history cache"""
        return Calculator.history[-1].getresult()

    @staticmethod
    def add_numbers(value_a, value_b):
        """ adds two numbers"""
        addition = Addition.create(value_a, value_b)
        Calculator.add_to_history(addition)
        return Calculator.get_history_result()

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ subtract numbers"""
        subtract = Subtraction.create(value_a, value_b)
        Calculator.add_to_history(subtract)
        return Calculator.get_history_result()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        multiply = Multiplication.create(value_a, value_b)
        Calculator.add_to_history(multiply)
        return Calculator.get_history_result()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divide two numbers and store the result"""
        divide = Division.create(value_a, value_b)
        Calculator.add_to_history(divide)
        return Calculator.get_history_result()

    @staticmethod
    def power_numbers(value_a, value_b):
        """ compute one number to the power of another and store the result"""
        expo = Exponent.create(value_a, value_b)
        Calculator.add_to_history(expo)
        return Calculator.get_history_result()
