"""Testing the functions of the Operations class - using ARRANGE, ACT, ASSERT"""
import pandas as pd
import numpy as np
from calc.history.operations import Operations


# test data
test_list = [1, 2, 3, 4, 5]
test_df = pd.DataFrame(test_list)


def test_convert_list_to_tuple():
    """ Tests conversion of a list into a tuple"""
    test_tuple = Operations.convert_list_to_tuple(test_list)
    assert test_tuple == (1, 2, 3, 4, 5)


def test_convert_df_to_array():
    """ Tests conversion of a dataframe into an array"""
    test_array = Operations.convert_df_to_array(test_df)
    assert test_array.tolist() == [[1], [2], [3], [4], [5]]


def test_add_answer_column_to_df():
    """ Tests the addition of a column to test df"""
    new_df = Operations.add_answer_column_to_df(test_df, test_list)
    new_array = new_df.values
    assert (np.transpose(new_array) == np.array([(1, 2, 3, 4, 5), (1, 2, 3, 4, 5)])).all


def test_create_a_log_entry():
    """ Tests creation of an entry for the logfile"""
    test_entry = Operations.create_a_log_entry("filename.csv", 11, "addition", 13)
    assert test_entry == "filename.csv, Record #12, addition, 13"