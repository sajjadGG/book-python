**************
Dates and Time
**************


Creating ``date`` objects
=========================

Create ``date``
---------------
.. code-block:: python
    :caption: Create ``date``

    from datetime import date


    d = date(1961, 4, 12)
    # datetime.date(1961, 4, 12)

    d.year    # 1961
    d.month   # 4
    d.day     # 12

Current ``date``
----------------
.. code-block:: python
    :caption: Current ``date``

    from datetime import date


    today = date.today()
    # datetime.date(2020, 1, 5)

    today.year    # 2020
    today.month   # 1
    today.day     # 5

``date`` methods
--------------------
.. code-block:: python
    :caption: ``date`` methods

    from datetime import date


    d = date(1969, 7, 21)

    d.weekday()         # 0  # in US week starts with Sunday
    d.isoweekday()      # 1
    d.isoformat()       # '1969-07-21'


Creating ``time`` objects
=========================

Create ``time``
---------------
.. code-block:: python
    :caption: Create ``time``

    from datetime import time


    t = time(12, 34, 56)
    # datetime.time(12, 33, 44)

    t.hour            # 12
    t.minute          # 34
    t.second          # 56
    t.microsecond     # 0


Create empty ``time`` (midnight)
--------------------------------
.. code-block:: python
    :caption: Create empty ``time`` - midnight

    from datetime import time


    midnight = time()
    # datetime.time(0, 0)


Creating ``datetime`` objects
=============================

Create ``datetime``
-------------------
.. code-block:: python
    :caption: Create ``datetime``

    from datetime import datetime


    dt = datetime(1969, 7, 21, 14, 56, 15)
    # datetime.datetime(1969, 7, 21, 14, 56, 15)

    dt.year          # 1969
    dt.month         # 7
    dt.day           # 21
    dt.hour          # 14
    dt.minute        # 56
    dt.second        # 15
    dt.microsecond   # 0

Create ``datetime`` with empty time (midnight)
----------------------------------------------
.. code-block:: python
    :caption: Create ``datetime`` with empty time

    from datetime import datetime


    dt = datetime(1969, 7, 21)
    # datetime.datetime(1969, 7, 21, 0, 0, 0)

    dt.year          # 1969
    dt.month         # 7
    dt.day           # 21
    dt.hour          # 0
    dt.minute        # 0
    dt.second        # 0
    dt.microsecond   # 0


Create ``datetime`` from ``date`` and ``time`` objects
------------------------------------------------------
.. code-block:: python
    :caption: Create ``datetime`` from ``date`` and ``time`` objects

    from datetime import datetime, date, time


    d = date(1969, 7, 21)
    t = time(14, 56, 15)

    dt = datetime(
        year=d.year,
        month=d.month,
        day=d.day,
        hour=t.hour,
        minute=t. minute,
        second=t.second)
    # datetime.datetime(1969, 7, 21, 14, 56, 15)


    dt = datetime(d.year, d.month, d.day, t.hour, t. minute, t.second)
    # datetime.datetime(1969, 7, 21, 14, 56, 15)

``datetime`` methods
--------------------
.. code-block:: python
    :caption: ``datetime`` methods

    from datetime import datetime


    dt = datetime(1969, 7, 21, 14, 56, 15)
    # datetime.datetime(1969, 7, 21, 14, 56, 15)

    dt.date()        # datetime.date(1969, 7, 21)
    dt.time()        # datetime.time(14, 56, 15)

    dt.weekday()     # 0  # in US week starts with Sunday
    dt.isoweekday()  # 1
    dt.isoformat()   # '1969-07-21T14:56:15'

Current ``datetime`` in local time
----------------------------------
.. code-block:: python
    :caption: Current ``datetime`` in local timezone

    from datetime import datetime


    now = datetime.now()
    # datetime.datetime(2019, 1, 5, 20, 15, 0, 547414)

    now.year          # 2019
    now.month         # 1
    now.day           # 5
    now.hour          # 20
    now.minute        # 15
    now.second        # 0
    now.microsecond   # 547414


Assignments
===========

Create current ``date`` and ``datetime`` objects
------------------------------------------------
* Filename: :download:`solution/datetime_create_current.py`
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min

#. Stwórz obiekt ``date`` z obecną datą
#. Stwórz obiekt ``datetime`` z obecną datą i czasem
#. Jak stworzyć obiekt ``time`` obecnym czasem?

Create ``date``, ``time`` and ``datetime`` objects
--------------------------------------------------
* Filename: :download:`solution/datetime_create_custom.py`
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min

#. Stwórz obiekt ``date`` z datą Twojego urodzenia
#. Stwórz obiekt ``time`` z czasem Twojego urodzenia
#. Stwórz obiekt ``datetime`` z datą i czasem Twojego urodzenia
