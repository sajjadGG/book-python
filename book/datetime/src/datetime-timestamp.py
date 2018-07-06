import datetime

MILISECODS = 1e3

# JavaScript has timestamp in miliseconds
# you have to divide by 1e3 = 1000
timestamp = 1331856000000
datetime.datetime.fromtimestamp(timestamp / MILISECODS)
# datetime.datetime(2012, 3, 16, 1, 0)


timestamp = 1331856000000
datetime.datetime.fromtimestamp(timestamp)

