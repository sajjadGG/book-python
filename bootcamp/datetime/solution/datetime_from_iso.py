from datetime import datetime


DATA = '1969-07-21T02:56:15.123Z'
format = '%Y-%m-%dT%H:%M:%S.%fZ'

output = datetime.strptime(DATA, format)
print(output)
