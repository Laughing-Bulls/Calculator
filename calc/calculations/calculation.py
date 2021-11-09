""" This is the calculation base class / ABSTRACT CLASS """


class Calculation:
    """ the constructor is the first function called"""

    # pylint: disable=too-few-public-methods
    def __init__(self, values: tuple):
        """ initialize - self references instantiated object of class"""
        self.values = Calculation.convert_args_to_list(values)

    # @classmethod
    # def create(cls, values: tuple):
        """ class factory method"""
    #    return cls(values)

    # class factory method
    @staticmethod
    def convert_args_to_list(values):
        """ bound to the class, not the instance of the class"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float
