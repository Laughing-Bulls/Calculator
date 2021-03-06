""" Division inherits arguments from parent Calculation class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """ values come from the calculation parent class"""

    def getresult(self):
        """ Divide first element by each subsequent element; return None if dividing by zero"""
        quotient = self.values[0]
        for value in self.values[1:]:
            if value != 0:
                quotient /= value
            else:
                return None
        return quotient
