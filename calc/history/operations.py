""" This class is for operations on data extracted from the input files and create log entries"""


class Operations:
    """ This is the class to perform operations on the data and create log entries"""

    @staticmethod
    def convert_list_to_tuple(list_to_convert):
        """ Convert a list into a tuple to perform operations"""
        return tuple(list_to_convert)

    @staticmethod
    def convert_df_to_array(df_in):
        """ Convert a dataframe into an array"""
        return df_in.values

    @staticmethod
    def add_answer_column_to_df(df_in, answers):
        """ Add the answer column as last column of input df"""
        df_out = df_in.assign(answers=answers)
        return df_out

    @staticmethod
    def create_a_log_entry(filename, record_nm, operation, result):
        """ Create an entry for the logfile or the exception file"""
        entry = filename + ", Record #" + str(record_nm + 1) + ", " + operation + ", " + str(result)
        return entry

    @staticmethod
    def create_a_history_entry(tuple_in, operation, result):
        """ Create an entry for the calculation history file"""
        if len(tuple_in) == 2:
            third = ""
        else:
            third = str(tuple_in[2])
        entry = str(tuple_in[0]) + ", " + str(tuple_in[1]) + ", " + third + ", " + operation \
            + ", " + result
        return entry
