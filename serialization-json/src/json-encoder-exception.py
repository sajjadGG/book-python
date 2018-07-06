import datetime
import json

DATA = {"datetime": datetime.datetime(1961, 4, 12, 2, 7, 0, 123456)}

json.dumps(DATA)
# Traceback (most recent call last):
#   ...
# TypeError: Object of type 'datetime' is not JSON serializable