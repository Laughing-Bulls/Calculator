""" This class is for operations on the input files"""
# Use Pandas library with alias pd for file actions
import pandas as pd


class Operations:
    """ This is the class to perform operations on the files"""

    @staticmethod
    def get_tuple_from_row():
        """ Turns the dataframe row into tuples """
        # iterate through each row and select
        # 'Name' and 'Stream' column respectively.
        # for ind in df.index:
        #   print(df['Name'][ind], df['Stream'][ind])
        """ alternate"""
        # iterate through each row and select
        # 'Name' and 'Age' column respectively.
        # for i in range(len(df)):
        #   print(df.loc[i, "Name"], df.loc[i, "Age"])
        """ 2 alternative"""
        # iterate through each row and select
        # 0th and 2nd index column respectively.
        # for i in range(len(df)):
        #   print(df.iloc[i, 0], df.iloc[i, 2])
        pass

    @staticmethod
    def perform_operation():
        """ perform designated operation"""
        # to add new column at front: df.insert(0, 'Sum', range(0, len(df)))
        pass

    @staticmethod
    def create_a_log_entry(record_num, operation, result):
        """ Create an entry for the logfile with the record number, operation, and result of the calculation"""
        entry = ", Record #" + str(record_num + 1) + ", " + operation + ", " + str(result)
        return entry

    @staticmethod
    def convert_list_to_tuple(list):
        """ Convert a list into a tuple to perform operations"""
        return tuple(list)

    @staticmethod
    def convert_df_to_array(df):
        """ Convert a list into a tuple to perform operations"""
        return df.values

    @staticmethod
    def add_answer_column_to_df(df, answers):
        """ Add answer column as last column of input df"""
        df1 = df.assign(answers=answers)
        return df1

    @staticmethod
    def create_error_log_entry():
        """Write log file for exceptions such as divide by zero with a record number and filename"""
        pass
