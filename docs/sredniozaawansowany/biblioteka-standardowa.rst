**********************
Biblioteka standardowa
**********************

``datetime``
============

* `Computerophile Time & Time Zones <https://www.youtube.com/watch?v=-5wpm-gesOY>`_

Tworzenie obiektu ``date`` i ``datetime``
-----------------------------------------

.. code-block:: python

    import datetime

    now = datetime.datetime.now()
    today = datetime.date.today()

    date = datetime.date(2017, 12, 15)
    dt = datetime.datetime(2017, 12, 15, 20, 13, 33)
    midnight = datetime.datetime(2017, 12, 15)


Różne formaty dat
-----------------

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

* '15.12.2017'
* '15/12/2017'
* '15 grudnia 2017'
* '15 grudzień 2017'
* '12/15/17'
* 'December 15, 2017'
* '2017-12-15'

.. code-block:: python

    import datetime

    now = datetime.datetime.now()
    now.strftime('%A, %B %d, %I:%M %p')

    print(f'{now:%Y-%m-%d}')

+-----------+--------------------------------+------------------------+
| Directive | Meaning                        | Example                |
+===========+================================+========================+
| ``%a``    | Weekday as locale's            | Sun, Mon, ..., Sat     |
|           | abbreviated name.              |  (en_US);              |
|           |                                | So, Mo, ..., Sa (de_DE)|
+-----------+--------------------------------+------------------------+
| ``%A``    | Weekday as locale's full name. | Sunday, Monday, ...,   |
|           |                                |  Saturday (en_US);     |
|           |                                | Sonntag, Montag, ...,  |
|           |                                |  Samstag (de_DE)       |
+-----------+--------------------------------+------------------------+
| ``%w``    | Weekday as a decimal number,   | 0, 1, ..., 6           |
|           | where 0 is Sunday and 6 is     |                        |
|           | Saturday.                      |                        |
+-----------+--------------------------------+------------------------+
| ``%d``    | Day of the month as a          | 01, 02, ..., 31        |
|           | zero-padded decimal number.    |                        |
+-----------+--------------------------------+------------------------+
| ``%b``    | Month as locale's abbreviated  | Jan, Feb, ..., Dec     |
|           | name.                          |  (en_US);              |
|           |                                | Jan, Feb, ..., Dez     |
|           |                                |  (de_DE)               |
+-----------+--------------------------------+------------------------+
| ``%B``    | Month as locale's full name.   | January, February,     |
|           |                                |  ..., December (en_US);|
|           |                                | Januar, Februar, ...,  |
|           |                                |  Dezember (de_DE)      |
+-----------+--------------------------------+------------------------+
| ``%m``    | Month as a zero-padded         | 01, 02, ..., 12        |
|           | decimal number.                |                        |
+-----------+--------------------------------+------------------------+
| ``%y``    | Year without century as a      | 00, 01, ..., 99        |
|           | zero-padded decimal number.    |                        |
+-----------+--------------------------------+------------------------+
| ``%Y``    | Year with century as a decimal | 0001, 0002, ..., 2013, |
|           | number.                        | 2014, ..., 9998, 9999  |
+-----------+--------------------------------+------------------------+
| ``%H``    | Hour (24-hour clock) as a      | 00, 01, ..., 23        |
|           | zero-padded decimal number.    |                        |
+-----------+--------------------------------+------------------------+
| ``%I``    | Hour (12-hour clock) as a      | 01, 02, ..., 12        |
|           | zero-padded decimal number.    |                        |
+-----------+--------------------------------+------------------------+
| ``%p``    | Locale's equivalent of either  | AM, PM (en_US);        |
|           | AM or PM.                      | am, pm (de_DE)         |
+-----------+--------------------------------+------------------------+
| ``%M``    | Minute as a zero-padded        | 00, 01, ..., 59        |
|           | decimal number.                |                        |
+-----------+--------------------------------+------------------------+
| ``%S``    | Second as a zero-padded        | 00, 01, ..., 59        |
|           | decimal number.                |                        |
+-----------+--------------------------------+------------------------+
| ``%f``    | Microsecond as a decimal       | 000000, 000001, ...,   |
|           | number, zero-padded on the     | 999999                 |
|           | left.                          |                        |
+-----------+--------------------------------+------------------------+
| ``%z``    | UTC offset in the form +HHMM   | (empty), +0000, -0400, |
|           | or -HHMM (empty string if the  | +1030                  |
|           | object is naive).              |                        |
+-----------+--------------------------------+------------------------+
| ``%Z``    | Time zone name (empty string   | (empty), UTC, EST, CST |
|           | if the object is naive).       |                        |
+-----------+--------------------------------+------------------------+
| ``%j``    | Day of the year as a           | 001, 002, ..., 366     |
|           | zero-padded decimal number.    |                        |
+-----------+--------------------------------+------------------------+
| ``%U``    | Week number of the year        | 00, 01, ..., 53        |
|           | (Sunday as the first day of    |                        |
|           | the week) as a zero padded     |                        |
|           | decimal number. All days in a  |                        |
|           | new year preceding the first   |                        |
|           | Sunday are considered to be in |                        |
|           | week 0.                        |                        |
+-----------+--------------------------------+------------------------+
| ``%W``    | Week number of the year        | 00, 01, ..., 53        |
|           | (Monday as the first day of    |                        |
|           | the week) as a decimal number. |                        |
|           | All days in a new year         |                        |
|           | preceding the first Monday     |                        |
|           | are considered to be in        |                        |
|           | week 0.                        |                        |
+-----------+--------------------------------+------------------------+
| ``%c``    | Locale's appropriate date and  | Tue Aug 16 21:30:00    |
|           | time representation.           |  1988 (en_US);         |
|           |                                | Di 16 Aug 21:30:00     |
|           |                                |  1988 (de_DE)          |
+-----------+--------------------------------+------------------------+
| ``%x``    | Locale's appropriate date      | 08/16/88 (None);       |
|           | representation.                | 08/16/1988 (en_US);    |
|           |                                | 16.08.1988 (de_DE)     |
+-----------+--------------------------------+------------------------+
| ``%X``    | Locale's appropriate time      | 21:30:00 (en_US);      |
|           | representation.                | 21:30:00 (de_DE)       |
+-----------+--------------------------------+------------------------+
| ``%%``    | A literal ``'%'`` character.   | %                      |
+-----------+--------------------------------+------------------------+

