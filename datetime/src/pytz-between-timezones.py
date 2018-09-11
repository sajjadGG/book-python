from datetime import datetime
import pytz

utc = pytz.utc
kazachstan = pytz.timezone('Asia/Almaty')
eastern = pytz.timezone('US/Eastern')
warsaw = pytz.timezone('Europe/Warsaw')


gagarin = datetime(1961, 4, 12, 14, 7, tzinfo=kazachstan)


in_utc = utc.localize(gagarin, is_dst=None)      # No daylight saving time

print(in_utc)

import sys
sys.exit()

in_est = eastern.localize(gagarin, is_dst=None)  # No daylight saving time
in_waw = warsaw.localize(gagarin, is_dst=None)   # No daylight saving time


print(f'{in_utc:%Y-%m-%d %H:%M:%S %Z%z}')
# 1961-04-12 14:07:00 UTC+0000


print(f'{in_est:%Y-%m-%d %H:%M:%S %Z%z}')
# 1961-04-12 14:07:00 EST-0500


print(f'{in_waw:%Y-%m-%d %H:%M:%S %Z%z}')
# 1961-04-12 14:07:00 CET+0100
