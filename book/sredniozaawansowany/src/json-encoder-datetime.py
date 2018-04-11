import json


DATA = """{
    "astronaut":{
        "date": "1923-11-18",
        "person": "jose.jimenez@nasa.gov"
    },
    "flight": [
        {"datetime": "1961-05-05T14:34:13.000Z", "action": "launch"},
        {"datetime": "1961-05-05T14:49:35.000Z", "action": "landing"}
    ]
}
"""


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return f'{obj:%Y-%m-%dT%H:%M:%S.%fZ}'


json.dumps(DATA, cls=DatetimeEncoder)