""" Exponent calculation that inherits A and B from calculation class"""

from calc.calculations.calculation import Calculation


class Exponent(Calculation):
    # A and B come from the calculation parent class
    """ Calculates one value to the power of another"""
    def getresult(self):
        """ Take A to the power of B"""
        exponential = self.values[0] ** self.values[1]
        return exponential
