from datetime import datetime
from pytz import timezone


BAJKONUR = timezone('Asia/Almaty')


# timezone naive
gagarin = datetime(1961, 4, 12, 14, 7)

BAJKONUR.localize(gagarin)
# datetime.datetime(1961, 4, 12, 14, 7,
#                   tzinfo=<DstTzInfo 'Asia/Almaty' +06+6:00:00 STD>)
