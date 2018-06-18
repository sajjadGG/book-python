import datetime
import json


DATA = {"datetime": datetime.datetime(1961, 4, 12, 2, 7, 0, 123456)}


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return f'{obj:%Y-%m-%dT%H:%M:%S.%fZ}'


json.dumps(DATA, cls=DatetimeEncoder)
