from datetime import datetime


INPUT = '1969-07-21T02:56:15.123Z'

OUTPUT = datetime.strptime(INPUT, '%Y-%m-%dT%H:%M:%S.%fZ')
print(OUTPUT)
