""" This class contains all the filehandling methods. Directories will be 'input/' and 'output/' """
import os
import time
from datetime import datetime
import pandas as pd
from calc.history.operations import Operations


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
    def get_datetime():
        """ Convert UNIX timestamp to date and time"""
        time_stamp = Filehandling.get_timestamp()
        date_time = datetime.fromtimestamp(time_stamp, tz=None)
        return date_time

    @staticmethod
    def append_timestamp(filename):
        """ Append timestamp to filename"""
        newfilename = filename.split(".")
        return newfilename[0] + "_output-" + str(Filehandling.get_timestamp()) + ".csv"

    @staticmethod
    def make_log_entry(message):
        """ Entry w/ unix time stamp, input filename, record number, operation, result"""
        logfile = Filehandling.make_output_directory() + "logfile.csv"
        Filehandling.log_entry(logfile, message)
        return True

    @staticmethod
    def make_exception_log_entry(error_message):
        """ Entry for exceptions like divide by zero w/ filename and record number"""
        logfile = Filehandling.make_output_directory() + "errorlog.csv"
        Filehandling.log_entry(logfile, error_message)
        return True

    @staticmethod
    def make_history_log_entry(input_tuple, operation):
        """ Entry for exceptions like divide by zero w/ filename and record number"""
        logfile = Filehandling.make_input_directory() + "calculation-history.csv"
        entry = Operations.create_a_history_entry(input_tuple, operation)
        Filehandling.log_entry(logfile, entry)
        return True

    @staticmethod
    def log_entry(logpathfile, message):
        """ Make an entry into the designated log"""
        fileobject = Filehandling.open_file(logpathfile)
        log_line = str(Filehandling.get_datetime()) + ", " + message + '\n'
        Filehandling.write_to_file(fileobject, log_line)
        Filehandling.close_file(fileobject)
        return True

    @staticmethod
    def retrieve_df_from_file(filename):
        """ Read data from file using pandas and return it as a dataframe"""
        filestring = Filehandling.make_input_directory() + filename
        df_out = pd.read_csv(filestring, index_col=None)
        return df_out

    @staticmethod
    def write_df_to_output_file(pathname, df_in):
        """ Use pandas to write dataframe to csv file in designated file"""
        df_in.to_csv(pathname)
        return True

    @staticmethod
    def open_file(filepath):
        """ Open file in specified path"""
        # pylint: disable=try-except-raise,consider-using-with
        try:
            fileobject = open(filepath, 'a', encoding="utf8")
        except IOError:
            raise
        return fileobject

    @staticmethod
    def close_file(fileobject):
        """ Close designated file"""
        fileobject.close()
        return True

    @staticmethod
    def write_to_file(fileobject, content):
        """ Write content to designated file"""
        fileobject.write(content)
        return True
