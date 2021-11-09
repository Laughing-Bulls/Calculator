""" Addition calculation that inherits arguments from calculation class"""
from calc.calculations.calculation import Calculation


# This extends the Addition class within Calculation
class Addition(Calculation):
    """ Arguments come from the calculation parent class """

    def getresult(self):
        """ Add the arguments"""
        result = 0.0
        for value in self.values:
            result += value
        return result
        # TEST THIS: return sum(self.values)
