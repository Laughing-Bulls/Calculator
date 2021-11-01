""" This is a Python calculator"""


class Calculator:
    """ This is the static Calculator class"""

    @staticmethod
    def add_numbers(value_a, value_b):
        """ adds two numbers"""
        return value_a + value_b

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ subtract numbers"""
        return value_a - value_b

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        return value_a * value_b

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divide two numbers and store the result"""
        if value_b == 0:
            raise Exception("Division by zero is not allowed")
        return value_a / value_b

    @staticmethod
    def power_numbers(value_a, value_b):
        """ compute one number to the power of another and store the result"""
        return value_a ** value_b
