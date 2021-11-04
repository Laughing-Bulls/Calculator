""" Exponent calculation that inherits A and B from calculation class"""

from calc.calculation import Calculation


class Exponent(Calculation):
    # A and B come from the calculation parent class
    """ Calculates one value to the power of another"""
    def getResult(self):
        """ Take A to the power of B"""
        return self.value_a ** self.value_b
