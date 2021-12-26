Pandas Read String
==================


Rationale
---------
* File paths works also with URLs
* `io.StringIO` Converts ``str`` to File-like object


Example
-------
>>> from io import StringIO
>>> import pandas as pd
>>>
>>>
>>> DATA = """
... "Crew", "Role", "Astronaut"
... "Prime", "CDR", "Neil Armstrong"
... "Prime", "LMP", "Buzz Aldrin"
... "Prime", "CMP", "Michael Collins"
... "Backup", "CDR", "James Lovell"
... "Backup", "LMP", "William Anders"
... "Backup", "CMP", "Fred Haise"
... """
>>>
>>> data = StringIO(DATA)
>>> df = pd.read_csv(data)
>>>
>>> df
     Crew  "Role"         "Astronaut"
0   Prime   "CDR"    "Neil Armstrong"
1   Prime   "LMP"       "Buzz Aldrin"
2   Prime   "CMP"   "Michael Collins"
3  Backup   "CDR"      "James Lovell"
4  Backup   "LMP"    "William Anders"
5  Backup   "CMP"        "Fred Haise"

>>> from io import StringIO
>>> import pandas as pd
>>>
>>>
>>> DATA = 'https://python.astrotech.io/_static/astro-order.csv'
>>>
>>> resp = requests.get(DATA)
>>> data = StringIO(resp.text)
>>> df = pd.read_csv(data)
>>>
>>> df
     Order           Astronaut         Date       Mission
0      1.0        Yuri Gagarin   1961-04-12        Vostok
1      2.0       Gherman Titov   1961-08-06      Vostok 2
2      3.0   Andrian Nikolayev   1962-08-11      Vostok 3
3      4.0      Pavel Popovich   1962-08-12      Vostok 4
4      5.0     Valeri Bykovsky   1963-06-14      Vostok 5
..     ...                 ...          ...           ...
530  531.0      Thomas Pesquet   2016-11-17   Soyuz MS-03
531  532.0        Jack Fischer   2017-04-20   Soyuz MS-04
532  533.0      Mark Vande Hei   2017-09-12   Soyuz MS-06
533  534.0     Norishige Kanai   2017-12-17   Soyuz MS-07
534    NaN        Scott Tingle   2017-12-17   Soyuz MS-07
[535 rows x 4 columns]
