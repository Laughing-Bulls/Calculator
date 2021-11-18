""" This is a script to run a user test of the Python calculator"""
from filehandling.filehandling import Filehandling
import os
import pandas as pd
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


def main():
    """ User test of the calculator program"""

    print("Calculator program is running. Monitoring for new input files to calculate...")
    # print current working directory
    print(os.getcwd())

    data = Filehandling.read_line_from_file("input_test.csv")
    data.head()

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
