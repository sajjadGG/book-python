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
.. code-block:: python

    import pandas as pd


    pd.date_range('1970-01-01', periods=3, freq='D')
    # DatetimeIndex(['1970-01-01', '1970-01-02', '1970-01-03'], dtype='datetime64[ns]', freq='D')

    pd.date_range('1970-01-01', periods=3, freq='M')
    # DatetimeIndex(['1970-01-31', '1970-02-28', '1970-03-31'], dtype='datetime64[ns]', freq='M')

    pd.date_range('1970-01-01', periods=3, freq='Y')
    # DatetimeIndex(['1970-12-31', '1971-12-31', '1972-12-31'], dtype='datetime64[ns]', freq='A-DEC')


Timestamp
=========
* subclass of ``datetime.datetime``
* pandas' scalar type for timezone-naive or timezone-aware datetime data
* https://pandas.pydata.org/pandas-docs/stable/reference/arrays.html#timedelta-data

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


DateOffset
==========
* A relative time duration that respects calendar arithmetic
* For example, ``Bday`` defines the set of dates that are weekdays (M-F)
* To test if a date is in the ``DateOffset`` use: dateOffset.onOffset(date).

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


    march = pd.Timestamp('1970-03-01 00:00:00')

    march - pd.DateOffset(days=1)
    # Timestamp('1970-02-28 00:00:00')


Timedelta
=========
* An absolute time duration. Similar to datetime.timedelta from the standard library
* Represents a duration, the difference between two dates or times
* Timedeltas are differences in times, expressed in difference units, e.g. days, hours, minutes, seconds. They can be both positive and negative.

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


Assignments
===========
.. todo:: Create assignments
