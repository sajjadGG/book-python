import datetime
import json


DATA = """
{
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


def decoder(obj):
    for key, value in obj.items():

        if key == 'datetime':
            obj['datetime'] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')

        elif key == 'date':
            obj['date'] = datetime.datetime.strptime(value, '%Y-%m-%d').date()

        else:
            return obj


output = json.loads(DATA, object_hook=decoder)
print(output)
