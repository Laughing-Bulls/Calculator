""" This is the calculation base class / ABSTRACT CLASS """


class Calculation:
    """ the constructor is the first function called"""

    def __init__(self, value_a, value_b):
        """ initialize - self references instantiated object of class"""
        self.value_a = value_a
        self.value_b = value_b

    # class factory method
    @classmethod
    def create(cls, value_a, value_b):
        """ bound to the class, not the instance of the class"""
        return cls(value_a, value_b)
