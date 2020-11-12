import unittest
from zeppos_data_manager.data_cleaner import DataCleaner
from datetime import datetime


class TestTheProjectMethods(unittest.TestCase):
    def test_to_date_method(self):
        self.assertEqual(DataCleaner.to_date('01/01/2020'), datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))

    def test_to_numeric_method(self):
        self.assertEqual(DataCleaner.to_numeric('0'), 0)

    def test_to_string_method(self):
        self.assertEqual(DataCleaner.to_string(0), '0')

    def test_is_numeric_method(self):
        self.assertEqual(DataCleaner.is_numeric(1), True)
        self.assertEqual(DataCleaner.is_numeric("1"), True)
        self.assertEqual(DataCleaner.is_numeric(1.0), True)
        self.assertEqual(DataCleaner.is_numeric("1.0"), True)
        self.assertEqual(DataCleaner.is_numeric("nan"), False)
        self.assertEqual(DataCleaner.is_numeric("a"), False)
        self.assertEqual(DataCleaner.is_numeric(None), False)

    def test_is_integer_method(self):
        self.assertEqual(DataCleaner.is_integer(1), True)
        self.assertEqual(DataCleaner.is_integer(1.0), False)
        self.assertEqual(DataCleaner.is_integer(1.1), False)
        self.assertEqual(DataCleaner.is_integer("1"), True)
        self.assertEqual(DataCleaner.is_integer("1.0"), False)
        self.assertEqual(DataCleaner.is_integer("1.1"), False)
        self.assertEqual(DataCleaner.is_integer(None), False)

    def test_is_decimal_method(self):
        self.assertEqual(DataCleaner.is_decimal(1.1), True)
        self.assertEqual(DataCleaner.is_decimal(1.0), True)
        self.assertEqual(DataCleaner.is_decimal("1.1"), True)
        self.assertEqual(DataCleaner.is_decimal("1.0"), True)
        self.assertEqual(DataCleaner.is_decimal("1"), False)
        self.assertEqual(DataCleaner.is_decimal(1), False)
        self.assertEqual(DataCleaner.is_decimal("a.1"), False)

    def test_is_alpha_only_method(self):
        self.assertEqual(DataCleaner.is_alpha_only("test"), True)
        self.assertEqual(DataCleaner.is_alpha_only(""), False)
        self.assertEqual(DataCleaner.is_alpha_only(None), False)
        self.assertEqual(DataCleaner.is_alpha_only(1), False)
        self.assertEqual(DataCleaner.is_alpha_only("1"), False)
        self.assertEqual(DataCleaner.is_alpha_only("test1"), False)
        self.assertEqual(DataCleaner.is_alpha_only("test test"), False)

    def test_is_nan_method(self):
        self.assertEqual(DataCleaner.is_nan(0), False)

    def test_is_date_method(self):
         self.assertEqual(DataCleaner.is_date('1/1/1900'), True)

    def test_lreplace_method(self):
        self.assertEqual(DataCleaner.lreplace("0", "_", "011"), "_11")

    def test_rreplace_method(self):
        self.assertEqual(DataCleaner.rreplace("0", "_", "110"), "11_")

    def test_drop_first_characters_method(self):
        self.assertEqual(DataCleaner.drop_first_characters("12345", 2), "345")

    def test_replace_alpha_numeric_value_only_method(self):
        self.assertEqual(DataCleaner.replace_alpha_numeric_value_only(" $231aA "), "231aA")

    def test_pad_left_method(self):
        self.assertEqual(DataCleaner.pad_left('2', '0', 2), '02')
        self.assertEqual(DataCleaner.pad_left('02', '0', 2), '02')
        self.assertEqual(DataCleaner.pad_left('002', '0', 2), '02')

    def test_get_date_format_method(self):
        self.assertEqual(DataCleaner.get_date_format('1900'), '%Y')
        self.assertEqual(DataCleaner.get_date_format('1/1/1900'), '%m/%d/%Y')
        self.assertEqual(DataCleaner.get_date_format('111900'), None)

    def test_clean_filename_method(self):
        self.assertEqual(DataCleaner.clean_filename("$my_File_123"), "_my_File_123")


if __name__ == '__main__':
    unittest.main()