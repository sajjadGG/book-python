"""
* Assignment: Datetime Create Custom
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create `date` object with date of your birth
    2. Create `time` object with time of your birth
    3. Create `datetime` object with date and time of your birth

Polish:
    1. Stwórz obiekt `date` z datą Twojego urodzenia
    2. Stwórz obiekt `time` z czasem Twojego urodzenia
    3. Stwórz obiekt `datetime` z datą i czasem Twojego urodzenia

Tests:
    >>> assert type(dt) is datetime, \
    'Variable `dt` has invalid type, must be a datetime'

    >>> assert type(d) is date, \
    'Variable `dt` has invalid type, must be a date'

    >>> assert type(t) is time, \
    'Variable `t` has invalid type, must be a time'

    >>> str(d)
    '1970-01-01'
    >>> str(t)
    '00:00:00'
    >>> str(dt)
    '1970-01-01 00:00:00'
"""


# Given
from datetime import datetime, date, time


# Solution
d = date(1970, 1, 1)
t = time(0, 0)
dt = datetime(1970, 1, 1, 0, 0, 0)
