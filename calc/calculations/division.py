""" Division inherits arguments from parent Calculation class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """ values come from the calculation parent class"""

    def getresult(self):
        """ Divide first element by each subsequent element; throw exception if dividing by zero"""
        quotient = self.values[0]
        for value in self.values[1:]:
            if self.values[1] == 0:
                raise Exception("Division by zero is not allowed")
            quotient /= value
        return quotient
