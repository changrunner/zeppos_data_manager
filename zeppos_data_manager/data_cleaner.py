import pandas as pd
import re
from datetime import datetime

class DataCleaner:

    @staticmethod
    def to_date(string_value):
        try:
            return pd.to_datetime(string_value)
        except:
            return None

    @staticmethod
    def to_numeric(string_value):
        try:
            return pd.to_numeric(string_value)
        except:
            return None

    @staticmethod
    def to_string(string_value, trim_right=-1):
        try:
            if string_value is None:
                return None
            if pd.isna(string_value):
                return None
            if trim_right == -1:
                return str(string_value)
            else:
                return str(string_value)[:trim_right]
        except:
            return None

    @staticmethod
    def is_numeric(string_value):
        try:
            if not string_value:
                return False
            else:
                pd.to_numeric(string_value)
            return True
        except:
            return False

    @staticmethod
    def is_integer(string_value):
        try:
            if isinstance(string_value, int):
                return True
            if isinstance(string_value, float):
                if str(string_value).count("0") > 0:
                    return False
                return string_value.is_integer()
            if isinstance(string_value, str):
                if DataCleaner.is_numeric(string_value):
                    if string_value.count(".") == 0:
                        return True
            return False
        except:
            return False

    @staticmethod
    def is_decimal(string_value):
        try:
            if isinstance(string_value, int):
                return False
            if isinstance(string_value, float):
                if str(string_value).count(".") == 1:
                    return True
                return string_value.is_integer()
            if isinstance(string_value, str):
                if DataCleaner.is_numeric(string_value):
                    if string_value.count(".") == 1:
                        return True
        except:
            pass

        return False

    @staticmethod
    def is_alpha_only(string_value):
        try:
            if not string_value:
                return False

            clean_string = str(string_value).strip()
            if clean_string.lower() == "nan":
                return False
            return clean_string.isalpha()
        except:
            return False

    @staticmethod
    def is_nan(string_value):
        try:
            if pd.isna(string_value):
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def is_date(date_string,
                fmts=('%Y', '%b %d, %Y', '%b %d, %Y', '%B %d, %Y', '%B %d %Y', '%m/%d/%Y', '%m/%d/%y', '%b %Y', '%B%Y',
                      '%b %d,%Y')
                ):
        if DataCleaner.get_date_format(date_string, fmts):
            return True
        else:
            return False

    @staticmethod
    def lreplace(pattern, substitute, string_value):
        """
        Replaces 'pattern' in 'string' with 'sub' if 'pattern' starts 'string'.
        """
        return re.sub('^%s' % pattern, substitute, string_value)

    @staticmethod
    def rreplace(pattern, substitute, string_value):
        """
        Replaces 'pattern' in 'string' with 'sub' if 'pattern' ends 'string'.
        """
        return re.sub('%s$' % pattern, substitute, string_value)

    @staticmethod
    def drop_first_characters(string_value, drop_count=1, strip_character="0"):
        return string_value[((drop_count + 1) * -1):].lstrip(strip_character)

    @staticmethod
    def replace_alpha_numeric_value_only(string_value, substitute=""):
        x = re.sub('[^0-9a-zA-Z]+', substitute, string_value)
        x = DataCleaner.lreplace(substitute, '', x)
        x = DataCleaner.rreplace(substitute, '', x)
        return x

    @staticmethod
    def pad_left(string_value, pad_character, length):
        return f'{(pad_character * length)}{string_value}'[length * -1:]

    @staticmethod
    def get_date_format(date_string,
                        fmts=('%Y', '%b %d, %Y', '%b %d, %Y', '%B %d, %Y', '%B %d %Y', '%m/%d/%Y', '%m/%d/%y', '%b %Y',
                              '%B%Y', '%b %d,%Y')):
        for fmt in fmts:
            try:
                t = datetime.strptime(date_string, fmt)
                return fmt
            except:
                pass  # Keep going if an error happens on the format. Will return None if no format was found

        return None

    @staticmethod
    def clean_filename(filename):
        return re.sub('[^0-9a-zA-Z]+', '_', filename.strip())
