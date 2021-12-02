"""Testing the functions of the Filehandling class - using ARRANGE, ACT, ASSERT"""
import pytest
import pandas as pd
import os
import shutil
import time
from filehandling.filehandling import Filehandling


# assign the filepath ./tests/ as the test file path for test-file.csv
current_working_directory = os.getcwd()
test_path = current_working_directory + "/tests/"
test_file = "test-file.csv"
testfilepath = test_path + test_file
# assign test dataframe
test_values = [1, 2, 3, 4, 5]
test_value_string = "1, 2, 3, 4, 5"


@pytest.fixture
def delete_existing_test_file_fixture():
    """ This FIXTURE will delete testfile in tests/ directory - it runs each time it is passed to a test """
    if os.path.exists(testfilepath) and os.path.isfile(testfilepath):
        os.remove(testfilepath)


@pytest.fixture
def make_test_file_fixture(delete_existing_test_file_fixture):
    """ This FIXTURE will create a test csv file in tests/ directory - it runs each time it is passed to a test """
    fileobject = Filehandling.open_file(testfilepath)
    Filehandling.write_to_file(fileobject, test_value_string)
    Filehandling.close_file(fileobject)


def test_current_directory_path():
    """ test for current working directory"""
    assert Filehandling.current_directory_path() == current_working_directory


def test_make_input_directory():
    """ test input directory"""
    assert Filehandling.make_input_directory() == current_working_directory + "/input/"


def test_make_output_directory():
    """ test output directory"""
    assert Filehandling.make_output_directory() == current_working_directory + "/output/"


def test_get_timestamp():
    """ Test UNIX timestamp"""
    assert Filehandling.get_timestamp() == round(time.time())


def test_append_timestamp_to_filename():
    """ Test append timestamp to filename"""
    newfilename = Filehandling.append_timestamp_to_filename(test_file)
    assert newfilename == "test-file_output-" + str(round(time.time())) + ".csv"


def test_open_file(make_test_file_fixture):
    """ Test to open file in specified test path"""
    try:
        fileobject = Filehandling.open_file(testfilepath)
    except IOError:
        raise
    fileobject.close()
    assert True


def test_close_file(make_test_file_fixture):
    """ Close designated file"""
    try:
        fileobject = open(testfilepath, 'a')
    except IOError:
        raise
    assert Filehandling.close_file(fileobject) is True


def test_write_to_file(delete_existing_test_file_fixture):
    """ Test write additional content to designated file"""
    try:
        fileobject = open(testfilepath, 'w')
    except IOError:
        raise
    Filehandling.write_to_file(fileobject, test_value_string)
    fileobject.close()
    fileobject = open(testfilepath, 'r')
    read_data = fileobject.readline()
    fileobject.close()
    assert read_data == "1, 2, 3, 4, 5"


def test_log_entry(make_test_file_fixture):
    """ Tests entry into the designated test file"""
    message = "Test log entry"
    Filehandling.log_entry(testfilepath, message)
    with open(testfilepath, "r") as file:
        for line in file:
            pass
    assert line == test_value_string + str(round(time.time())) + ", " + message + "\n"


def test_write_df_to_output_file(delete_existing_test_file_fixture):
    """ Test pandas write dataframe to csv file in test folder"""
    df_test = pd.DataFrame(test_values)
    Filehandling.write_df_to_output_file(testfilepath, df_test)
    test_file_data = pd.read_csv(testfilepath, index_col=0)
    output = test_file_data.values.tolist()
    assert output == [[1], [2], [3], [4], [5]]


def test_retrieve_df_from_file(delete_existing_test_file_fixture):
    """ Test pandas read dataframe from csv file"""
    df_test = pd.DataFrame(test_values)
    Filehandling.write_df_to_output_file(testfilepath, df_test)
    inputpath = current_working_directory + "/input/"
    shutil.move(testfilepath, inputpath)
    df = Filehandling.retrieve_df_from_file(test_file)
    output = df.values.tolist()
    inputfilepath = inputpath + test_file
    os.remove(inputfilepath)
    assert output == [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]


