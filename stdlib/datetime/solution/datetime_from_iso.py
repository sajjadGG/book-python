from datetime import datetime


INPUT = '1969-07-21T02:56:15.123Z'
format = '%Y-%m-%dT%H:%M:%S.%fZ'

OUTPUT = datetime.strptime(INPUT, format)
print(OUTPUT)
