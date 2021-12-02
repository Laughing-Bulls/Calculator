""" This is a script to run the Python calculator"""
from filehandling.watcher import Watchdog


def main():
    """ Run the calculator program"""

    print("Calculator program is running. Monitoring for new input files to calculate...")

    Watchdog.watch()

    print("That's all, Folks!")


if __name__ == "__main__":
    main()

""" MANUAL USER TEST - NOT USED
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

    inputs = (value_a, value_b)

    if operand == "+":
        answer = Calculator.addition(inputs)
        print(str(value_a) + " + " + str(value_b) + " = " + str(answer))

    if operand == "-":
        answer = Calculator.subtraction(inputs)
        print(str(value_a) + " - " + str(value_b) + " = " + str(answer))

    if operand == "*":
        answer = Calculator.multiplication(inputs)
        print(str(value_a) + " * " + str(value_b) + " = " + str(answer))

    if operand == "/":
        if value_b == 0:
            raise Exception("Division by zero is not allowed")
        answer = Calculator.division(inputs)
        print(str(value_a) + " / " + str(value_b) + " = " + str(answer))

    if operand == "^":
        answer = Calculator.exponent(inputs)
        print(str(value_a) + "^" + str(value_b) + " = " + str(answer))
    """
