import datetime
import json


DATA = """{
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


class DatetimeDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.convert_datetime)

    def convert_datetime(slef, args):
        for key, value in args.items():
            if key == 'datetime':
                args[key] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
        return args


out = json.loads(DATA, cls=DatetimeDecoder)
print(out)


# Alternatywnie

def datetime_decoder(obj):
    for key, value in obj.items():
        if key == 'datetime':
            obj[key] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
    return obj


out = json.loads(DATA, object_hook=datetime_decoder)
print(out)