Several additional directives not required by the C89 standard are included for
convenience. These parameters all correspond to ISO 8601 date values. These
may not be available on all platforms when used with the `strftime`
method. The ISO 8601 year and ISO 8601 week directives are not interchangeable
with the year and week number directives above. Calling `strptime` with
incomplete or ambiguous ISO 8601 directives will raise a `ValueError`.

+-----------+--------------------------------+------------------------+
| Directive | Meaning                        | Example                |
+===========+================================+========================+
| ``%G``    | ISO 8601 year with century     | 0001, 0002, ..., 2013, |
|           | representing the year that     | 2014, ..., 9998, 9999  |
|           | contains the greater part of   |                        |
|           | the ISO week (``%V``).         |                        |
+-----------+--------------------------------+------------------------+
| ``%u``    | ISO 8601 weekday as a decimal  | 1, 2, ..., 7           |
|           | number where 1 is Monday.      |                        |
+-----------+--------------------------------+------------------------+
| ``%V``    | ISO 8601 week as a decimal     | 01, 02, ..., 53        |
|           | number with Monday as          |                        |
|           | the first day of the week.     |                        |
|           | Week 01 is the week containing |                        |
|           | Jan 4.                         |                        |
+-----------+--------------------------------+------------------------+


Przesunięcia czasu (dodawanie i odejmowanie)
--------------------------------------------

.. code-block:: python

    import datetime

    datetime.datetime.now() - datetime.timedelta(hours=3)
    datetime.date(2017, 12, 15) - datetime.timedelta(days=3)

