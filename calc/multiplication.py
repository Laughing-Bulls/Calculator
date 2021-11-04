""" Multiplication calculation that inherits A and B from calculation class"""

from calc.calculation import Calculation


class Multiplication(Calculation):
    """ A and B come from the calculation parent class"""
    def getResult(self):
        """ Multiply A * B"""
        return self.value_a * self.value_b
