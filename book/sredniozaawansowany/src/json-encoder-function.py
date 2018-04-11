import datetime
import json


DATA = {"datetime": datetime.datetime(1961, 4, 12, 2, 7, 0, 123456)}


def datetime_encoder(self, obj):
    if isinstance(obj, datetime.datetime):
        # return obj.isoformat()
        return f'{obj:%Y-%m-%dT%H:%M:%S.%fZ}'
    elif isinstance(obj, datetime.date):
        return f'{obj:%Y-%m-%d}'
    else:
        return None

json.JSONEncoder.default = datetime_encoder

out = json.dumps(DATA)
print(out)
