""" Addition calculation that inherits A and B from calculation class"""

from calc.calculation import Calculation


# This extends the Addition class within Calculation
class Addition(Calculation):
    """ A and B come from the calculation parent class """
    def getResult(self):
        """ Add A + B"""
        return self.value_a + self.value_b
