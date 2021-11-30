""" This class contains all the filehandling methods. Directories will be 'input' and 'output' """
# Use Pandas library with alias pd for file actions
import pandas as pd
# pip install watchdog
import os
# import sys
import time
# import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class Filehandling:
    """ Contains all the filehandling methods"""

    # directory_path_in = "/home/myusr/input/"
    # directory_path_out = "/home/myusr/output/"

    @staticmethod
    def current_directory_path():
        """ get current working directory and make it a string"""
        return os.getcwd()

    @staticmethod
    def make_directory_path_name():
        """ get current working directory and add input directory"""
        # add "input" to get_directory_path()
        # string = "directory name" + "filename.csv"
        pass

    @staticmethod
    def make_output_directory():
        """ get current working directory and add output directory"""
        # add "input" to get_directory_path()
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
    def monitor_directory():
        """ Return an alert if file is added to the directory"""
        pass

    @staticmethod
    def open_file(filename):
        """ Open file in specified path"""
        pass

    @staticmethod
    def create_output_file(filename):
        """ Make file to hold output of calculations"""
        pass

    @staticmethod
    def make_log_entry(filename, entry):
        """ Write log file file in the output folder with a unix time stamp, filename of the input file, record number, operation, and result"""
        filepath = Filehandling.make_output_directory() + "logfile.csv"
        fileobject = open(filepath, 'a')
        log_entry = str(Filehandling.get_timestamp()) + ", " + filename + entry + '\n'
        fileobject.write(log_entry)
        Filehandling.close_file(fileobject)
        return True

    @staticmethod
    def make_exception_log_entry(filename, record_num):
        """ Write log file for exceptions such as divide by zero with a record number and filename"""
        filepath = Filehandling.make_output_directory() + "errorlog.csv"
        fileobject = open(filepath, 'a')
        error_log_entry = str(Filehandling.get_timestamp()) + ", " + filename + ", Record #" + str(
            record_num + 1) + '\n'
        fileobject.write(error_log_entry)
        Filehandling.close_file(fileobject)
        return True

    @staticmethod
    def retrieve_df_from_file(filename):
        """ Read data from file and return it"""
        # arguments include (filepath,
        # df = pd.read_csv("https://sample.com/test.csv", sep="\t")
        # iterator: if TRUE, returns text file reader object for iteration
        # on_bad_lines parameter for error handling
        # nrows = number of lines to read, useful for large files
        # can cycle through the lines and values with range(n) where n = array length
        # pd.DataFrame(df,
        # df.iloc[integer] select row by integer location
        # To select NaN entries you can use pd.isnull() or its companion pd.notnull(): reviews[pd.isnull(reviews.country)]
        filestring = Filehandling.current_directory_path() + "/input/" + filename
        df = pd.read_csv(filestring, index_col=None)
        return df

    @staticmethod
    def write_df_to_output_file(pathname, df):
        """ Write dataframe to csv file in output folder"""
        # first argument is path_or_buf: only required field; if a file object, it must be opened with: newline=''
        # header: default is true for column index names
        # index: default is true for row index names
        # chunksize: number of rows to write at a time
        # by default, columns get inserted at the end: df.insert(values)
        # assign method will create a new column to the dataframe: df.assign(math_function). It returns a COPY of the data
        # df.to_csv(filename) - creates a csv file from a dataframe
        df.to_csv(pathname)  # creates a csv file from a dataframe
        return True

    @staticmethod
    def close_file(fileobject):
        """ Close designated file"""
        fileobject.close()
        return True


"""

path

event_handler = LoggingEventHandler()

observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()            


"""
