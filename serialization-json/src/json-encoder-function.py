from datetime import datetime, date
import json


DATA = {
    "datetime": datetime(1961, 4, 12, 2, 7, 0, 123456),
    "date": date.today(),
    "name": "Jose Jimenez",
}


def encoder(self, obj):
    if isinstance(obj, datetime):
        return f'{obj:%Y-%m-%dT%H:%M:%S.%fZ}'
    elif isinstance(obj, date):
        return f'{obj:%Y-%m-%d}'


json.JSONEncoder.default = encoder
out = json.dumps(DATA)

print(out)
