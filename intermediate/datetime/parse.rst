Datetime Parse
==============


Rationale
---------
* Parsing - analyze (a sentence) into its parts and describe their syntactic roles.


Parsing dates
-------------
>>> from datetime import datetime

Datetime parsing from string:

>>> x = '1961-04-12 06:07'
>>> datetime.strptime(x, '%Y-%m-%d %H:%M')
datetime.datetime(1961, 4, 12, 6, 7)


Leading Zero
------------
Mind that while parsing dates without leading zero, you do not use ``%#H``
or ``%-H`` as it was for formatting. One should simply use ``%H`` to capture
hour:

>>> x = '1961-04-12 6:07'
>>> datetime.strptime(x, '%Y-%m-%d %H:%M')
datetime.datetime(1961, 4, 12, 6, 7)


String Fitting
--------------
If there are any other characters in the string, such as commas, brackets
spaces, colons, dashes etc, they should be reflected in the format string.

>>> x = 'Apr 12th, 61 6:07 am'
>>> datetime.strptime(x, '%b %dth, %y %I:%M %p')
datetime.datetime(1961, 4, 12, 6, 7)

>>> x = '12 April 1961 at 6:07 am'
>>> datetime.strptime(x, '%d %B %Y at %I:%M %p')
datetime.datetime(1961, 4, 12, 6, 7)

Omitting any of those values will result with an error:

>>> x = '12 April 1961 at 6:07 am'
>>> datetime.strptime(x, '%d %B %Y %I:%M %p')
Traceback (most recent call last):
ValueError: time data '12 April 1961, at 6:07 am' does not match format '%d %B %Y, %I:%M %p'


Time Zone
---------
* More information in `Datetime Timezone`

>>> x = '12 April 1961 6:07 UTC'
>>> datetime.strptime(x, '%d %B %Y %H:%M %Z')
datetime.datetime(1961, 4, 12, 6, 7)

>>> x = '1961-04-12 6:07 local'
>>> datetime.strptime(x, '%Y-%m-%d %H:%M')
Traceback (most recent call last):
ValueError: unconverted data remains:  local

>>> x = '1961-04-12 6:07 local'
>>> datetime.strptime(x, '%Y-%m-%d %H:%M %Z')
Traceback (most recent call last):
ValueError: time data '1961-04-12 06:07 local' does not match format '%Y-%m-%d %H:%M %Z'

>>> x = '1961-04-12 6:07 local'
>>> datetime.strptime(x, '%Y-%m-%d %H:%M local')
datetime.datetime(1961, 4, 12, 6, 7)


Parsing Parameters
------------------
.. csv-table:: Date and time parsing parameters
    :header-rows: 1
    :widths: 5,35,60
    :file: data/datetime-formatting.csv

.. todo:: Convert table into smaller parts, based on categories: months, day, hour etc.


Use Case - 0x01
---------------
>>> from datetime import datetime
>>>
>>>
>>> line = '1969-07-21T02:56:15.123 [WARNING] First step on the Moon'
>>>
>>> dt, lvl, msg = line.split(maxsplit=2)
>>> dt = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%f')
>>> lvl = lvl.strip('[]')
>>>
>>> print(dt)
1969-07-21 02:56:15.123000
>>>
>>> print(lvl)
WARNING
>>>
>>> print(msg)
First step on the Moon



Assignments
-----------
.. literalinclude:: assignments/datetime_parse_a.py
    :caption: :download:`Solution <assignments/datetime_parse_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_parse_b.py
    :caption: :download:`Solution <assignments/datetime_parse_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_parse_c.py
    :caption: :download:`Solution <assignments/datetime_parse_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_parse_d.py
    :caption: :download:`Solution <assignments/datetime_parse_d.py>`
    :end-before: # Solution
