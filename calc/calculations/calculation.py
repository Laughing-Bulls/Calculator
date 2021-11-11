""" This is the calculation base class / it is an ABSTRACT CLASS """


class Calculation:
    """ the constructor is the first function called"""

    # pylint: disable=too-few-public-methods
    def __init__(self, values: tuple):
        """ initialize - self references instantiated object of class"""
        self.values = Calculation.convert_to_tuple_of_floats(values)

    @classmethod
    def create(cls, values: tuple):
        """ class factory method"""
        return cls(values)

    # class factory method
    @staticmethod
    def convert_to_tuple_of_floats(values):
        """ make tuples of type float. values bound to the class, not the instance of the class"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)
