""" Subtraction calculation that inherits A and B from calculation class"""

from calc.calculation import Calculation


# This extends the Addition class within Calculation
class Subtraction(Calculation):
    """ A and B come from the calculation parent class"""
    def getresult(self):
        """ Subtract A - B"""
        return self.value_a - self.value_b
