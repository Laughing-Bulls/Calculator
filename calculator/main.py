""" This is the my Python calculator"""

class Calculator:
    """ This is the Calculator class"""

    result = 0

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result

    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result

    def multiply_numbers(self, value_a, value_b):
        """ multiply two numbers and store the result"""
        self.result = value_a * value_b
        return self.result

    def divide_numbers(self, value_a, value_b):
        """ divide two numbers and store the result"""
        try:
            self.result = value_a / value_b
        except ZeroDivisionError:
            print("Division by zero is not allowed")
        return self.result

    def power_numbers(self, value_a, value_b):
        """ compute one number to the power of another and store the result"""
        self.result = value_a ** value_b
        return self.result
