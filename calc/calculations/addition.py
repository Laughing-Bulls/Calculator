""" Addition class inherits from parent Calculation class"""
from calc.calculations.calculation import Calculation


# This extends the Addition class within Calculation
class Addition(Calculation):
    """ values come from the Calculation parent class """

    def getresult(self):
        """ Add all the elements of the tuple"""
        return sum(self.values)
