""" This class is for operations on data extracted from the input files and create log entries"""
# Use Pandas library with alias pd for file actions
# import pandas as pd


class Operations:
    """ This is the class to perform operations on the data and create log entries"""

    @staticmethod
    def convert_list_to_tuple(list_to_convert):
        """ Convert a list into a tuple to perform operations"""
        return tuple(list_to_convert)

    @staticmethod
    def convert_df_to_array(df):
        """ Convert a dataframe into an array"""
        return df.values

    @staticmethod
    def add_answer_column_to_df(df, answers):
        """ Add the answer column as last column of input df"""
        df1 = df.assign(answers=answers)
        return df1

    @staticmethod
    def create_a_log_entry(record_num, operation, result):
        """ Create an entry for the logfile with the record number, operation, and result of the calculation"""
        entry = ", Record #" + str(record_num + 1) + ", " + operation + ", " + str(result)
        return entry

    @staticmethod
    def create_error_log_entry():
        """Write log file for exceptions such as divide by zero with a record number and filename"""
        pass
