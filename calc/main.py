""" This is a script to run the Python calculator"""

from calc.calculator import Calculator
from calc.history.calculations import Calculations


def main():
    """ User test of the calculator program"""

    Calculations.add_to_history(2)
    print(Calculations.get_history_result())

    Calculator.add_numbers(2.0, 3.0, 4.0)
    print(Calculations.get_history_result())

    Calculations.clear_history()

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
        answer = Calculator.add_numbers(value_a, value_b)
        print(str(value_a) + " + " + str(value_b) + " = " + str(answer))

    if operand == "-":
        answer = Calculator.subtract_numbers(value_a, value_b)
        print(str(value_a) + " - " + str(value_b) + " = " + str(answer))

    if operand == "*":
        answer = Calculator.multiply_numbers(value_a, value_b)
        print(str(value_a) + " * " + str(value_b) + " = " + str(answer))

    if operand == "/":
        if value_b == 0:
            raise Exception("Division by zero is not allowed")
        answer = Calculator.divide_numbers(value_a, value_b)
        print(str(value_a) + " / " + str(value_b) + " = " + str(answer))

    if operand == "^":
        answer = Calculator.power_numbers(value_a, value_b)
        print(str(value_a) + "^" + str(value_b) + " = " + str(answer))

    print("That's all, Folks!")


if __name__ == "__main__":
    main()
