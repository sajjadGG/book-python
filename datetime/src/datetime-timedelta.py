from datetime import datetime, timedelta, date


datetime.now() - timedelta(hours=3)
date(1961, 4, 12) - timedelta(days=3)


def month_ago(date):
    """
    >>> month_ago(datetime(1969, 7, 21, 14, 56, 15))
    datetime.datetime(1969, 6, 21, 14, 56, 15)
    """
    return date - timedelta(days=30.436875)
