**********
Date Types
**********


Date frequency
==============
.. csv-table:: Offset aliases
    :header: "Alias", "Description"
    :widths: 15, 85

    "``B``",            "business day frequency"
    "``C``",            "custom business day frequency"
    "``D``",            "calendar day frequency"
    "``W``",            "weekly frequency"
    "``M``",            "month end frequency"
    "``SM``",           "semi-month end frequency (15th and end of month)"
    "``BM``",           "business month end frequency"
    "``CBM``",          "custom business month end frequency"
    "``MS``",           "month start frequency"
    "``SMS``",          "semi-month start frequency (1st and 15th)"
    "``BMS``",          "business month start frequency"
    "``CBMS``",         "custom business month start frequency"
    "``Q``",            "quarter end frequency"
    "``BQ``",           "business quarter end frequency"
    "``QS``",           "quarter start frequency"
    "``BQS``",          "business quarter start frequency"
    "``A``, ``Y``",     "year end frequency"
    "``BA``, ``BY``",   "business year end frequency"
    "``AS``, ``YS``",   "year start frequency"
    "``BAS``, ``BYS``", "business year start frequency"
    "``BH``",           "business hour frequency"
    "``H``",            "hourly frequency"
    "``T``, ``min``",   "minutely frequency"
    "``S``",            "secondly frequency"
    "``L``, ``ms``",    "milliseconds"
    "``U``, ``us``",    "microseconds"
    "``N``",            "nanoseconds"

.. csv-table:: Date frequency units
    :header: "Frequency", "Letter", "Long name", "Short name"
    :widths: 15, 5, 40, 40

    "Year",         "``Y``"
    "Month",        "``M``"
    "Week",         "``W``"
    "Day",          "``D``", "``day``, ``days``"
    "Hour",         "``H``", "``hour``, ``hours``",                 "``h``, ``hr``"
    "Minute",       "``T``", "``minute``, ``minutes``",             "``m``, ``min``"
    "Second",       "``S``", "``second``, ``seconds``",             "``sec``"
    "Millisecond",  "``L``", "``millisecond``, ``milliseconds``",   "``ms``, ``milli``, ``millis``"
    "Microsecond",  "``U``", "``microsecond``, ``microseconds``",   "``us``, ``micro``, ``micros``"
    "Nanosecond",   "``N``", "``nanosecond``, ``nanoseconds``",     "``ns``, ``nano``, ``nanos``"


Generate dates
==============

Days in a row
-------------
.. code-block:: python

    import pandas as pd


    pd.date_range('1970-01-01', periods=3, freq='D')
    # DatetimeIndex(['1970-01-01', '1970-01-02', '1970-01-03'], dtype='datetime64[ns]', freq='D')

    pd.date_range('1970-01-01', periods=3, freq='M')
    # DatetimeIndex(['1970-01-31', '1970-02-28', '1970-03-31'], dtype='datetime64[ns]', freq='M')

    pd.date_range('1970-01-01', periods=3, freq='Y')
    # DatetimeIndex(['1970-12-31', '1971-12-31', '1972-12-31'], dtype='datetime64[ns]', freq='A-DEC')

Days between
------------
.. code-block:: python

    from datetime import datetime
    import pandas as pd


    start = datetime(1969, 7, 16)
    end = datetime(1969, 7, 21)

    pd.date_range(start, end)
    # DatetimeIndex(['1969-07-16', '1969-07-17', '1969-07-18',
    #                '1969-07-19', '1969-07-20', '1969-07-21'],
    #                dtype='datetime64[ns]', freq='D')

Business days
-------------
.. code-block:: python

    from pandas.tseries.holiday import USFederalHolidayCalendar
    from pandas.tseries.offsets import CustomBusinessDay


    business_days = CustomBusinessDay(calendar=USFederalHolidayCalendar())

    pd.date_range(start='2019-12-24',end='2019-12-31', freq=business_days)
    # DatetimeIndex(['2019-12-24', '2019-12-26', '2019-12-27',
    #                '2019-12-30', '2019-12-31'],
    #                dtype='datetime64[ns]', freq='C')

.. code-block:: python

    from datetime import datetime, time
    import pandas as pd
    from pandas.tseries.holiday import USFederalHolidayCalendar


    today = datetime(2014, 1, 17, 15)


    bhour_us = pd.offsets.CustomBusinessHour(
        calendar=USFederalHolidayCalendar(),
        start='08:00',
        end=time(16, 0),
        weekmask='Mon Tue Wed Thu Fri')


    dt+bhour_us

