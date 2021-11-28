Datetime Format
===============


Rationale
---------
* ``format(dt, '%Y-%m-%d')``
* ``dt.__format__('%Y-%m-%d')``
* ``dt.strftime('%Y-%m-%d')``
* ``f'Today is {dt:%Y-%m-%d}'``


Formats
-------
>>> from datetime import datetime
>>>
>>>
>>> dt = datetime(1961, 4, 12, 6, 7)
>>>
>>> format(dt, '%Y')
'1961'
>>>
>>> format(dt, '%Y-%m-%d')
'1961-04-12'
>>>
>>> format(dt, '%d.%m.%Y')
'12.04.1961'
>>>
>>> format(dt, '%H:%M')
'06:07'
>>>
>>> format(dt, '%Y-%m-%d %H:%M')
'1961-04-12 06:07'
>>>
>>> format(dt, '%Y-%m-%d %H:%M:%S')
'1961-04-12 06:07:00'
>>>
>>> format(dt, '%B %d, %Y')
'April 12, 1961'


Parameters
----------
* Similar in almost all programming language
* Some minor differences like in JavaScript minutes are ``i``, not ``M``

.. csv-table:: Date and time parsing and formatting parameters
    :header-rows: 1
    :widths: 5,35,60
    :file: data/datetime-formatting.csv

.. todo:: Convert table into smaller parts, based on categories: months, day, hour etc.


Leading Zero
------------
* ``%#H`` - remove leading zero (Windows)
* ``%-H`` - remove leading zero (macOS, Linux, \*nix)
* ``%_H`` - replace leading zero with space (macOS, Linux, \*nix)
* Works only with formatting
* raises ValueError while parsing [#pydocdtformat]_

On Linux and \*nix systems:

>>> from datetime import datetime
>>>
>>>
>>> dt = datetime(1961, 4, 12, 6, 7)
>>>
>>> format(dt, '%H:%M')
'06:07'
>>>
>>> format(dt, '%-H:%M')
'6:07'
>>>
>>> format(dt, '%_H:%M')
' 6:07'
>>>
>>> format(dt, '%#H:%M')
'06:07'

On macOS:

>>> from datetime import datetime
>>>
>>>
>>> dt = datetime(1961, 4, 12, 6, 7)
>>>
>>> format(dt, '%H:%M')
'06:07'
>>>
>>> format(dt, '%-H:%M')
'6:07'
>>>
>>> format(dt, '%#H:%M')  # doctest: +SKIP
'#H:07'

On Windows 10:

>>> from datetime import datetime
>>>
>>>
>>> dt = datetime(1961, 4, 12, 6, 7)
>>>
>>> format(dt, '%H:%M')
'06:07'
>>>
>>> format(dt, '%-H:%M')  # doctest: +SKIP
Traceback (most recent call last):
ValueError: Invalid format string
>>>
>>> format(dt, '%_H:%M')  # doctest: +SKIP
Traceback (most recent call last):
ValueError: Invalid format string
>>>
>>> format(dt, '%#H:%M')  # doctest: +SKIP
'6:07'


.. csv-table:: Leading Zero
    :header: "Meaning", "With", "Without (macOS, Linux)", "Without (Windows)"
    :widths: 55, 15, 15, 15

    "day",                          ``%d``, ``%-d``, ``%#d``
    "hour 24h",                     ``%H``, ``%-H``, ``%#H``
    "hour 12h",                     ``%I``, ``%-I``, ``%#I``
    "day of a year",                ``%j``, ``%-j``, ``%#j``
    "month",                        ``%m``, ``%-m``, ``%#m``
    "minute",                       ``%M``, ``%-M``, ``%#M``
    "second",                       ``%S``, ``%-S``, ``%#S``
    "week number (Sunday first)",   ``%U``, ``%-U``, ``%#U``
    "week number (Monday first)",   ``%W``, ``%-W``, ``%#W``
    "weekday (Sunday first)",       ``%w``, ``%-w``, ``%#w``
    "year short",                   ``%y``, ``%-y``, ``%#y``
    "year long",                    ``%Y``, ``%-Y``, ``%#Y``


String Format Time
------------------
>>> from datetime import datetime
>>>
>>>
>>> gagarin = datetime(1961, 4, 12, 6, 7)
>>> formatted = gagarin.strftime('%Y-%m-%d %H:%M')
>>>
>>> print(f'Gagarin launched on {formatted}')
Gagarin launched on 1961-04-12 06:07


Format String
-------------
>>> from datetime import datetime
>>>
>>>
>>> gagarin = datetime(1961, 4, 12, 6, 7)
>>>
>>> print(f'Gagarin launched on {gagarin:%Y-%m-%d}')
Gagarin launched on 1961-04-12
>>>
>>> print(f'Gagarin launched on {gagarin:%Y-%m-%d %H:%M}')
Gagarin launched on 1961-04-12 06:07

>>> from datetime import datetime
>>>
>>>
>>> gagarin = datetime(1961, 4, 12, 6, 7)
>>> format = '%Y-%m-%d %H:%M'
>>>
>>> print(f'Gagarin launched on {gagarin:{format}}')
Gagarin launched on 1961-04-12 06:07


References
----------
.. [#pydocdtformat] https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior


Assignments
-----------
.. literalinclude:: assignments/datetime_format_a.py
    :caption: :download:`Solution <assignments/datetime_format_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_format_b.py
    :caption: :download:`Solution <assignments/datetime_format_b.py>`
    :end-before: # Solution
