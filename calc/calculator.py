""" This is a Python calculator"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.calculations.exponent import Exponent
from calc.history.calculations import Calculations


class Calculator:
    """ This is the static Calculator class"""

    @staticmethod
    def addition(tuple_vales: tuple):
        """ add inputted numbers and store the result"""
        Calculations.add_to_history(Addition.create(tuple_vales).getresult())
        return True

    @staticmethod
    def subtraction(tuple_vales: tuple):
        """ subtract inputted numbers from first element"""
        Calculations.add_to_history(Subtraction.create(tuple_vales).getresult())
        return True

    @staticmethod
    def multiplication(tuple_vales: tuple):
        """ multiply inputted numbers and store the result"""
        Calculations.add_to_history(Multiplication.create(tuple_vales).getresult())
        return True

    @staticmethod
    def division(tuple_vales: tuple):
        """ divide first number by the following elements"""
        Calculations.add_to_history(Division.create(tuple_vales).getresult())
        return True

    @staticmethod
    def exponent(tuple_vales: tuple):
        """ compute one number to the powers of following elements"""
        Calculations.add_to_history(Exponent.create(tuple_vales).getresult())
        return True