Custom Calendar
---------------
.. code-block:: python

    import pandas as pd
    from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, EasterMonday, Easter
    from pandas.tseries.offsets import Day, CustomBusinessDay


    class PLHolidayCalendar(AbstractHolidayCalendar):
        """
        Holiday calendar for Poland
        """
        rules = [
            Holiday('New Years Day', month=1, day=1),
            Holiday('Epiphany', month=1, day=6),
            Holiday('Easter', month=1, day=1, offset=[Easter()]),
            EasterMonday,
            Holiday('May Day', month=5, day=1),
            Holiday('Constitution Day', month=5, day=3),
            Holiday('Pentecost Sunday', month=1, day=1, offset=[Easter(), Day(49)]),
            Holiday('Corpus Christi', month=1, day=1, offset=[Easter(), Day(60)]),
            Holiday('Assumption of the Blessed Virgin Mary', month=8, day=15),
            Holiday('All Saints Day', month=11, day=1),
            Holiday('Independence Day', month=11, day=11),
            Holiday('Christmas Day', month=12, day=25),
            Holiday('Second Day of Christmastide', month=12, day=26),
        ]


    pl_holidays_2019 = PLHolidayCalendar().holidays(start='2019-01-01', end='2019-12-31')
    # DatetimeIndex(['2019-01-01', '2019-01-06', '2019-04-21', '2019-04-22',
    #                '2019-05-01', '2019-05-03', '2019-06-09', '2019-06-20',
    #                '2019-08-15', '2019-11-01', '2019-11-11', '2019-12-25',
    #                '2019-12-26'],
    #               dtype='datetime64[ns]', freq=None)


    BUSINESS_DAY = CustomBusinessDay(
        calendar=PLHolidayCalendar(),
        weekmask='Mon Tue Wed Thu Fri')

    today = pd.Timestamp('2000-01-01 00:00')

    today + 2*BUSINESS_DAY
    # Timestamp('2000-01-04 00:00:00')

    today + 3*BUSINESS_DAY
    # Timestamp('2000-01-05 00:00:00')

    today + 4*BUSINESS_DAY
    # Timestamp('2000-01-07 00:00:00')

    today + 5*BUSINESS_DAY
    # Timestamp('2000-01-10 00:00:00')

Custom mask
-----------
.. code-block:: python

    from datetime import datetime
    import pandas as pd


    start = datetime(1970, 12, 1)
    end = datetime(1970, 12, 31)
    weekmask = 'Mon Tue Wed Thu Fri'
    holidays = [datetime(1970, 12, 25), datetime(1970, 12, 26)]

    pd.bdate_range(start, end, freq='C', weekmask=weekmask, holidays=holidays)
    # DatetimeIndex(['1970-12-01', '1970-12-02', '1970-12-03', '1970-12-04',
    #                '1970-12-07', '1970-12-08', '1970-12-09', '1970-12-10',
    #                '1970-12-11', '1970-12-14', '1970-12-15', '1970-12-16',
    #                '1970-12-17', '1970-12-18', '1970-12-21', '1970-12-22',
    #                '1970-12-23', '1970-12-24', '1970-12-28', '1970-12-29',
    #                '1970-12-30', '1970-12-31'],
    #                dtype='datetime64[ns]', freq='C')


Timestamp
=========
* subclass of ``datetime.datetime``
* pandas' scalar type for timezone-naive or timezone-aware datetime data
* https://pandas.pydata.org/pandas-docs/stable/reference/arrays.html#timedelta-data

Timezone naive
--------------
.. code-block:: python

    import pandas as pd


    pd.Timestamp('1961-04-12')
    # Timestamp('1961-04-12 00:00:00')

    pd.Timestamp('1961-04-12T06:07:00')
    # Timestamp('1961-04-12 06:07:00')

    pd.Timestamp('1961-04-12 6:07')
    # Timestamp('1961-04-12 06:07:00')

.. code-block:: python

    import pandas as pd


    pd.Timestamp('12/4/69')
    # Timestamp('1969-12-04 00:00:00')

    pd.Timestamp('12/4/69, 6:07')
    # Timestamp('1969-12-04 06:07:00')

    pd.Timestamp('12/4/69, 6:07 pm')
    # Timestamp('1969-12-04 18:07:00')

