""" Division calculation that inherits A and B from calculation class"""

from calc.calculation import Calculation


class Division(Calculation):
    """ A and B come from the calculation parent class"""
    def getresult(self):
        """ Divide A / B; throw exception if dividing by zero"""
        if self.value_b == 0:
            raise Exception("Division by zero is not allowed")
        return self.value_a / self.value_b
