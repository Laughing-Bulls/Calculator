""" Division calculation that inherits A and B from calculation class"""

from calc.calculations.calculation import Calculation


class Division(Calculation):
    """ A and B come from the calculation parent class"""
    def getresult(self):
        """ Divide A / B; throw exception if dividing by zero"""
        if self.values[1] == 0:
            raise Exception("Division by zero is not allowed")
        return self.values[0] / self.values[1]
