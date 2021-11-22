""" Multiplication inherits arguments from parent Calculation class"""
from calc.calculations.calculation import Calculation


class Multiplication(Calculation):
    """ values come from the Calculation parent class"""
    def getresult(self):
        """ Multiply all inputs together"""
        product = 1.0
        for value in self.values:
            product *= value
        return product
