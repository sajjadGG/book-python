"""
* Assignment: Datetime Create Custom
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. First human (Yuri Gagarin) flown to space on
       April 12th, 1961 at 6:07 a.m. from Bajkonur Cosmodrome in Kazahstan
    2. Create `date` object representing date of the launch
    3. Create `time` object representing time of the launch
    4. Combine date and time into `datetime` object representing
       exact moment of the launch
    5. Run doctests - all must succeed

Polish:
    1. Pierwszy człowiek (Juri Gagarin) poleciał w kosmos
       12 kwietnia 1961 roku o 6:07 rano z kosmodromu Bajkonur w Kazachstanie
    2. Stwórz obiekt `date` reprezentujący datę startu
    3. Stwórz obiekt `time` reprezentujący czas startu
    4. Połącz datę i czas w obiekt `datetime` reprezentujący
       dokładny moment startu
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert dt is not Ellipsis, \
    'Assign result to variable: `dt`'
    >>> assert d is not Ellipsis, \
    'Assign result to variable: `d`'
    >>> assert t is not Ellipsis, \
    'Assign result to variable: `t`'
    >>> assert type(dt) is datetime, \
    'Variable `dt` has invalid type, must be a datetime'
    >>> assert type(d) is date, \
    'Variable `d` has invalid type, must be a date'
    >>> assert type(t) is time, \
    'Variable `t` has invalid type, must be a time'

    >>> print(d)
    1961-04-12

    >>> print(t)
    06:07:00

    >>> print(dt)
    1961-04-12 06:07:00
"""

from datetime import date, datetime, time


# datetime: representing April 12th, 1961 6:07 a.m.
dt = ...

# date: representing April 12th, 1961 6:07 a.m.
d = ...

# time: representing April 12th, 1961 6:07 a.m.
t = ...

# Solution
dt = datetime(1961, 4, 12, 6, 7)
d = date(1961, 4, 12)
t = time(6, 7)
