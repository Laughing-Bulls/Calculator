""" Average class inherits from parent Calculation class"""
import statistics
from calc.calculations.calculation import Calculation


# This extends the Average class within Calculation
class Average(Calculation):
    """ values come from the Calculation parent class """

    def getresult(self):
        """ Average all the elements of the tuple"""
        return statistics.mean(self.values)
