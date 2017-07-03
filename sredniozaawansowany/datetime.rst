********
Datetime
********

``calendar``
============

.. code-block:: python

    import calendar

    cal = calendar.HTMLCalendar()
    cal.formatmonth(2017, 12)



``time``
========

.. code-block:: python

    import time

    time.sleep(2)

.. code-block:: python

    import time

    >>> time.time()
    1496737953.0712671

    >>> time.time()
    1496737954.3189602

    >>> time.time()
    1496737954.9830358

.. code-block:: python

    >>> from time import gmtime, strftime

    >>> strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    'Thu, 28 Jun 2001 14:17:15 +0000'

.. code-block:: python

    >>> import time

    >>> time.strptime("30 Nov 00", "%d %b %y")
    time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)

.. code-block:: python

    >>> import time

    >>> time.timezone
    -3600

    >>> time.tzname
    ('CET', 'CEST')


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
|           | abbreviated name.              |                        |
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
may not be available on all platforms when used with the ``strftime``
method. The ISO 8601 year and ISO 8601 week directives are not interchangeable
with the year and week number directives above. Calling ``strptime`` with
incomplete or ambiguous ISO 8601 directives will raise a ``ValueError``.

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

    >>> import datetime

    >>> d1 = datetime.datetime(2017, 6, 6, 10, 20, 36) - datetime.datetime(2017, 6, 3, 13, 17, 24)

    >>> print(d1)
    2 days, 21:03:12


.. code-block:: python

    import datetime

    datetime.datetime.now() - datetime.timedelta(hours=3)
    datetime.date(2017, 12, 15) - datetime.timedelta(days=3)

Strefy czasowe
--------------

.. code-block:: python

    import datetime

    datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)


``pytz``
========

.. code-block:: python

    >>> from datetime import datetime, timedelta
    >>> from pytz import timezone
    >>> import pytz

    >>> utc = pytz.utc
    >>> utc.zone
    'UTC'
    >>> eastern = timezone('US/Eastern')
    >>> eastern.zone
    'US/Eastern'
    >>> amsterdam = timezone('Europe/Amsterdam')
    >>> fmt = '%Y-%m-%d %H:%M:%S %Z%z'



Zadania kontrolne
=================

Manipulacja datami
------------------
Użytkownik poda wykorzystując ``input()`` dwie następujące daty w formacie jak poniżej:

    - 'April 12, 1961 2:07 AM local time' # ALMT Timezone
    - '07/21/69 2:56:15 AM UTC'

* Przedstaw daty jako obiekt ``datetime``. I wyświetl je w formacie ISO.
* Odejmij obie daty od siebie. Ile lat i miesięcy minęło między wydarzeniami?
* Do dzisiejszej dodaj ten sam czas ile wyszło Ci w poprzednim zadaniu.
* Wyświetl samą datę (bez czasu).
* Ile będziesz miał wtedy lat?

:Zadanie z gwiazdką:
    * Uwzględnij strefy czasowe.
    * Co to za daty, które podał użytkownik?

:Podpowiedź:
    * wykorzystaj ``try`` i ``except`` przy ``strptime``
