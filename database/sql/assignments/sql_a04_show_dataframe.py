"""
* Assignment: Database Show DataFrame
* Complexity: easy
* Lines of code: 0 lines
* Time: 3 min

English:
    1. Run file to show data from table in DataFrame format:
       a. table: apollo11
    2. Run doctests - all must succeed

Polish:
    1. Uruchom plik aby wyświetlić dane z tabeli w formacie DataFrame:
       a. table: apollo11
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> import sqlite3
    >>> import pandas as pd

    >>> pd.set_option('display.width', 1000)
    >>> pd.set_option('display.max_rows', 500)
    >>> pd.set_option('display.max_columns', 50)

    >>> database = Path(__file__).parent / 'sql.db'

    >>> with sqlite3.connect(database) as db:
    ...     df = pd.read_sql(result, db)

    >>> print(df)  # doctest: +ELLIPSIS
                    datetime        date             time                  met  category                                              event
    0    1969-07-14 21:00:00  1969-07-14  21:00:00.000000     -100800000000000     DEBUG                        Terminal countdown started.
    1    1969-07-15 16:00:00  1969-07-15  16:00:00.000000      -32400000000000     DEBUG               Scheduled 11-hour hold at T-9 hours.
    2    1969-07-16 03:00:00  1969-07-16  03:00:00.000000      -32400000000000     DEBUG                    Countdown resumed at T-9 hours.
    3    1969-07-16 08:30:00  1969-07-16  08:30:00.000000      -12600000000000     DEBUG  Scheduled 1-hour 32-minute hold at T-3 hours 3...
    4    1969-07-16 10:02:00  1969-07-16  10:02:00.000000      -12600000000000     DEBUG         Countdown resumed at T-3 hours 30 minutes.
    ...
    247  1969-08-10 00:00:00  1969-08-10  00:00:00.000000 -9223372036854775808     DEBUG                     Crew released from quarantine.
    248  1969-08-14 00:00:00  1969-08-14  00:00:00.000000 -9223372036854775808     DEBUG  CM delivered to contractor’s facility in Downe...
    249  1969-08-27 00:00:00  1969-08-27  00:00:00.000000 -9223372036854775808     DEBUG                EASEP turned off by ground command.
"""

# Show data from `apollo11` table in DataFrame format
# type: str
result = """

SELECT *
FROM apollo11

"""

# Solution
result = """

SELECT *
FROM apollo11

"""
