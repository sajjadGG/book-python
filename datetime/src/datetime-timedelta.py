from datetime import datetime, timedelta, date


def month_ago(dt):
    """
    >>> month_ago(datetime(1969, 7, 21, 14, 56, 15))
    datetime.datetime(1969, 6, 21, 4, 27, 9)
    """
    return dt - timedelta(days=30.436875)


datetime.now() - timedelta(hours=3)
date(1961, 4, 12) - timedelta(days=3)

now = datetime.now()
month_ago(now)
