""" This is a Python calculator"""


class Calculator:
    """ This is the Calculator class"""

    def add_numbers(self, value_a, value_b):
        """ adds two numbers"""
        return value_a + value_b

    def subtract_numbers(self, value_a, value_b):
        """ subtract numbers"""
        return value_a - value_b

    def multiply_numbers(self, value_a, value_b):
        """ multiply two numbers and store the result"""
        return value_a * value_b

    def divide_numbers(self, value_a, value_b):
        """ divide two numbers and store the result"""
        try:
            return value_a / value_b
        except ZeroDivisionError:
            print("Division by zero is not allowed")

    def power_numbers(self, value_a, value_b):
        """ compute one number to the power of another and store the result"""
        return value_a ** value_b

    print("Welcome to the calculator!")
    while True:
        try:
            value_a = float(input("Enter value a: "))
            break
        except ValueError:
            print("That is not a valid number")

    valid_operands = ["+", "-", "*", "/", "^"]
    operand = input("Enter a function (+,-,*,/,^): ")
    if operand not in valid_operands:
        raise Exception("That is not a valid function")

    while True:
        try:
            value_b = float(input("Enter value b: "))
            break
        except ValueError:
            print("That is not a valid number")

    if operand == "+":
        print(str(value_a) + " + " + str(value_b) + " = " + str(add_numbers(value_a, value_b)))

    if operand == "-":
        print(str(value_a) + " - " + str(value_b) + " = " + str(subtract_numbers(value_a, value_b)))

    if operand == "*":
        print(str(value_a) + " * " + str(value_b) + " = " + str(multiply_numbers(value_a, value_b)))

    if operand == "/":
        if value_b == "0":
            raise Exception("Division by zero is not allowed")
        else:
            print(str(value_a) + " / " + str(value_b) + " = " + str(divide_numbers(value_a, value_b)))

    if operand == "^":
        print(str(value_a) + "^" + str(value_b) + " = " + str(power_numbers(value_a, value_b)))

    print("That's all, Folks!")
