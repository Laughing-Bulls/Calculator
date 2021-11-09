""" Multiplication calculation that inherits A and B from calculation class"""

from calc.calculations.calculation import Calculation


class Multiplication(Calculation):
    """ A and B come from the calculation parent class"""
    def getresult(self):
        """ Multiply inputs"""
        product = 1.0
        for value in self.values:
            product *= value
        return product
