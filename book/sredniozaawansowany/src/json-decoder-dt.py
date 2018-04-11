import datetime
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


def make_datetime(string):
    """
    >>> make_datetime('1969-07-21T02:56:15.000Z')
    datetime.datetime(1969, 7, 21, 14, 56, 15, 000000, tzinfo=datetime.timezone.utc)
    """
    return datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%fZ').replace(
        tzinfo=datetime.timezone.utc)

def make_date(string):
    """
    >>> make_datetime('1969-07-21')
    datetime.datetime(1969, 7, 21, tzinfo=datetime.timezone.utc)
    """
    return datetime.datetime.strptime(string, '%Y-%m-%d').replace(
        tzinfo=datetime.timezone.utc)

data = json.loads(DATA)

for key, value in data.items():
    for element in value:
        if value.get('datetime'):
            value['datetime'] = make_datetime(value['datetime'])
        if value.get('date'):
            value['date'] = make_date(value['date'])
