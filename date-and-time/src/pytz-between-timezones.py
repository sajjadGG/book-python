from datetime import datetime
from pytz import timezone


WARSAW = timezone('Europe/Warsaw')
BAJKONUR = timezone('Asia/Almaty')


gagarin = datetime(1961, 4, 12, 14, 7, tzinfo=BAJKONUR)

gagarin.astimezone(WARSAW)
# datetime.datetime(1961, 4, 12, 9, 59,
#                   tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)

