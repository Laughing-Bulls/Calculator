""" This is a script to run a user test of the Python calculator"""
from filehandling.filehandling import Filehandling

# pip install watchdog
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler
# Use Pandas library with alias pd for file actions
from filehandling.filehandling import Filehandling
import os
import pandas as pd


def main():
    """ User test of the calculator program"""

    print("Calculator program is running. Monitoring for new input files to calculate...")
    # print current working directory
    print(os.getcwd())

    # data = Filehandling.read_line_from_file("input_test.csv")
    # data = pd.read_csv("input_test.csv", index_col=0)
    # print(data.head())
    # print(data.tail())
    # print(data)

    # Filehandling.write_line_to_file("output_test.csv", data)
    # pathname = "output_test.csv"
    # pd.to_csv(pathname, df)  # creates a csv file from a dataframe

    values_in = [1, 2, 3, 4, 5]  # assign a series of numbers
    print(type(values_in))
    df = pd.DataFrame(values_in)
    print(type(df))
    filename = "test.csv"  # uses current path
    df.to_csv(filename, index=False)  # creates a csv file from a dataframe

    data_in_file = pd.read_csv(filename, index_col=None)
    print(type(data_in_file))
    output = data_in_file.values.tolist()
    print(type(output))
    print(output)
    print(output == [[1], [2], [3], [4], [5]])


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

    print("That's all, Folks!")


if __name__ == "__main__":
    main()
