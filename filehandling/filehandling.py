""" This class contains all the filehandling methods. Directories will be 'input/' and 'output/' """
import os
import time
# Use Pandas library with alias pd for file actions
import pandas as pd


class Filehandling:
    """ Contains all the filehandling methods"""

    @staticmethod
    def current_directory_path():
        """ get current working directory and make it a string"""
        return os.getcwd()

    @staticmethod
    def make_input_directory():
        """ get current working directory and add input directory"""
        # add "input" to get_directory_path()
        return Filehandling.current_directory_path() + "/input/"

    @staticmethod
    def make_output_directory():
        """ get current working directory and add output directory"""
        # add "output" to get_directory_path()
        return Filehandling.current_directory_path() + "/output/"

    @staticmethod
    def get_timestamp():
        """ Get UNIX timestamp"""
        return round(time.time())

    @staticmethod
    def append_timestamp_to_filename(filename):
        """ Append timestamp to filename"""
        newfilename = filename.split(".")
        return newfilename[0] + "_output-" + str(Filehandling.get_timestamp()) + ".csv"

    @staticmethod
    def make_log_entry(filename, entry):
        """ Write log file in output folder with unix time stamp, input filename, record number, operation, result"""
        filepath = Filehandling.make_output_directory() + "logfile.csv"
        fileobject = open(filepath, 'a')
        log_entry = str(Filehandling.get_timestamp()) + ", " + filename + entry + '\n'
        fileobject.write(log_entry)
        Filehandling.close_file(fileobject)
        return True

    @staticmethod
    def make_exception_log_entry(filename, record_num, error):
        """ Write log file for exceptions such as divide by zero with a record number and filename"""
        filepath = Filehandling.make_output_directory() + "errorlog.csv"
        fileobject = open(filepath, 'a')
        error_log_entry = str(Filehandling.get_timestamp()) + ", " + filename + ", Record #" + str(
            record_num + 1) + error + '\n'
        fileobject.write(error_log_entry)
        Filehandling.close_file(fileobject)
        return True

    @staticmethod
    def retrieve_df_from_file(filename):
        """ Read data from file and return it"""
        filestring = Filehandling.make_input_directory() + filename
        df = pd.read_csv(filestring, index_col=None)
        return df

    @staticmethod
    def write_df_to_output_file(pathname, df):
        """ Write dataframe to csv file in output folder"""
        df.to_csv(pathname)
        return True

    @staticmethod
    def open_file(filename):
        """ Open file in specified path"""
        pass

    @staticmethod
    def close_file(fileobject):
        """ Close designated file"""
        fileobject.close()
        return True
