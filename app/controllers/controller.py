"""Parent class for page controllers"""
# pylint: disable=too-few-public-methods

class ControllerBase:
    """Page controller"""
    @staticmethod
    def base():
        """ This is a parent of other classes, for efficient code deployment"""
        return True
