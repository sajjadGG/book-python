from datetime import datetime
from pytz import timezone, utc as UTC


WARSAW = timezone('Europe/Warsaw')


armstrong = datetime(1969, 7, 21, 14, 56, 15, tzinfo=UTC)

armstrong.astimezone(WARSAW)
# datetime.datetime(1969, 7, 21, 15, 56, 15,
#                   tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)
