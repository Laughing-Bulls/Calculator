"""Testing the functions of the Filehandling class - using ARRANGE, ACT, ASSERT"""
import os
import shutil
import time
import pytest
import pandas as pd
from filehandling.filehandling import Filehandling


# assign the filepath ./tests/ as the test file path for test-file.csv
current_working_directory = os.getcwd()
test_path = current_working_directory + "/tests/"
TEST_FILE = "test-file.csv"
testfilepath = test_path + TEST_FILE
# assign test dataframe
test_values = [1, 2, 3, 4, 5]
TEST_VALUE_STRING = "1, 2, 3, 4, 5"


@pytest.fixture
def delete_existing_test_file_fixture():
    """ This FIXTURE deletes testfile in tests/ directory - runs when passed to a test"""
    # pylint: disable=redefined-outer-name
    if os.path.exists(testfilepath) and os.path.isfile(testfilepath):
        os.remove(testfilepath)


@pytest.fixture
def make_test_file_fixture(delete_existing_test_file_fixture):
    """ This FIXTURE creates a test csv file in tests/ directory - runs when passed to a test"""
    # pylint: disable=redefined-outer-name,unused-argument
    fileobject = Filehandling.open_file(testfilepath)
    Filehandling.write_to_file(fileobject, TEST_VALUE_STRING)
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
    newfilename = Filehandling.append_timestamp_to_filename(TEST_FILE)
    assert newfilename == "test-file_output-" + str(round(time.time())) + ".csv"


def test_open_file(make_test_file_fixture):
    """ Test to open file in specified test path"""
    # pylint: disable=redefined-outer-name,unused-argument
    fileobject = Filehandling.open_file(testfilepath)
    fileobject.close()
    assert True


def test_close_file(make_test_file_fixture):
    """ Close designated file"""
    # pylint: disable=redefined-outer-name,unused-argument,unspecified-encoding,consider-using-with
    fileobject = open(testfilepath, 'a')
    assert Filehandling.close_file(fileobject) is True


def test_write_to_file(delete_existing_test_file_fixture):
    """ Test write additional content to designated file"""
    # pylint: disable=redefined-outer-name,unused-argument
    with open(testfilepath, 'w', encoding="utf8") as fileobject:
        Filehandling.write_to_file(fileobject, TEST_VALUE_STRING)
    with open(testfilepath, 'r', encoding="utf8") as fileobject:
        read_data = fileobject.readline()
    assert read_data == "1, 2, 3, 4, 5"


def test_log_entry(delete_existing_test_file_fixture):
    """ Tests entry into the designated test file"""
    # pylint: disable=redefined-outer-name,unused-argument
    message = "Test log entry"
    Filehandling.log_entry(testfilepath, message)
    with open(testfilepath, "r", encoding="utf8") as fileobject:
        read_data = fileobject.readline()
    assert read_data == str(round(time.time())) + ", " + message + "\n"


def test_write_df_to_output_file(delete_existing_test_file_fixture):
    """ Test pandas write dataframe to csv file in test folder"""
    # pylint: disable=redefined-outer-name,unused-argument
    df_test = pd.DataFrame(test_values)
    Filehandling.write_df_to_output_file(testfilepath, df_test)
    test_file_data = pd.read_csv(testfilepath, index_col=0)
    output = test_file_data.values.tolist()
    assert output == [[1], [2], [3], [4], [5]]


def test_retrieve_df_from_file(delete_existing_test_file_fixture):
    """ Test pandas read dataframe from csv file"""
    # pylint: disable=redefined-outer-name,unused-argument
    df_test = pd.DataFrame(test_values)
    Filehandling.write_df_to_output_file(testfilepath, df_test)
    inputpath = current_working_directory + "/input/"
    shutil.move(testfilepath, inputpath)
    df_out = Filehandling.retrieve_df_from_file(TEST_FILE)
    output = df_out.values.tolist()
    inputfilepath = inputpath + TEST_FILE
    os.remove(inputfilepath)
    assert output == [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
