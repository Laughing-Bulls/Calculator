""" Exponent inherits arguments from parent Calculation class"""
from calc.calculations.calculation import Calculation


class Exponent(Calculation):
    """ values come from the calculation parent class"""

    def getresult(self):
        """ Raise first element to the power of second one, continue with subsequent ones"""
        exponential = self.values[0]
        for value in self.values[1:]:
            exponential = exponential ** value
        return exponential
