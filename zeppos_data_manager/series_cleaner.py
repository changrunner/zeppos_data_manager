import pandas as pd


class SeriesCleaner:
    @staticmethod
    def get_hours_only(series):
        if type(series) is pd.core.series.Series:
            series = (series / 3600)
            series = series.astype(int)
            return series
        return None

    @staticmethod
    def get_minutes_only(series):
        if type(series) is pd.core.series.Series:
            series_hours_in_seconds = SeriesCleaner.get_hours_only(series) * 3600
            series = ((series - series_hours_in_seconds) / 60)
            series = series.astype(int)
            return series
        return None

    @staticmethod
    def get_seconds_only(series):
        if type(series) is pd.core.series.Series:
            series_hours_in_seconds = SeriesCleaner.get_hours_only(series) * 3600
            series_minutes_in_seconds = SeriesCleaner.get_minutes_only(series) * 60
            series = (series - series_hours_in_seconds - series_minutes_in_seconds)
            series = series.astype(int)
            return series
        return None

    @staticmethod
    def get_date(series, date_format='%m/%d/%Y %I:%M %p'):
        if type(series) is pd.core.series.Series:
            series = series.fillna('')
            series = series.astype(str)
            series = series.str.replace('EDT', '')
            series = series.str.replace('EST', '')
            series = series.str.replace('CDT', '')
            series = series.str.replace('CST', '')
            series = series.str.replace('MDT', '')
            series = series.str.replace('ARIZ', '')
            series = series.str.replace('MST', '')
            series = series.str.replace('PDT', '')
            series = series.str.replace('PST', '')
            series = series.str.strip()
            series = pd.to_datetime(series, format=date_format, errors='coerce')
            return series
        return None

