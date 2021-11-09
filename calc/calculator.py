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
    def add_numbers(*args):
        """ adds inputted numbers"""
        addition = Addition(args)
        Calculations.add_to_history(addition)
        return addition.getresult()

    @staticmethod
    def subtract_numbers(*args):
        """ subtract inputted numbers"""
        subtract = Subtraction(args)
        Calculations.add_to_history(subtract)
        return subtract.getresult()

    @staticmethod
    def multiply_numbers(*args):
        """ multiply inputted numbers and store the result"""
        multiply = Multiplication(args)
        Calculations.add_to_history(multiply)
        return multiply.getresult()

    @staticmethod
    def divide_numbers(*args):
        """ divide two numbers and store the result"""
        divide = Division(args)
        Calculations.add_to_history(divide)
        return divide.getresult()

    @staticmethod
    def power_numbers(*args):
        """ compute one number to the power of another and store the result"""
        expo = Exponent(args)
        Calculations.add_to_history(expo)
        return expo.getresult()
