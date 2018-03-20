import datetime

datetime.datetime.now() - datetime.timedelta(hours=3)
datetime.date(2017, 12, 15) - datetime.timedelta(days=3)

def month_ago(date):
    """
    >>> month_ago(datetime.datetime(2000, 1, 31, 0, 0))
    datetime.datetime(2000, 1, 1, 0, 0)
    """
    return date - datetime.timedelta(days=30)
