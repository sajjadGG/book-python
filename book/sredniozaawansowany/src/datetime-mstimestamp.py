import datetime
import time


def datetime_to_mstimestamp(date):
    """
    Active Direcotry has different approach to create timestamp than Unix.
    Here's a function to convert the Unix timestamp to the AD one.

    >>> datetime_to_mstimestamp(datetime.datetime(2000, 1, 1, 0, 0))
    125911548000000000
    """
    timestamp = int(time.mktime(date.timetuple()))
    magic_number = 116444736000000000
    return timestamp * 10000000 + magic_number


def mstimestamp_to_datetime(mstimestamp):
    """
    Active Direcotry has different approach to create timestamp than Unix.
    Here's a function to convert AD timestamp to the Unix one.

    >>> mstimestamp_to_datetime(130567328471235643)
    datetime.datetime(2014, 10, 2, 16, 14, 7, 123563)
    """
    magic_number = 11644473600
    return datetime.datetime.fromtimestamp(
        mstimestamp / 10000000 - magic_number)
