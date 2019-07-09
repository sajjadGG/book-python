**********************
Parsing and Formatting
**********************


* https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

Date formats
============
* https://en.wikipedia.org/wiki/Date_format_by_country

Date format in USA
------------------
.. code-block:: text
    :caption: Formal date format in USA :cite:`DateFormatUS`

    4/12/61
    April 12, 1961

Date format in Japan
--------------------
.. code-block:: text
    :caption: Formal date format in Japan :cite:`DateFormatJapan`

    20/12/31

Date format in Germany
----------------------
.. code-block:: text
    :caption: Formal date format in Germany

    12.04.1961

Date format in Poland
---------------------
* Which format is a formal standard in Poland?
* https://en.wikipedia.org/wiki/ISO_8601

.. code-block:: text

    12.4.1961
    12.04.1961

.. code-block:: text

    12 IV 1961
    12.IV.1961

.. code-block:: text

    12/4/1961
    12/04/1961

.. code-block:: text

    12 kwietnia 1961
    12 kwiecień 1961


Time formats
============

24 and 12 hour clock
--------------------
* What AM stands for?
* What PM stands for?

.. code-block:: text

    17:00
    5:00 PM

Noon and Midnight
-----------------
* Which time is a midnight?
* Which time is a noon?
* `Confusion at noon and midnight <https://en.wikipedia.org/wiki/12-hour_clock#Confusion_at_noon_and_midnight>`_

.. code-block:: text

    12:00 am
    12:00 pm

.. code-block:: text
    :caption: Is 12:00 a noon (in 24h format), or someone just simply forgot to put AM/PM?

    12:00

.. code-block:: text

    12:00
    24:00

.. code-block:: text

    00:00
    0:00

Times after 24:00
-----------------
* `Times after 24:00 <https://en.wikipedia.org/wiki/24-hour_clock#Times_after_24:00>`_

.. code-block:: text

    23:59:59
    23:59:60

.. code-block:: text

    24:00
    24:01
    25:00
    27:45
    14:00-30:00

Military time
-------------
* `Military time <https://en.wikipedia.org/wiki/24-hour_clock#Military_time>`_
* `Military time zones <https://en.wikipedia.org/wiki/List_of_military_time_zones>`_

.. code-block:: text

    1200J


ISO 8601 Standard
=================
* https://en.wikipedia.org/wiki/ISO_8601

Dates
-----
.. code-block:: text

   1961-04-12

Date and time
-------------
* "Z" (Zulu) means UTC
* "T" separates date and time

.. code-block:: text
    :caption: Date and time with second precision

    1961-04-12T06:07:00Z

.. code-block:: text
    :caption: Date and time with with millisecond precision

    1961-04-12T06:07:00.123Z

.. code-block:: text
    :caption: Date and time with microsecond precision

    1961-04-12T06:07:00.123456Z

Noon and Midnight
-----------------
* "00:00" - midnight, at the beginning of a day (more frequent)
* "24:00" - midnight, at the end of a day
* "2007-04-05T24:00" is equal to "2007-04-06T00:00"

Weeks
-----
* Note year/month changes during the week

.. code-block:: text
    :caption: First week of 2009

    2009-W01

.. code-block:: text
    :caption: Monday 29 December 2008

    2009-W01-1

.. code-block:: text
    :caption: Sunday 3 January 2010

    2009-W53-7

Timezone
--------
* "Z" (Zulu) means UTC

.. code-block:: text

    <time>Z
    <time>±hh:mm
    <time>±hhmm
    <time>±hh

Duration
--------
* Format: ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``

.. csv-table:: Duration format
    :header: "Format", "Designator", "Description"
    :widths: 10, 15, 75

    "``P``", "duration (period)",  "placed at the start of the duration representation"
    "``Y``", "year",  "number of years"
    "``M``", "month",  "number of months"
    "``W``", "week",  "number of weeks"
    "``D``", "day",  "number of days"
    "``T``", "time",  "precedes the time components of the representation"
    "``H``", "hour",  "number of hours"
    "``M``", "minute",  "number of minutes"
    "``S``", "second",  "number of seconds"

.. code-block:: text
    :caption: Example

    P8Y3M9DT8H49M15S

    # Period of:
    #   8 years
    #   3 months
    #   9 days
    #   8 hours
    #   49 minutes
    #   5 seconds


