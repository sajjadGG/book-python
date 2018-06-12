import pytz

utc = pytz.utc
print(utc.zone)
#'UTC'

eastern = pytz.timezone('US/Eastern')
print(eastern.zone)
# 'US/Eastern'

amsterdam = pytz.timezone('Europe/Warsaw')
print(amsterdam.zone)
# 'Europe/Warsaw'