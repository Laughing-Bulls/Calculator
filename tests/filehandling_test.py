"""Testing the functions of the Filehandling class - using ARRANGE, ACT, ASSERT"""
import pytest
import pandas
# import pprint: allows print during test


@pytest.fixture
def open_file_fixture():
    """ This FIXTURE will clear the history cache - it runs each time it is passed to a test """
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


    def monitor_directory_test():
        """ Return an alert if file is added to the directory"""
        pass

    def open_file_test(filename):
        """ Add all the elements of the tuple"""
        pass

    def create_output_file_test(filename):
        """ Add all the elements of the tuple"""
        pass

    def read_line_from_file_test(filename):
        """ Read line from file and return it"""
        data = pd.read_csv(filename, index_col=0)
        return data

    def write_line_to_file_test(filename, output_line):
        """ Write entry in file"""
        # df.to_csv(filename) - creates a csv file from a dataframe
        pass

    def close_file_test(filename):
        """ Add all the elements of the tuple"""
        pass

