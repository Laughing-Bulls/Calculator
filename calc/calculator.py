""" This is a Python calculator"""
# import the namespaces
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.calculations.exponent import Exponent
from calc.history.calculations import Calculations


class Calculator:
    """ This is the static Calculator class"""

    @staticmethod
    def add_numbers(tuple_vales: tuple):
        """ adds inputted numbers"""
        addition = Addition(tuple_vales)
        Calculations.add_to_history(addition)
        return addition.getresult()

    @staticmethod
    def subtract_numbers(tuple_vales: tuple):
        """ subtract inputted numbers"""
        subtract = Subtraction(tuple_vales)
        Calculations.add_to_history(subtract)
        return subtract.getresult()

    @staticmethod
    def multiply_numbers(tuple_vales: tuple):
        """ multiply inputted numbers and store the result"""
        multiply = Multiplication(tuple_vales)
        Calculations.add_to_history(multiply)
        return multiply.getresult()

    @staticmethod
    def divide_numbers(tuple_vales: tuple):
        """ divide two numbers and store the result"""
        divide = Division(tuple_vales)
        Calculations.add_to_history(divide)
        return divide.getresult()

    @staticmethod
    def power_numbers(tuple_vales: tuple):
        """ compute one number to the power of another and store the result"""
        expo = Exponent(tuple_vales)
        Calculations.add_to_history(expo)
        return expo.getresult()
