***********
Time Deltas
***********


Time shifts
===========
.. code-block:: python
    :caption: Shifting datetime objects

    from datetime import datetime


    gagarin = datetime(1961, 4, 12, 6, 7)
    armstrong = datetime(1969, 7, 21, 14, 56, 15)

    between_dates = armstrong - gagarin    # datetime.timedelta(3022, 31755)

    between_dates                          # 3022 days, 8:49:15
    between_dates.days                     # 3022
    between_dates.seconds                  # 31755
    between_dates.total_seconds()          # 261132555.0 (days * seconds per day + seconds)


``timedelta``
=============

Simple ``timedelta`` shifts
---------------------------
.. code-block:: python
    :caption: Simple ``timedelta`` shifts

    from datetime import timedelta, datetime


    gagarin = datetime(1961, 4, 12)

    gagarin - timedelta(minutes=15)
    gagarin + timedelta(minutes=10)


.. code-block:: python
    :caption: Simple ``timedelta`` shifts

    from datetime import timedelta, datetime


    armstrong = datetime(1969, 7, 21, 14, 56, 15)

    armstrong - timedelta(hours=21)
    armstrong + timedelta(hours=5)

.. code-block:: python
    :caption: Simple ``timedelta`` shifts

    from datetime import timedelta, date


    sputnik = date(1957, 10, 4)

    sputnik + timedelta(days=5)
    sputnik - timedelta(days=3)

.. code-block:: python
    :caption: Simple ``timedelta`` shifts

    from datetime import datetime, timedelta


    gagarin = datetime(1961, 4, 12)

    gagarin + timedelta(weeks=2)
    gagarin - timedelta(weeks=3)

Complex ``timedelta`` shifts
----------------------------
.. code-block:: python
    :caption: Complex ``timedelta`` shifts


    from datetime import timedelta, datetime


    armstrong = datetime(1969, 7, 21, 14, 56, 15)

    armstrong - timedelta(days=2, hours=21)

.. code-block:: python
    :caption: Complex ``timedelta`` shifts

    from datetime import timedelta, datetime


    armstrong = datetime(1969, 7, 21, 14, 56, 15)

    duration = timedelta(
        weeks=3,
        days=2,
        hours=21,
        minutes=5,
        seconds=12,
        milliseconds=10,
        microseconds=55)
    # datetime.timedelta(days=23, seconds=75912, microseconds=10055)

    between_dates = armstrong - duration
    # datetime.datetime(1969, 6, 27, 17, 51, 2, 989945)


``timedelta`` month shifts
--------------------------
.. code-block:: python
    :caption: Subtract month from ``datetime``

    from datetime import timedelta, date


    def month():
        """Average days a month in solar calendar"""
        return timedelta(days=30.436875)


    month_before = date(1961, 4, 12) - month()
    # datetime.date(1961, 3, 13)


.. todo:: Biblioteka calendar ma funkcję wyliczającą ilość dni w miesiącu


Time diff
=========
.. code-block:: python
    :caption: Diff between datetime objects

    from datetime import datetime


    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    MONTH = 30.436875 * DAY    # Average days a month in solar calendar
    YEAR = 365.2425 * DAY      # Solar calendar


    gagarin = datetime(1961, 4, 12, 6, 7)
    armstrong = datetime(1969, 7, 21, 14, 56, 15)

    duration = armstrong - gagarin
    # datetime.timedelta(3022, 31755)

    years, seconds = divmod(duration.total_seconds(), YEAR)
    months, seconds = divmod(seconds, MONTH)
    days, seconds = divmod(seconds, DAY)
    hours, seconds = divmod(duration.seconds, HOUR)
    minutes, seconds = divmod(seconds, MINUTE)

    difference = {
        'years': int(years),
        'months': int(months),
        'days': int(days),
        'hours': int(hours),
        'minutes': int(minutes),
        'seconds': int(seconds),
    }

    print(difference)
    # {'years': 8, 'months': 3, 'days': 9, 'hours': 8, 'minutes': 49, 'seconds': 15}


Assignments
===========

Date manipulation
------------------
* Filename: ``datetime_deltas.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min

#. Dane są dwie następujące daty w formacie jak poniżej:

    .. code-block:: python

        gagarin = 'April 12, 1961 2:07 local time'  # Asia/Almaty
        armstrong = '"07/21/69 2:56:15 AM UTC"'

#. Przedstaw daty jako obiekt ``datetime``
#. Odejmij obie daty od siebie
#. Oblicz ile lat i miesięcy minęło między wydarzeniami
#. Od obecnej chwili odejmij ten sam czas, który Ci wyszedł w poprzednim punkcie
#. Wyświetl samą datę (bez czasu)
#. Ile miałeś wtedy lat?
#. Przyjmij:

    - rok = 365.2425 dni
    - miesiąc = 30.436875 dni

:Zadanie z gwiazdką:
    * Co robiłeś przez ten czas?

:Hint:
    * Wpisz "local time" jako zwykły tekst do ``strptime``
    * ``datetime.now(tz=timezone.utc)``
    * ``datetime(1961, 04, 12, 6, 7).replace(tz=timezone.utc)``
    * Standard ISO:

        * '1961-04-12'
        * '1961-04-12T06:07:00'
        * '1961-04-12T06:07:00.123456'
