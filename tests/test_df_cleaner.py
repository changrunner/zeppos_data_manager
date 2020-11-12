import unittest
from zeppos_data_manager.df_cleaner import DfCleaner
import pandas as pd


class TestTheProjectMethods(unittest.TestCase):
    def test_clean_column_names_in_place_method(self):
        DfCleaner.clean_column_names_in_place(pd.DataFrame({'seconds': [3600]}, columns=['seconds']))

    def test_rename_column_names_in_place_method(self):
        DfCleaner.rename_column_names_in_place(pd.DataFrame({'seconds': [3600]}, columns=['seconds']),
                                               {'seconds': 'sec'})

    def test_set_columns_to_numeric_method(self):
        DfCleaner.set_columns_to_numeric(pd.DataFrame({'seconds': ['3600']}, columns=['seconds']),
                                         ['seconds'])

    def test_set_columns_to_integer_method(self):
        DfCleaner.set_columns_to_integer(pd.DataFrame({'seconds': ['3600']}, columns=['seconds']),
                                         ['seconds'])

    def test_set_columns_to_string_method(self):
        DfCleaner.set_columns_to_string(pd.DataFrame({'seconds': ['3600']}, columns=['seconds']),
                                         ['seconds'])

    def test_set_columns_to_datetime_method(self):
        DfCleaner.set_columns_to_datetime(pd.DataFrame({'seconds': ['1/1/2020 01:00:00']}, columns=['seconds']),
                                         ['seconds'])

    def test_set_columns_to_date_only_method(self):
        DfCleaner.set_columns_to_date_only(pd.DataFrame({'seconds': ['1/1/2020 01:00:00']}, columns=['seconds']),
                                         ['seconds'])

    def test_set_columns_to_time_only_method(self):
        DfCleaner.set_columns_to_time_only(pd.DataFrame({'seconds': ['1/1/2020 01:00:00']}, columns=['seconds']),
                                         ['seconds'])


if __name__ == '__main__':
    unittest.main()
