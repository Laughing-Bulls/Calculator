""" This is a script to run a user test of the Python calculator"""
from filehandling.filehandling import Filehandling
from calc.history.operations import Operations
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from filehandling.filehandling import Filehandling
from filehandling.watcher import Watchdog
# pip install watchdog
# import sys
# import time
# import logging
# import os
# import pandas as pd
# import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler


def main():
    """ User test of the calculator program"""

    print("Calculator program is running. Monitoring for new input files to calculate...")

    filename = Watchdog.watch()

    # get filename, read data and put it into an array
    # filename = "subtraction_test.csv"
    df = Filehandling.retrieve_df_from_file(filename)
    vals = Operations.convert_df_to_array(df)

    print("Input file detected.")
    print(df.head())
    # print(df.tail())
    # print(df)

    # length of row = df.shape[1]
    arguments = df.shape[1] - 1
    # print(len(df))
    # df.iloc[count, 1]

    # decide operation
    defined_ops = ["addition", "subtraction", "multiplication", "division", "exponent"]
    operation = next((x for x in defined_ops if x in filename), False)
    print(operation)

    answers = []

    for i in range(len(df)):
        inputs = []
        for j in range(arguments):
            # if not null, add number to list
            if vals[i, j] is not None:
                inputs.append(vals[i, j])

        # make number a tuple and perform operation
        input_tuple = Operations.convert_list_to_tuple(inputs)
        if(operation == "addition"):
            Calculator.add_numbers(input_tuple)
        if (operation == "subtraction"):
            Calculator.subtract_numbers(input_tuple)
        if (operation == "multiplication"):
            Calculator.multiply_numbers(input_tuple)
        if (operation == "division"):
            Calculator.divide_numbers(input_tuple)
        if (operation == "exponent"):
            Calculator.power_numbers(input_tuple)
        if (operation is False):
            print("No file operation designated in input file. Error logged.")
            Filehandling.make_exception_log_entry(filename, 0)
            break

        # compile answers and add to log file
        answers.append(Calculations.get_history_result())
        Filehandling.make_log_entry(filename, Operations.create_a_log_entry(i, operation, answers[-1]))

    # add answers to new df and save in results file
    df_out = Operations.add_answer_column_to_df(df, answers)
    outfile = Filehandling.make_output_directory() + Filehandling.append_timestamp_to_filename(filename)
    print("Output is in: " + outfile)
    Filehandling.write_df_to_output_file(outfile, df_out)

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

    input("Press [ENTER] to exit program:")
    print("That's all, Folks!")


if __name__ == "__main__":
    main()
