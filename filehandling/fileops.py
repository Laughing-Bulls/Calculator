""" This is the script that directs the program what to do with the new file"""
from calc.history.operations import Operations
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from filehandling.filehandling import Filehandling
# import pandas as pd


class Fileops:
    """ Runs calculator program on designated files"""

    @staticmethod
    def get_file_data(filename):
        # get file, read it and return data as an array
        print("Input file being processed...")
        df = Filehandling.retrieve_df_from_file(filename)
        vals = Operations.convert_df_to_array(df)
        return vals

    @staticmethod
    def determine_operation_from_filename(filename):
        # decide operation to use from the filename and return it as a string
        defined_ops = ["addition", "subtraction", "multiplication", "division", "exponent"]
        operation = next((x for x in defined_ops if x in filename), False)
        return operation

    @staticmethod
    def perform_operation_on_data(vals, operation, filename):
        # loop through array and return the results calculated using operation passed to it
        answers = []

        for i in range(vals.shape[0]):
            inputs = []
            for j in range(vals.shape[1] - 1):
                # if not null, add number to list
                if vals[i, j] is not None:
                    inputs.append(vals[i, j])

            # make number a tuple and perform operation
            input_tuple = Operations.convert_list_to_tuple(inputs)
            if (operation == "addition"):
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
                error = "No file operation designated in input file"
                print(error + ". Error logged.")
                Filehandling.make_exception_log_entry(filename, 0, error)
                return answers
            answers.append(Calculations.get_history_result())
            # log the operations as they are completed
            Filehandling.make_log_entry(filename, Operations.create_a_log_entry(i, operation, answers[-1]))
        return answers

    @staticmethod
    def add_answers_to_output_file(answers, filename):
        # add answers to new df and save in results file
        df = Filehandling.retrieve_df_from_file(filename)
        df_out = Operations.add_answer_column_to_df(df, answers)
        print(df_out.head())
        outfile = Filehandling.make_output_directory() + Filehandling.append_timestamp_to_filename(filename)
        print("Sample of output that is saved in: " + outfile)
        Filehandling.write_df_to_output_file(outfile, df_out)
        return True

    @staticmethod
    def calculate_file(filename):
        # These are the designated steps to perform on new file

        # 1. determine operation to be conducted
        operation = Fileops.determine_operation_from_filename(filename)

        # 2. read data and put it into an array
        vals = Fileops.get_file_data(filename)

        # 3. perform specified operation on input values and update log file
        answers = Fileops.perform_operation_on_data(vals, operation, filename)

        # 4. create output file with the answers
        if answers:
            Fileops.add_answers_to_output_file(answers, filename)
            print("The " + operation + " operations have been processed.")

        return True
