""" This class contains all the filehandling methods. Directories will be 'input' and 'output' """
import pandas as pd
# pip install watchdog
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# Use Pandas library with alias pd for file actions


class Filehandling:
    """ Contains all the filehandling methods"""

    directory_path_in = "/home/myusr/input/"
    directory_path_out = "/home/myusr/output/"

    @staticmethod
    def monitor_directory():
        """ Return an alert if file is added to the directory"""
        pass

    @staticmethod
    def open_file(filename):
        """ Add all the elements of the tuple"""
        pass

    @staticmethod
    def create_output_file(filename):
        """ Add all the elements of the tuple"""
        pass

    @staticmethod
    def read_line_from_file(filename):
        """ Read line from file and return it"""
        # arguments include (filepath,
        # df = pd.read_csv("https://sample.com/test.csv", sep="\t")
        # iterator: if TRUE, returns text file reader object for iteration
        # on_bad_lines parameter for error handling
        # nrows = number of lines to read, useful for large files
        # can cycle through the lines and values with range(n) where n = array length
        # pd.DataFrame(df,
        # df.iloc[integer] select row by integer location
        # df.to_csv(filename) - creates a csv file from a dataframe
        input = pd.read_csv(filename, index_col=0)
        data = pd.DataFrame(input) # necessary?
        return data

    @staticmethod
    def write_line_to_file(pathname, df):
        """ Write entry in file"""
        # first argument is path_or_buf: only required field; if a file object, it must be opened with: newline=''
        # header: default is true for column index names
        # index: default is true for row index names
        # chunksize: number of rows to write at a time
        # by default, columns get inserted at the end: df.insert(values)
        # assign method will create a new column to the dataframe: df.assign(math_function). It returns a COPY of the data
        pd.to_csv(pathname, df)  # creates a csv file from a dataframe
        return True

    @staticmethod
    def close_file(filename):
        """ Add all the elements of the tuple"""
        pass

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