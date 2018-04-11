import datetime
import json


DATA = {
    "astronaut": {
        "date": datetime.date(1923, 11, 18),
        "person": "jose.jimenez@nasa.gov"
    },
    "flight": [
        {"datetime": datetime.datetime(1961, 5, 5, 14, 34, 13), "action": "launch"},
        {"datetime": datetime.datetime(1961, 5, 5, 14, 49, 35), "action": "landing"}
    ]
}



# Sposob 1
json.JSONEncoder.default = lambda self, obj: (f'{obj:%Y-%m-%dT%H:%M:%S.%fZ}' if isinstance(obj, datetime.datetime) else None)

out = json.dumps(DATA)
print(out)


# Sposob 2
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