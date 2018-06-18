import datetime


datetime.datetime.now() - datetime.timedelta(hours=3)
datetime.date(1961, 4, 12) - datetime.timedelta(days=3)


def month_ago(date):
    """
    >>> month_ago(datetime.datetime(1969, 7, 21, 14, 56, 15))
    datetime.datetime(1969, 6, 21, 14, 56, 15)
    """
    return date - datetime.timedelta(days=30)
