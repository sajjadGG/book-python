Datetime Create
===============

Rationale
---------
* Date
* Time
* Datetime


Custom Date and Time
--------------------
All ``date``, ``time`` and ``datetime`` classes resides in ``datetime``
module in standard library. At first name may look weird to import
class datetime from module with the same name, but this is pretty common
Python practice. There is a lot of classes with the same name as the module.

First, lets import all the necessary classes:

>>> from datetime import date, time, datetime

Date objects represents a particular day. Example dates are Yuri Gagarin
(first man to fly to space) launch date, or the first day when a person
(Neil Armstrong) set foot on the Moon. In order to create a ``date`` object:

>>> x = date(1969, 7, 21)
>>> print(x)
1969-07-21

Time objects represents given time. For example our classes starts at 9:00
am. or Armstrong set foot on the Moon at 2:56:15 am.

>>> x = time(2, 56, 15)
>>> print(x)
02:56:15

The most important object is a ``datetime`` class. This represents a
particular moment in time. A date and a time. For example, Armstrong set
his foot on the Moon on: July 21st, 1969 at 2:56:15 am. Datetimes are
typically associated with timezones (and the above event happen on that
particular time of UTC timezone) but we will cover this topic later on:

>>> x = datetime(1969, 7, 21, 2, 56, 15)
>>> print(x)
1969-07-21 02:56:15


Date Attributes
---------------
Lets create a date object:

>>> from datetime import date
>>>
>>> x = date(1969, 7, 21)

You can access date attributes by ``.`` dot notation. Attributes stored in
this class are: year, month, day:

>>> print(x.year)
1969

>>> print(x.month)
7

>>> print(x.day)
21


Time Attributes
---------------
Lets create a time object:

>>> from datetime import time
>>>
>>> t = time(2, 56, 15)

Time object, has different attributes than date object. This should be
completely understandable since both objects represents different things,
a date and time respectively.

With time object you can access hour, minute, second and microsecond
attributes:

>>> t.hour
2

>>> t.minute
56

>>> t.second
15

>>> t.microsecond
0


Datetime Attributes
-------------------
Lets create a time object:

>>> from datetime import datetime
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)

Datetime object is the most versatile and the most commonly used. It
combines all the attributes from both ``date`` and ``time`` objects. You can
access all of those attributes using dot ``.`` notation. The attributes are:
year, month, day, hour, minute, second, microsecond.

>>> dt.year
1969
>>>
>>> dt.month
7
>>>
>>> dt.day
21

>>> dt.hour
2
>>>
>>> dt.minute
56
>>>
>>> dt.second
15
>>>
>>> dt.microsecond
0


Current Date and Time
---------------------
Create ``date`` object with current date:

>>> from datetime import date
>>>
>>>
>>> today = date.today()

Create ``datetime`` object with current date and time:

>>> from datetime import datetime
>>>
>>>
>>> now = datetime.now()

There is no ``time.now()``


Combine
-------
Create ``datetime`` from ``date`` and ``time`` objects:

>>> from datetime import datetime, date, time
>>>
>>>
>>> d = date(1969, 7, 21)
>>> t = time(2, 56, 15)
>>>
>>> datetime.combine(d, t)
datetime.datetime(1969, 7, 21, 2, 56, 15)


Split
-----
>>> from datetime import datetime
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> dt.date()
datetime.date(1969, 7, 21)
>>>
>>> dt.time()
datetime.time(2, 56, 15)



Empty Time
----------
>>> from datetime import time
>>>
>>>
>>> time()
datetime.time(0, 0)
>>>
>>> time(0, 0)
datetime.time(0, 0)
>>>
>>> time(0, 0, 0)
datetime.time(0, 0)
>>>
>>> time(12)
datetime.time(12, 0)
>>>
>>> time(12, 0)
datetime.time(12, 0)
>>>
>>> time(12, 0, 0)
datetime.time(12, 0)
>>>
>>> time(24, 0)
Traceback (most recent call last):
ValueError: hour must be in 0..23

>>> from datetime import datetime
>>>
>>>
>>> datetime(1969, 7, 21)
datetime.datetime(1969, 7, 21, 0, 0)


Use Case - 0x01
---------------
>>> from datetime import datetime, date, time
>>>
>>>
>>> d = date(1969, 7, 21)
>>> t = time(2, 56, 15)
>>>
>>> datetime(
...     year=d.year,
...     month=d.month,
...     day=d.day,
...     hour=t.hour,
...     minute=t.minute,
...     second=t.second)
datetime.datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> datetime(d.year, d.month, d.day, t.hour, t. minute, t.second)
datetime.datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> datetime.combine(d, t)
datetime.datetime(1969, 7, 21, 2, 56, 15)



Assignments
-----------
.. literalinclude:: assignments/datetime_create_a.py
    :caption: :download:`Solution <assignments/datetime_create_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_create_b.py
    :caption: :download:`Solution <assignments/datetime_create_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_create_c.py
    :caption: :download:`Solution <assignments/datetime_create_c.py>`
    :end-before: # Solution
