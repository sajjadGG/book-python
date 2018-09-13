from datetime import datetime, date
import json


DATA = {
    'first_name': 'Ivan',
    'last_name': 'Иванович',
    'datetime': datetime(1961, 4, 12, 2, 7, 0, 123456),
    'date': date(1969, 7, 21),
}


class DatetimeEncoder(json.JSONEncoder):
    def default(self, value):

        if isinstance(value, datetime):
            return f'{value:%Y-%m-%dT%H:%M:%S.%fZ}'

        elif isinstance(value, date):
            return f'{value:%Y-%m-%d}'


out = json.dumps(DATA, cls=DatetimeEncoder)
print(out)
# {
#   "first_name": "Ivan",
#   "last_name": "\u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447",
#   "datetime": "1961-04-12T02:07:00.123456Z",
#   "date": "1969-07-21"
# }
