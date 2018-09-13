from datetime import datetime, date
import json


DATA = {
    "datetime": datetime(1961, 4, 12, 2, 7, 0, 123456),
    "date": date(1969, 7, 21),
    "name": "Jose Jimenez",
}


def encoder(self, value):
    if isinstance(value, datetime):
        return f'{value:%Y-%m-%dT%H:%M:%S.%fZ}'

    elif isinstance(value, date):
        return f'{value:%Y-%m-%d}'


json.JSONEncoder.default = encoder
out = json.dumps(DATA)

print(out)
