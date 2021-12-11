"""Testing the functions of the FileOps class - using ARRANGE, ACT, ASSERT"""
# pylint: disable=import-error,no-name-in-module
from filehandling.fileops import Fileops


def test_determine_operation_from_filename():
    """ Tests the selection of operation from the filename, returned as a string"""
    filename = "001-multiplication-test-input-file.csv"
    assert Fileops.determine_operation_from_filename(filename) == "multiplication"
