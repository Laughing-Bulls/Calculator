""" Subtraction calculation that inherits A and B from calculation class"""

from calc.calculations.calculation import Calculation


# This extends the Addition class within Calculation
class Subtraction(Calculation):
    """ values come from the calculation parent class"""
    def getresult(self):
        """ Subtract numbers in order of input"""
        difference = 0.0
        for value in self.values:
            difference -= value
        return difference
