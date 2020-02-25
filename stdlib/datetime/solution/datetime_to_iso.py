from datetime import datetime


INPUT = 'April 12, 1961 6:07 local time'

format = '%B %d, %Y %H:%M local time'
dt = datetime.strptime(INPUT, format)

OUTPUT = dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
print(OUTPUT)
