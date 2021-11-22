""" Subtraction inherits arguments from parent Calculation class"""
from calc.calculations.calculation import Calculation


class Subtraction(Calculation):
    """ values come from the calculation parent class"""

    def getresult(self):
        """ Start with first element, and then subtract the numbers following it"""
        difference = self.values[0]
        for value in self.values[1:]:
            difference -= value
        return difference
