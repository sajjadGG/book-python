import pytz

utc = pytz.utc
print(utc.zone)
#'UTC'

eastern = pytz.timezone('US/Eastern')
print(eastern.zone)
# 'US/Eastern'

warsaw = pytz.timezone('Europe/Warsaw')
print(warsaw.zone)
# 'Europe/Warsaw'
