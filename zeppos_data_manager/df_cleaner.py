import re
from zeppos_data_manager.data_cleaner import DataCleaner
import pandas as pd
import numpy as np

class DfCleaner:
    @staticmethod
    def clean_column_names_in_place(df):
        df.rename(columns={c: re.sub('[^0-9a-zA-Z]+', '_', c).rstrip('_').upper() for c in df.columns.to_list()}, inplace=True)

    @staticmethod
    def rename_column_names_in_place(df, columns_to_rename_dict):
        for k, v in columns_to_rename_dict.items():
            if k in df.columns.to_list():
                df.rename(columns={k:v}, inplace=True)

    @staticmethod
    def set_columns_to_numeric(df, numeric_column_list, default_value=0):
        for column_name in numeric_column_list:
            if column_name in df.columns.tolist():
                df[column_name] = pd.to_numeric(df[column_name], errors='coerce').fillna(default_value)

    @staticmethod
    def set_columns_to_integer(df, integer_column_list, default_value=0):
        DfCleaner.set_columns_to_numeric(df, integer_column_list, default_value)
        for column_name in integer_column_list:
            if column_name in df.columns.tolist():
                df[column_name] = df[column_name].astype(int)

    @staticmethod
    def set_columns_to_string(df, string_columns):
        for column_name in string_columns:
            if column_name in df.columns.tolist():
                df[column_name] = np.where(df[column_name].isnull(), None, df[column_name])

    @staticmethod
    def set_columns_to_datetime(df, date_columns):
        for col in date_columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    @staticmethod
    def set_columns_to_date_only(df, date_columns):
        DfCleaner.set_columns_to_datetime(df, date_columns)
        for col in date_columns:
            pd.to_datetime(df[col], errors='coerce')
            df[col] = df[col].dt.date

    @staticmethod
    def set_columns_to_time_only(df, date_columns):
        DfCleaner.set_columns_to_datetime(df, date_columns)
        for col in date_columns:
            pd.to_datetime(df[col], format='%H:%M', errors='coerce')
            df[col] = df[col].dt.time

