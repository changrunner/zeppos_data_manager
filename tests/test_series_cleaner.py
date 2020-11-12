import unittest
from zeppos_data_manager.series_cleaner import SeriesCleaner
import pandas as pd
from datetime import datetime
import time

class TestTheProjectMethods(unittest.TestCase):
    def test_get_hours_only_method(self):
        self.assertEqual(SeriesCleaner.get_hours_only(None), None)
        self.assertEqual(
            SeriesCleaner.get_hours_only(pd.DataFrame({'seconds': [3600]}, columns=['seconds'])['seconds']).to_list(),
            pd.DataFrame({'seconds': [1]}, columns=['seconds'])['seconds'].to_list())
        self.assertEqual(
            SeriesCleaner.get_hours_only(pd.DataFrame({'seconds': [4000]}, columns=['seconds'])['seconds']).to_list(),
            pd.DataFrame({'seconds': [1]}, columns=['seconds'])['seconds'].to_list())
        self.assertEqual(
            SeriesCleaner.get_hours_only(pd.DataFrame({'seconds': [100]}, columns=['seconds'])['seconds']).to_list(),
            pd.DataFrame({'seconds': [0]}, columns=['seconds'])['seconds'].to_list())

    def test_get_minutes_only_method(self):
        self.assertEqual(SeriesCleaner.get_minutes_only(None), None)
        self.assertEqual(
            SeriesCleaner.get_minutes_only(pd.DataFrame({'seconds': [600]}, columns=['seconds'])['seconds']).to_list(),
            pd.DataFrame({'seconds': [10]}, columns=['seconds'])['seconds'].to_list())

    def test_get_seconds_only_method(self):
        self.assertEqual(SeriesCleaner.get_seconds_only(None), None)
        self.assertEqual(
            SeriesCleaner.get_seconds_only(pd.DataFrame({'seconds': [50]}, columns=['seconds'])['seconds']).to_list(),
            pd.DataFrame({'seconds': [50]}, columns=['seconds'])['seconds'].to_list())

    def test_get_date_method(self):
        self.assertEqual(SeriesCleaner.get_date(None), None)
        self.assertEqual(SeriesCleaner.get_date(
            series=pd.DataFrame({'date': ['01/01/2020 01:00:00 PM']}, columns=['date'])['date'],
            date_format='%m/%d/%Y %I:%M:%S %p').to_list()[0],
            datetime.strptime('2020-01-01 13:00:00', '%Y-%m-%d %H:%M:%S')
                         )
        self.assertEqual(SeriesCleaner.get_date(
            series=pd.DataFrame({'date': ['01/01/2020 01:00:00 PM EDT']}, columns=['date'])['date'],
            date_format='%m/%d/%Y %I:%M:%S %p').to_list()[0],
            datetime.strptime('2020-01-01 13:00:00', '%Y-%m-%d %H:%M:%S')
                         )


if __name__ == '__main__':
    unittest.main()
