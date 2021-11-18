""" This class contains all the filehandling methods. Directories will be 'input' and 'output' """
import pandas as pd


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
        data = pd.read_csv(filename)
        return data

    @staticmethod
    def write_line_to_file(filename, output_line):
        """ Write entry in file"""
        pass

    @staticmethod
    def close_file(filename):
        """ Add all the elements of the tuple"""
        pass
