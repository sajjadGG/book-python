*********
Timezones
*********


Time zones in ``datetime`` library
==================================
* Always keep dates and times only in UTC (**important!**)
* Datetimes should be converted to localtime only when displaying to user
* Computerphile Time & Time Zones :cite:`VideoComputerphileTimeZones`

Timezone naive
--------------
.. code-block:: python
    :caption: Timezone naive datetimes

    from datetime import datetime

    datetime.now()

.. code-block:: python
    :caption: Timezone naive datetimes. This is potentially dangerous!

    from datetime import datetime

    datetime.utcnow()

.. code-block:: python
    :caption: Timezone naive datetimes

    from datetime import datetime

    datetime(1957, 10, 4, 19, 28, 34)

Timezone aware
--------------
.. code-block:: python
    :caption: Timezone aware datetime

    from datetime import datetime, timezone

    datetime(1957, 10, 4, 19, 28, 34, tzinfo=timezone.utc)

.. code-block:: python
    :caption: Timezone aware datetime

    from datetime import datetime, timezone

    dt = datetime(1957, 10, 4, 19, 28, 34)
    d.replace(tzinfo=timezone.utc)

.. code-block:: python
    :caption: Timezone aware datetime

    from datetime import datetime, timezone

    datetime.now(tz=timezone.utc)


``pytz``
========

List of Timezones
-----------------
* https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
* https://www.iana.org/time-zones

.. code-block:: python
    :caption: ``pytz`` brings the Olson tz database into Python.

    from pytz import timezone


    timezone('UTC')
    timezone('US/Eastern')
    timezone('Europe/Warsaw')
    timezone('Asia/Almaty')

From naive to local
-------------------
.. code-block:: python
    :caption: From naive to local time

    from datetime import datetime
    from pytz import timezone


    # timezone naive
    my_date = datetime(1961, 4, 12, 14, 7)

    timezone('Asia/Almaty').localize(my_date)
    # datetime.datetime(1961, 4, 12, 14, 7,
    #                   tzinfo=<DstTzInfo 'Asia/Almaty' +06+6:00:00 STD>)

From naive to UTC
-----------------
.. code-block:: python
    :caption: From naive to local time

    from datetime import datetime


    # timezone naive
    my_date = datetime(1961, 4, 12, 14, 7)

    timezone('UTC').localize(my_date)
    # datetime.datetime(1961, 4, 12, 14, 7, tzinfo=<UTC>)

From UTC to local time
----------------------
.. code-block:: python
    :caption: From UTC to local time

    from datetime import datetime
    from pytz import timezone


    my_date = datetime(1969, 7, 21, 14, 56, 15, tzinfo=timezone('UTC'))

    my_date.astimezone(timezone('Europe/Warsaw'))
    # datetime.datetime(1969, 7, 21, 15, 56, 15,
    #                   tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)

Between timezones
-----------------
.. code-block:: python
    :caption: Between timezones

    from datetime import datetime
    from pytz import timezone


    my_date = datetime(1961, 4, 12, 14, 7, tzinfo=timezone('Asia/Almaty'))

    my_date.astimezone(timezone('Europe/Warsaw'))
    # datetime.datetime(1961, 4, 12, 9, 59,
    #                   tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)


Assignments
===========

Time zone converting
--------------------
* Filename: :download:`solution/datetime_tz.py`
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min

#. Dane są dwie następujące daty w formacie jak poniżej:

    .. code-block:: python

        gagarin = 'April 12, 1961 2:07 local time'  # Asia/Almaty
        armstrong = '"07/21/69 2:56:15 AM UTC"'

#. Przedstaw daty jako obiekt ``datetime`` ze strefą czasową UTC
#. Wyświetl obie daty w formacie *ISO* w strefie czasowej ``Europe/Warsaw``

:Hint:
    * Wpisz "local time" jako zwykły tekst w parametrze ``fmt`` funkcji ``.strptime()``
    * Wpisz znaki cudzysłowia ``"`` jako zwykły tekst w parametrze ``fmt`` funkcji ``.strptime()``
    * Standard ISO:

        * '1961-04-12'
        * '1961-04-12T06:07:00Z'
        * '1961-04-12T06:07:00.123456Z'
