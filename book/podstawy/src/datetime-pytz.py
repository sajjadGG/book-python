from datetime import datetime, timedelta
from pytz import timezone
import pytz

utc = pytz.utc
print(utc.zone)
#'UTC'

eastern = timezone('US/Eastern')
print(eastern.zone)
# 'US/Eastern'

amsterdam = timezone('Europe/Amsterdam')
print(amsterdam.zone)
# 'Europe/Amsterdam'