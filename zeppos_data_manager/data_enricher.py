import pytz
from datetime import datetime


class DataEnricher:
    @staticmethod
    def get_time_zone_from_location(tzwhere, location):
        # You want to pass the tzwhere as tzwhere.tzwhere() with import tzwhere from tzwhere
        # because the creation of the tzwhere object is expensive.
        try:
            location_array = location.split(',')
            return tzwhere.tzNameAt(float(location_array[0]), float(location_array[1]))
        except:
            return None

    @staticmethod
    def convert_time_zone(utc_event_time, time_zone_str, date_format='%m/%d/%Y %I:%M:%S %p'):
        try:
            timezone = pytz.timezone(time_zone_str)
            dt = datetime.strptime(utc_event_time, date_format)
            return dt + timezone.utcoffset(dt)
        except:
            return None