import datetime
import json


DATA = """
{
    "astronaut":{
        "datetime":"1961-05-05T14:34:13.640Z",
        "person":"jose.jimenez@nasa.gov"
    },
    "first-flight":[
        {"datetime":"1961-05-05T14:34:13.640Z", "action":"launch"},
        {"datetime":"1961-05-05T14:49:35.640Z", "action":"landing"},
    ],
}
"""

def datetime_decoder(obj):
    for key, value in obj.items():
        if key == 'datetime':
            obj['datetime'] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
    return obj


out = json.loads(DATA, object_hook=datetime_decoder)
print(out)