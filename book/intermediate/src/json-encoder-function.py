import datetime
import json


DATA = {"datetime": datetime.datetime(1961, 4, 12, 2, 7, 0, 123456)}


def encoder(self, obj):

    if isinstance(obj, datetime.datetime):
        return f'{obj:%Y-%m-%dT%H:%M:%S.%fZ}'

    elif isinstance(obj, datetime.date):
        return f'{obj:%Y-%m-%d}'


json.JSONEncoder.default = encoder

json.dumps(DATA)
