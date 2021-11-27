"""Testing the functions of the Filehandling class - using ARRANGE, ACT, ASSERT"""
import pytest
import pandas as pd
import os
# import pprint: allows print during test


@pytest.fixture
def open_file_fixture():
    """ This FIXTURE will clear the history cache - it runs each time it is passed to a test """
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


@pytest.fixture
def assign_file_path_fixture():
    """ This FIXTURE will assign the current filepath as the test file path """
    current_path = os.getcwd()

@pytest.fixture
def put_data_into_file_fixture():
    """ This FIXTURE will make a file with data - it runs each time it is passed to a test """
    values_in = [1, 2, 3, 4, 5]     # assign a series of numbers
    df = pd.DataFrame(values_in)    # makes into a pandas dataframe
    filename = "test.csv"           # uses current path
    df.to_csv(filename, index=False)             # creates a csv file from the dataframe

def test_read_from_file(put_data_into_file_fixture):
    """ Read test file and check values"""
    filename = "test.csv"
    data_in_file = pd.read_csv(filename, index_col=None)
    output = data_in_file.values.tolist()
    assert output == [[1], [2], [3], [4], [5]]

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
        # arguments include (filepath,
        # df = pd.read_csv("https://sample.com/test.csv", sep="\t")
        # iterator: if TRUE, returns text file reader object for iteration
        # on_bad_lines parameter for error handling
        # nrows = number of lines to read, useful for large files
        # can cycle through the lines and values with range(n) where n = array length
        # pd.DataFrame(df,
        # df.iloc[integer] select row by integer location
        input = pd.read_csv(filename, index_col=0)
        data = pd.DataFrame(input)
        assert data == (1, 2, 3, 4, 5)

    def write_line_to_file_test(pathname, filename, df):
        """ Write entry in file"""
        # first argument is path_or_buf: only required field; if a file object, it must be opened with: newline=''
        # header: default is true for column index names
        # index: default is true for row index names
        # chunksize: number of rows to write at a time
        # by default, columns get inserted at the end: df.insert(values)
        # assign method will create a new column to the dataframe: df.assign(math_function). It returns a COPY of the data
        pd.to_csv(pathname, filename, df) # creates a csv file from a dataframe
        return True

    def close_file_test(filename):
        """ Add all the elements of the tuple"""
        pass