Table of date and time parsing and formatting parameters
========================================================
.. note:: Prawie wszystkie parametry są podobne różnych językach programowania. Od czasu do czasu występują małe zmiany, np. w JavaScript minuty to ``i`` a nie ``M``

.. csv-table:: Tabelka parametrów formatowania i parsowania dat i czasu
    :header-rows: 1
    :file: data/datetime-formatting.csv


Date formatting
===============

``f-string`` formatting
-----------------------
.. code-block:: python
    :caption: Datetime formatting as string with ``f'...'``

    from datetime import datetime

    gagarin = datetime(1961, 4, 12, 6, 7)

    print(f'Gagarin launched on {gagarin:%Y-%m-%d}')
    # Gagarin launched on 1961-04-12

.. code-block:: python
    :caption: Datetime formatting as string with ``f'...'``

    from datetime import datetime

    gagarin = datetime(1961, 4, 12, 6, 7)

    print(f'Gagarin launched on {gagarin:%Y-%m-%d %H:%M}')
    # Gagarin launched on 1961-04-12 06:07

.. code-block:: python
    :caption: Datetime formatting as string with ``f'...'``

    from datetime import datetime

    gagarin = datetime(1961, 4, 12, 6, 7)
    format = '%Y-%m-%d %H:%M'

    print(f'Gagarin launched on {gagarin:{format}}')
    # Gagarin launched on 1961-04-12  06:07

Format to string
----------------
.. code-block:: python
    :caption: Datetime formatting as string with ``.strftime()``

    from datetime import datetime

    gagarin = datetime(1961, 4, 12, 6, 7)
    formatted = gagarin.strftime('%Y-%m-%d %H:%M')

    print(f'Gagarin launched on {formatted}')
    # Gagarin launched on 1961-04-12 06:07

ISO Format
----------
.. code-block:: python
    :caption: Datetime formatting to ISO format

    from datetime import datetime

    dt = datetime(1969, 7, 21, 14, 56, 15)

    dt.isoformat()
    # 1969-07-21T14:56:15

.. code-block:: python
    :caption: Date formatting to ISO format

    from datetime import date

    d = date(1969, 7, 21)

    d.isoformat()
    # 1969-07-21


Parsing dates
=============
* Parsing - analyze (a sentence) into its parts and describe their syntactic roles.

.. code-block:: python
    :caption: Datetime parsing from string

    from datetime import datetime

    sputnik = '4 October 1957, 19:28:34 [UTC]'

    out = datetime.strptime(sputnik, '%d %B %Y, %H:%M:%S [%Z]')
    # datetime.datetime(1957, 10, 4, 19, 28, 34)

    print(out)
    # 1957-10-04 19:28:34


Assignments
===========

From ISO date format
--------------------
* Filename: :download:`solution/datetime_from_iso.py`
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Input data: :numref:`listing-time-from-iso`

#. Datę:

    .. code-block:: text
        :name: listing-time-from-iso
        :caption: Convert ``str`` from ISO date format to ``datetime`` objects

        1969-07-21T14:56:15.123Z

#. Przedstaw datę jako obiekt ``datetime``

To ISO date format
------------------
* Filename: :download:`solution/datetime_to_iso.py`
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min

#. Datę:

    .. code-block:: python

        gagarin = 'April 12, 1961 2:07 local time'  # Asia/Almaty

#. Przekonwertuj do obiektu ``datetime``
#. Wyświetl w formacie ISO datę i czas, tj.:

    .. code-block:: text
        :caption: "Rok-Miesiąc-DzieńTGodzina:Minuta:Sekunda.MikrosekundyZ"

        1961-04-12T06:07:00.123456

US date and time format
-----------------------
* Filename: :download:`solution/datetime_from_us.py`
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min

#. Rozczytaj datę z formatu amerykańskiego długiego (skopiuj z cudzysłowami):

    .. code-block:: python

        armstrong = '"June 21st, 1969 2:56:15 AM UTC"'

#. Wyświetl datę w formacie amerykańskim krótkim:

    .. code-block:: text
        :caption: "Miesiąc/Dzień/Rok Godzina:Minuta AM/PM"

        7/21/69 2:56 AM

:Hint:
    * Wpisz "local time" jako zwykły tekst w parametrze ``fmt`` funkcji ``.strptime()``
    * Wpisz znaki cudzysłowia ``"`` jako zwykły tekst w parametrze ``fmt`` funkcji ``.strptime()``
