""" This is a script to run the Python calculator"""
# from filehandling.filehandling import Filehandling
# from calc.history.operations import Operations
# from calc.calculator import Calculator
# from calc.history.calculations import Calculations
# from filehandling.filehandling import Filehandling
# from filehandling.fileops import Fileops
# pip install watchdog
# import sys
# import time
# import logging
# import os
# import pandas as pd
# import time
# from watchdog.observers import Observer
# from watchdog.events import LoggingEventHandler
# from watchdog.events import PatternMatchingEventHandler
from filehandling.watcher import Watchdog


def main():
    """ Run the calculator program"""

    print("Calculator program is running. Monitoring for new input files to calculate...")

    Watchdog.watch()

    print("That's all, Folks!")


if __name__ == "__main__":
    main()

""" SPARE CODE
    # print(series)
    # by default, columns get inserted at the end: df.insert(values)
    # df.insert(0, 0, series, allow_duplicates=True)

    # Filehandling.write_line_to_file("output_test.csv", data)
    # pathname = "output_test.csv"
    # pd.to_csv(pathname, df)  # creates a csv file from a dataframe

    # values_in = [1, 2, 3, 4, 5]  # assign a series of numbers
    # print(type(values_in))

    # df = pd.DataFrame(values_in)
    # print(type(df))

    # df.to_csv(filename, index=False)  # creates a csv file from a dataframe

    # data_in_file = pd.read_csv(filename, index_col=None)
    # print(df)
    # output = data_in_file.values.tolist()
    # print(type(output))
    # print(output)
    # print(output == [[1], [2], [3], [4], [5]])
    """

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
        answer = Calculator.add_numbers(inputs)
        print(str(value_a) + " + " + str(value_b) + " = " + str(answer))

    if operand == "-":
        answer = Calculator.subtract_numbers(inputs)
        print(str(value_a) + " - " + str(value_b) + " = " + str(answer))

    if operand == "*":
        answer = Calculator.multiply_numbers(inputs)
        print(str(value_a) + " * " + str(value_b) + " = " + str(answer))

    if operand == "/":
        if value_b == 0:
            raise Exception("Division by zero is not allowed")
        answer = Calculator.divide_numbers(inputs)
        print(str(value_a) + " / " + str(value_b) + " = " + str(answer))

    if operand == "^":
        answer = Calculator.power_numbers(inputs)
        print(str(value_a) + "^" + str(value_b) + " = " + str(answer))
    """
