Pandas Read SQL
===============


Rationale
---------
* File paths works also with URLs
* SQL functions uses SQLAlchemy, which supports many RDBMS

>>> import pandas as pd

Read SQL query or database table into a DataFrame:

>>> pd.read_sql()  # doctest: +SKIP

Read SQL query into a DataFrame

>>> pd.read_sql_query()  # doctest: +SKIP

Read SQL database table into a DataFrame

>>> pd.read_sql_table()  # doctest: +SKIP
>>> pd.read_table()  # doctest: +SKIP


Read SQL
--------
>>> import sqlite3
>>> import requests
>>>
>>>
>>> DATA = 'https://python.astrotech.io/_static/astro-timeline.sqlite3'
>>> DATABASE = '/tmp/astro-timeline.sqlite3'
>>>
>>> SQL = """
...     SELECT *
...     FROM logs
... """
>>>
>>>
>>> # Download database
>>> with open(DATABASE, mode='wb') as db:
...     resp = requests.get(DATA)
...     db.write(resp.content)
12145
>>>
>>>
>>> # Read data from database
>>> with sqlite3.connect(DATABASE) as db:
...     astro_timeline = pd.read_sql(SQL, db, parse_dates=['datetime'])
>>>
>>>
>>> astro_timeline
    id  ...                                            message
0    1  ...                         Terminal countdown started
1    2  ...                          S-IC engine ignition (#5)
2    3  ...          Maximum dynamic pressure (735.17 lb/ft^2)
3    4  ...                                      S-II ignition
4    5  ...                     Launch escape tower jettisoned
5    6  ...                          S-II center engine cutoff
6    7  ...                               Translunar injection
7    8  ...                           CSM docked with LM/S-IVB
8    9  ...                     Lunar orbit insertion ignition
9   10  ...               Lunar orbit circularization ignition
10  11  ...                                    CSM/LM undocked
11  12  ...                 LM powered descent engine ignition
12  13  ...                                      LM 1202 alarm
13  14  ...                                      LM 1201 alarm
14  15  ...                                   LM lunar landing
15  16  ...                           EVA started (hatch open)
16  17  ...                 1st step taken lunar surface (CDR)
17  18  ...  That's one small step for [a] man... one giant...
18  19  ...        Contingency sample collection started (CDR)
19  20  ...                               LMP on lunar surface
20  21  ...                           EVA ended (hatch closed)
21  22  ...                 LM lunar liftoff ignition (LM APS)
22  23  ...                                      CSM/LM docked
23  24  ...                Transearth injection ignition (SPS)
24  25  ...                                   CM/SM separation
25  26  ...                                              Entry
26  27  ...                     Splashdown (went to apex-down)
27  28  ...                                        Crew egress
[28 rows x 4 columns]


Assignments
-----------
