Datetime ISO Standard
=====================
* ISO 8601 is an International Standard [#wikiISO8601]_


Dates
-----
* Format: ``YYYY-mm-dd``
* Year-Month-Day

Example:

    * 1961-04-12
    * 1969-07-21


Time
----
* Format: ``HH:MM:SS.ffffff`` or ``HH:MM:SS`` or ``HH:MM``
* 24 hour clock
* Optional seconds and microseconds
* ``00:00`` - midnight, at the beginning of a day
* ``24:00`` - midnight, at the end of a day (not recommended)
* ``1969-12-31T24:00`` is equal to ``1970-01-01T00:00``

Example:

    * 00:00
    * 06:07:00
    * 13:00:00.123
    * 23:59:59.999999


Date and Time
-------------
* Format: ``YYYY-mm-ddTHH:MM:SS.ffffff``
* "T" separates date and time)
* Optional seconds and microseconds

Example:

    * 1961-04-12T06:07
    * 1961-04-12T06:07:00
    * 1961-04-12T06:07:00.123
    * 1961-04-12T06:07:00.123456


Timezone
--------
* Format: ``YYYY-mm-ddTHH:MM:SS.ffffffUTC``
* Format: ``YYYY-mm-ddTHH:MM:SS.ffffffZ``
* Optional seconds and microseconds
* "Z" (Zulu) means UTC

Time zone notation:

    * ``<time>UTC``
    * ``<time>Z``
    * ``<time>±hh:mm``
    * ``<time>±hhmm``
    * ``<time>±hh``

Example:

    * 1961-04-12T06:07:00.123456Z
    * 1961-04-12T06:07:00.123456UTC
    * 1961-04-12T06:07:00.123456CEST
    * 1961-04-12T06:07:00.123456CET
    * 1961-04-12T06:07:00.123456+02:00
    * 1961-04-12T06:07:00.123456+0200
    * 1961-04-12T06:07:00.123456+02


Week
----
* Format: ``YYYY-Www``
* The ISO 8601 definition for week 01 is the week with the first Thursday of the Gregorian year (i.e. of January) in it. [#wikisoweekdate]_
* ``2009-W01`` - First week of 2009
* ``2009-W53`` - Last week of 2009


Weekday
-------
* Format: ``YYYY-Www-dd``
* Week starts on Monday
* ISO defines Monday as one
* Note year/month changes during the week
* ``2009-W01-1`` - Monday 29 December 2008
* ``2009-W53-7`` - Sunday 3 January 2010

>>> from datetime import datetime
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> dt.isoweekday()
1
>>>
>>> dt.weekday()
0

Duration
--------
* Format: ``P...Y...M...DT...H...M...S``
* Example: P8Y3M8DT20H49M15S
* ``P`` - period - placed at the start of the duration representation
* ``Y`` - number of years
* ``M`` - number of months
* ``W`` - number of weeks
* ``D`` - number of days
* ``T`` - precedes the time components of the representation
* ``H`` - number of hours
* ``M`` - number of minutes
* ``S`` - number of seconds

.. code-block:: text

    P8Y3M8DT20H49M15S

    8 years
    3 months
    8 days
    20 hours
    49 minutes
    15 seconds


To ISO Format
-------------
* ``datetime.isoformat()``
* ``date.isoformat()``
* ``time.isoformat()``

Format to string in ISO-8601 standard:

>>> from datetime import date, time, datetime
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)
>>> d = date(1969, 7, 21)
>>> t = time(2, 56, 15)
>>>
>>> dt.isoformat()
'1969-07-21T02:56:15'
>>>
>>> dt.isoformat(' ')
'1969-07-21 02:56:15'
>>>
>>> d.isoformat()
'1969-07-21'
>>>
>>> t.isoformat()
'02:56:15'


From ISO Format
---------------
* ``datetime.fromisoformat()``
* ``date.fromisoformat()``
* ``time.fromisoformat()``

Parse from string in ISO-8601 standard:

>>> from datetime import date, time, datetime
>>>
>>>
>>> datetime.fromisoformat('1969-07-21T02:56:15')
datetime.datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> date.fromisoformat('1969-07-21')
datetime.date(1969, 7, 21)
>>>
>>> time.fromisoformat('02:56:15')
datetime.time(2, 56, 15)

Note, that ``.fromisoformat()`` is fault-tolerant:

>>> from datetime import date, time, datetime
>>>
>>>
>>> datetime.fromisoformat('1969-07-21T02:56:15')
datetime.datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> datetime.fromisoformat('1969-07-21 02:56:15')
datetime.datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> date.fromisoformat('1969-07-21')
datetime.date(1969, 7, 21)
>>>
>>> time.fromisoformat('02:56:15')
datetime.time(2, 56, 15)
>>>
>>> time.fromisoformat('2:56:15')
Traceback (most recent call last):
ValueError: Invalid isoformat string: '2:56:15'
>>>
>>> time.fromisoformat('2:56')
Traceback (most recent call last):
ValueError: Invalid isoformat string: '2:56'


Use Case - 0x01
---------------
>>> from datetime import datetime
>>>
>>>
>>> line = '1969-07-21T02:56:15.123 [WARNING] First step on the Moon'
>>>
>>> dt, lvl, msg = line.split(maxsplit=2)
>>>
>>> result = {
...     'when': datetime.fromisoformat(dt),
...     'level': lvl.strip('[]'),
...     'message': msg.strip(),
... }
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'when': datetime.datetime(1969, 7, 21, 2, 56, 15, 123000),
 'level': 'WARNING',
 'message': 'First step on the Moon'}


References
----------
.. [#wikisoweekdate] https://en.wikipedia.org/wiki/ISO_week_date
.. [#wikiISO8601] https://en.wikipedia.org/wiki/ISO_8601


Assignments
-----------
.. literalinclude:: assignments/datetime_iso_a.py
    :caption: :download:`Solution <assignments/datetime_iso_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_iso_b.py
    :caption: :download:`Solution <assignments/datetime_iso_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_iso_c.py
    :caption: :download:`Solution <assignments/datetime_iso_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_iso_d.py
    :caption: :download:`Solution <assignments/datetime_iso_d.py>`
    :end-before: # Solution
