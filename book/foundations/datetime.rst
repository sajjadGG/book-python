**************
Dates and Time
**************

.. warning:: If you're thinking about implementing your own time calculator or system, watch Computerophile Time & Time Zones https://www.youtube.com/watch?v=-5wpm-gesOY

``datetime``
============

Tworzenie obiektu ``date`` i ``datetime``
-----------------------------------------
.. literalinclude:: src/datetime-new.py
    :language: python
    :caption: Creating ``date`` and ``datetime`` objects


Różne formaty dat i czasu
-------------------------
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

Problem z formatami dat:

* '12.4.1961'
* '12.04.1961'
* '12 IV 1961'
* '12.IV.1961'
* '12/4/1961'
* '12/04/1961'
* '12 kwietnia 1961'
* '12 kwiecień 1961'
* '4/12/61'
* 'April 12, 1961'

Problem z formatami czasu:

* '12:00 am'
* '12:00 pm'
* '12:00'
* '23:59'
* '24:00'
* '0:00'
* '00:00'

Standard ISO:

* '1961-04-12'
* '1961-04-12T06:07:00'
* '1961-04-12T06:07:00.123456'

Formatowanie dat
----------------
.. literalinclude:: src/datetime-format.py
    :language: python
    :caption: Datetime formatting as string

Parsowanie dat
--------------
.. literalinclude:: src/datetime-parse.py
    :language: python
    :caption: Datetime parsing from string

Tabelka parametrów formatowania i parsowania dat i czasu
--------------------------------------------------------
.. note:: Prawie wszystkie parametry są podobne różnych językach programowania. Od czasu do czasu występują małe zmiany, np. w JavaScript minuty to ``i`` a nie ``M``

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
.. literalinclude:: src/datetime-shift.py
    :language: python
    :caption: Shifting datetimes

.. literalinclude:: src/datetime-timedelta.py
    :language: python
    :caption: Substract time from datetimes

Konwersja Timestamp Unix Timestamp -> Microsoft Timestamp
---------------------------------------------------------
.. literalinclude:: src/datetime-mstimestamp.py
    :name: code-datetime-mstimestamp
    :language: python
    :caption: Konwersja Timestamp Unix Timestamp -> Microsoft Timestamp

Strefy czasowe
--------------
.. literalinclude:: src/datetime-tzinfo.py
    :language: python
    :caption: Make timezone aware object from naive datetime


``pytz``
========
.. literalinclude:: src/datetime-pytz.py
    :language: python
    :caption: ``pytz`` brings the Olson tz database into Python.

This library allows accurate and cross platform timezone calculations using Python 2.4 or higher. It also solves the issue of ambiguous times at the end of daylight saving time, which you can read more about in the Python Library Reference (datetime.tzinfo).


``calendar``
============
.. literalinclude:: src/calendar-html.py
    :language: python
    :caption: HTML Calendar


``time``
========
.. literalinclude:: src/time-sleep.py
    :language: python
    :caption: Time sleep function

.. literalinclude:: src/time-timestamp.py
    :language: python
    :caption: Get timestamp

.. literalinclude:: src/time-format.py
    :language: python
    :caption: Time formatting

.. literalinclude:: src/time-parse.py
    :language: python
    :caption: Time parsing

.. literalinclude:: src/time-timezone.py
    :language: python
    :caption: Timezone information for time


``timeit``
==========
.. literalinclude:: src/timeit.sh
    :language: console
    :caption: Timeit

.. literalinclude:: src/timeit.py
    :language: python
    :caption: Timeit


Zadania kontrolne
=================

Manipulacja datami
------------------
#. Dane są dwie następujące daty w formacie jak poniżej:

.. code-block:: python

    date1 = 'April 12, 1961 2:07 local time'  # ALMT Timezone
    date2 = '"07/21/69 2:56:15 AM UTC"'

#. Co to za daty, które podał użytkownik?
#. Przedstaw daty jako obiekt ``datetime``. I wyświetl je w formacie ISO.
#. Odejmij obie daty od siebie. Ile lat i miesięcy minęło między wydarzeniami?
#. Do dzisiejszej daty dodaj ten sam czas, który Ci wyszedł w poprzednim punkcie.
#. Wyświetl samą datę (bez czasu).
#. Ile będziesz miał wtedy lat?
#. Przyjmij:

    - rok = 365 dni
    - miesiac = 30 dni

:Założenia:
    * Nazwa pliku: ``datetime-deltas.py``
    * Szacunkowa długość kodu: około 15 linii
    * Maksymalny czas na zadanie: 20 min

:Zadanie z gwiazdką:
    * Uwzględnij strefy czasowe.