.. code-block:: python
    :caption: 2016-12-31 23:59:60 is a valid date (UTC leap second)

    import pandas as pd


    pd.Timestamp('2016-12-31 23:59:60')
    # ValueError: second must be in 0..59

Timezone aware
--------------
.. code-block:: python

    import pandas as pd


    gagarin = pd.Timestamp('1961-04-12 12:07:00', tz='Asia/Almaty')

    gagarin.astimezone('UTC')
    # Timestamp('1961-04-12 06:07:00+0000', tz='UTC')

    gagarin.astimezone('Europe/Moscow')
    #Timestamp('1961-04-12 09:07:00+0300', tz='Europe/Moscow')

    gagarin.astimezone('Europe/Warsaw')
    # Timestamp('1961-04-12 07:07:00+0100', tz='Europe/Warsaw')

    gagarin.astimezone('EST')
    # Timestamp('1961-04-12 01:07:00-0500', tz='EST')

    gagarin.astimezone('America/New_York')
    # Timestamp('1961-04-12 01:07:00-0500', tz='America/New_York')

.. code-block:: python

    import pandas as pd


    armstrong = pd.Timestamp('1969-07-21 2:56:15', tz='UTC')

    armstrong.tz_convert('Europe/Warsaw')
    # Timestamp('1969-07-21 03:56:15+0100', tz='Europe/Warsaw')

    armstrong.astimezone('Europe/Warsaw')
    # Timestamp('1969-07-21 03:56:15+0100', tz='Europe/Warsaw')


Period
======
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Period.html

.. code-block:: python

    import pandas as pd


    apollo11 = pd.Period('1969-07-16', '9D')

    apollo11.start_time
    # Timestamp('1969-07-16 00:00:00')

    apollo11.end_time
    # Timestamp('1969-07-24 23:59:59.999999999')


Timedelta
=========
* Represents a duration, the difference between two dates or times
* Difference expressed in: days, hours, minutes, seconds
* Similar to ``datetime.timedelta`` from the standard library
* Can be both positive and negative.

.. code-block:: python

    import pandas as pd


    pd.Timedelta('1 day')
    # Timedelta('1 days 00:00:00')

    pd.Timedelta(days=1)
    # Timedelta('1 days 00:00:00')

.. code-block:: python

    import pandas as pd


    feb = pd.Timestamp('2001-02-28')
    mar = pd.Timestamp('2001-03-01')

    feb + pd.Timedelta(days=1)
    # Timestamp('2001-03-01 00:00:00')

    mar - pd.Timedelta(days=1)
    # Timestamp('2001-02-28 00:00:00')

.. code-block:: python

    import pandas as pd


    feb = pd.Timestamp('2000-02-28')
    mar = pd.Timestamp('2000-03-01')

    feb + pd.Timedelta(days=1)
    # Timestamp('2000-02-29 00:00:00')

    feb + pd.Timedelta(days=2)
    # Timestamp('2000-03-01 00:00:00')

    mar - pd.Timedelta(days=1)
    # Timestamp('2000-02-29 00:00:00')

.. code-block:: python
    :caption: Leap second has not been added

    import pandas as pd


    leap = pd.Timestamp('2016-12-31 23:59:59')

    leap + pd.Timedelta(seconds=1)
    # Timestamp('2017-01-01 00:00:00')


DateOffset
==========
* A relative time duration that respects calendar arithmetic
* If a date is Sat then adding a ``Bday`` will return the next Monday (next Business day) instead of a Saturday
* Test if a date is in the ``DateOffset().onOffset(date)``

.. code-block:: python

    import pandas as pd


    first_step = pd.Timestamp('1969-07-21 02:56:15')

    first_step + pd.DateOffset(months=3)
    # Timestamp('1969-10-21 02:56:15')

.. code-block:: python

    import pandas as pd


    epoch = pd.Timestamp('1970-01-01 00:00:00')

    epoch + pd.DateOffset(month=3)
    # Timestamp('1970-03-01 00:00:00')


.. code-block:: python

    import pandas as pd


    mar = pd.Timestamp('1970-03-01 00:00:00')

    mar - pd.DateOffset(days=1)
    # Timestamp('1970-02-28 00:00:00')


Assignments
===========
.. todo:: Create assignments
