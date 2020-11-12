import unittest
from zeppos_data_manager.data_enricher import DataEnricher
from tzwhere import tzwhere
from datetime import datetime


class TestTheProjectMethods(unittest.TestCase):
    def test_get_time_zone_from_location_method(self):
        self.assertEqual(DataEnricher.get_time_zone_from_location(tzwhere.tzwhere(), "40.732525,-74.105650"), "America/New_York")

    def test_convert_time_zone_method(self):
        self.assertEqual(DataEnricher.convert_time_zone('01/01/2020 01:00:00 PM', 'America/New_York'),
                         datetime.strptime('2020-01-01 08:00:00', '%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    unittest.main()