Strefy czasowe
--------------

.. code-block:: python

    import datetime

    datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)

Zadanie kontrolne
-----------------

:Zadanie:
    Zaczytaj datę podaną przez użytkownika wykorzystując ``input()``. Użytkownik podaje datę w formacie amerykańskim, na przykład:

        - 'April 12, 1961 6:07 AM'
        - 'July 21, 1969 2:56:15 AM UTC'

    * Przedstaw datę jako objekt ``datetime``. I wyświetl go w formacie ISO.
    * Odejmij obie daty od siebie. Ile czasu minęło między wydarzeniami?
    * Do dzisiejszej dodaj ten sam czas ile wyszło Ci w poprzednim zadaniu. Wyświetl datę (bez czasu).

:Zadanie z gwiazdką:
    * Uwzględnij strefy czasowe.
    * Co to za daty, które podał użytkownik?


``time``
========


``os``
======

.. code-block:: python

    import os

    os.path
    os.walk
    os.path.join
    os.path.abspath
    os.path.dirname

.. code-block:: python

    import os

    for element in os.scandir('/etc'):
        print(element.name)

    script = os.path.basename(__file__)
    PWD = os.path.basename(os.getcwd())

    path = os.path.join(PWD, script)

    print(path)


``sys``
=======

.. code-block:: python

    import sys

    sys.path
    sys.path.append
    sys.platform


``warnings``
============

.. code-block:: python

    import warnings

    warnings.warn('Wersja API jest już nieaktualna', PendingDeprecationWarning)

.. code-block:: python

    import warnings

    def run_HTTP_server(*args, **kwargs):
        pass


    def runHTTPServer(*args, **kwargs):
        warnings.warn(PendingDeprecationWarning, 'You should use \'run_HTTP_server()\' instead.')
        return run_HTTP_server(*args, **kwargs)


``pprint``
==========

.. code-block:: python

    from pprint import pprint

    data = [
       {'first_name': 'Baked', 'last_name': 'Beans'},
       {'first_name': 'Lovely', 'last_name': 'Spam'},
       {'first_name': 'Wonderful', 'last_name': 'Spam'}
    ]

    pprint(data)

``csv``
=======

.. code-block:: python

    import csv

    csv.DictReader()
    csv.DictWriter()

``memoize``
===========

``json``
========

.. code-block:: python

    import json

    json.loads()
    json.dumps()

``sqlite``
==========

``re``
======

.. code-block:: python

    import re

    re.search()
    re.findall()
    re.match()
    re.compile()

``httplib``
===========

``urllib``
==========

``socket``
==========

``tempfile``
============

``io``
======

.. code-block:: python

    import io

    io.StringIO

``functools``
=============

``itertools``
=============

``math``
========

.. code-block:: python

    import math

    math.sin()
    math.cos()
    math.tan()
    math.pi

``statistics``
==============

.. code-block:: python

    import statistics

    statistics.avg()
    statistics.mean()
    statistics.stdev()

``random``
==========

.. code-block:: python

    import random

    random.sample()
    random.random()

``subprocess``
==============

.. code-block:: python

    import subprocess

    subprocess.Popen()

``doctest``
===========

.. code-block:: python

    import doctest

    doctest.testmod()


Collections
===========

================  ====================================================================
Name              Description
================  ====================================================================
``namedtuple()``  factory function for creating tuple subclasses with named fields
``deque``         list-like container with fast appends and pops on either end
``ChainMap``      dict-like class for creating a single view of multiple mappings
``Counter``       dict subclass for counting hashable objects
``OrderedDict``   dict subclass that remembers the order entries were added
``defaultdict``   dict subclass that calls a factory function to supply missing values
``UserDict``      wrapper around dictionary objects for easier dict subclassing
``UserList``      wrapper around list objects for easier list subclassing
``UserString``    wrapper around string objects for easier string subclassing
================  ====================================================================
