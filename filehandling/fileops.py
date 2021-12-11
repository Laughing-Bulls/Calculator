""" This is the script that directs the program what to do with the new file"""
# pylint: disable=import-error,no-name-in-module
from calc.history.operations import Operations
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from filehandling.filehandling import Filehandling


class Fileops:
    """ Runs calculator program on designated files"""

    @staticmethod
    def get_file_data(filename):
        """ get file, read it and return data as an array"""
        print("Input file being processed...")
        df_in = Filehandling.retrieve_df_from_file(filename)
        vals = Operations.convert_df_to_array(df_in)
        return vals

    @staticmethod
    def determine_operation_from_filename(filename):
        """ decide operation to use from the filename and return it as a string"""
        defined_ops = ["addition", "subtraction", "multiplication", "division", "average", "exponent"]
        operation = next((x for x in defined_ops if x in filename), False)
        return operation

    @staticmethod
    def perform_operation_on_data(vals, operation, filename):
        """ loop through array and return the results calculated using operation passed to it"""
        answers = []

        for i in range(vals.shape[0]):
            inputs = []
            for j in range(vals.shape[1] - 1):
                # if not null, add number to list
                if vals[i, j] is not None:
                    inputs.append(vals[i, j])

            # make number a tuple and perform operation
            input_tuple = Operations.convert_list_to_tuple(inputs)
            getattr(Calculator, operation)(input_tuple)
            calculated_result = Calculations.get_history_result()
            answers.append(calculated_result)

            # log the operations and any errors as they are completed
            entry = Operations.create_a_log_entry(filename, i, operation, answers[-1])
            Filehandling.make_log_entry(entry)
            if calculated_result is None:
                error = "Math error logged. "
                if operation == "division":
                    error += "Division by zero attempted for line"
                if operation == "exponent":
                    error += "Exponent for line generated number too large to compute"
                print(error)
                error_entry = Operations.create_a_log_entry(filename, i, error, None)
                Filehandling.make_exception_log_entry(error_entry)

        return answers

    @staticmethod
    def add_answers_to_output_file(answers, filename):
        """ add answers to new df and save in results file"""
        df_in = Filehandling.retrieve_df_from_file(filename)
        df_out = Operations.add_answer_column_to_df(df_in, answers)
        print(df_out.head())
        outfile = Filehandling.make_output_directory() + Filehandling.append_timestamp(filename)
        print("Sample of output that is saved in: " + outfile)
        Filehandling.write_df_to_output_file(outfile, df_out)
        return True

    @staticmethod
    def get_calculation_result(input_tuple, operation):
        """ perform calculation from the designated operation and return result"""
        getattr(Calculator, operation)(input_tuple)
        result = Operations.format_with_commas(Calculator.get_last_result_value())
        return result

    @staticmethod
    def calculate_history_file(filename):
        """ These are the designated steps to perform on the history file before it is rendered"""
        # 1. read data from history file and put it into a df
        df_history = Filehandling.retrieve_df_from_file(filename)
        # 2. convert it to an array
        vals = Operations.convert_df_to_array(df_history)
        # 3. perform specified operation on history values by looping through array
        answers = []
        end_column = vals.shape[1] - 1
        for i in range(vals.shape[0]):
            inputs = []
            for j in range(1, end_column):
                # if not null, add number to list
                try:
                    float(vals[i, j])
                    inputs.append(vals[i, j])
                except:
                    pass
            # make numbers a tuple and perform operation
            input_tuple = Operations.convert_list_to_tuple(inputs)
            operation = vals[i, end_column]
            answers.append(Fileops.get_calculation_result(input_tuple, operation))
        # 4. append the answers to the history df and return it
        df_answers = Operations.add_answer_column_to_df(df_history, answers)
        return df_answers

    @staticmethod
    def calculate_input_file(filename):
        """ These are the designated steps to perform on new file"""

        # 1. determine operation to be conducted
        operation = Fileops.determine_operation_from_filename(filename)
        if operation is False:
            error = "No file operation designated in input file"
            print(error + ". Error logged.")
            error_entry = Operations.create_a_log_entry(filename, 0, error, None)
            Filehandling.make_exception_log_entry(error_entry)
            return True

        # 2. read data and put it into an array
        vals = Fileops.get_file_data(filename)

        # 3. perform specified operation on input values and update log file
        answers = Fileops.perform_operation_on_data(vals, operation, filename)

        # 4. create output file with the answers
        if answers:
            Fileops.add_answers_to_output_file(answers, filename)
            print("The " + operation + " operations have been processed.")

        return True
