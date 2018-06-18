import datetime
import json


DATA = {"datetime": datetime.datetime(1961, 4, 12, 2, 7, 0, 123456)}


json.JSONEncoder.default = lambda self, obj: (f'{obj:%Y-%m-%dT%H:%M:%S.%fZ}' if isinstance(obj, datetime.datetime) else None)

out = json.dumps(DATA)
print(out)
# '{"now": "1961-04-12T02:07:00.123456Z"}'
