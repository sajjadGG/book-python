**********
Data Types
**********


Common types
============

Series
------
.. code-block:: python

    import pandas as pd


    pd.Series([1., 2., 3., 4.])
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    4.0
    # dtype: float64

DataFrame
---------
.. code-block:: python

    import pandas as pd


    df = pd.DataFrame({
        'A': ['a', 'b', 'c', 'd'],
        'B': [0, 1, 2, 3],
        'C': [0., 1., 2., 3.]})

    #    A  B    C
    # 0  a  0  0.0
    # 1  b  1  1.0
    # 2  c  2  2.0
    # 3  d  3  3.0

Sparse data
-----------
* Data where a single value is repeated many times (e.g. ``0`` or ``NaN``) may be stored efficiently as a ``SparseArray``

.. code-block:: python

    import pandas as pd


    sa = pd.SparseArray([1, 2, 3])
    # [1, 2, 3]
    # Fill: 0
    # IntIndex
    # Indices: array([0, 1, 2], dtype=int32)

.. code-block:: python

    import pandas as pd


    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': pd.SparseArray([np.nan, np.nan, np.nan])})

    #    A   B
    # 0  1 NaN
    # 1  2 NaN
    # 2  3 NaN

    df.dtypes
    # A                   int64
    # B    Sparse[float64, nan]
    # dtype: object


Datetime
========

.. csv-table:: Offset aliases
    :header: "Alias", "Description"

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

Timestamp
---------
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

Period
------
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Period.html

.. code-block:: python

    import pandas as pd


    apollo11 = pd.Period('1969-07-16', '9D')

    apollo11.start_time
    # Timestamp('1969-07-16 00:00:00')

    apollo11.end_time
    # Timestamp('1969-07-24 23:59:59.999999999')

DateOffset
----------
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

    march - pd.DateOffset(day=1)
    # Timestamp('1970-03-01 00:00:00')

Timedelta
---------
* Represents a duration, the difference between two dates or times


Numerical
=========

Interval
--------
.. code-block:: python

    import pandas as pd


    pd.Interval(0, 5)
    # Interval(0, 5, closed='right')

    pd.Interval(left=0, right=5)
    # Interval(0, 5, closed='right')

    pd.Interval(left=0, right=5, closed='both')
    Interval(0, 5, closed='both')

Interval
--------
.. code-block:: python

    import pandas as pd


    interval = pd.Interval(0, 5, closed='left')

    2.5 in interval
    # True

    5.0 in interval
    # False


.. code-block:: python

    import pandas as pd


    year_1970 = pd.Interval(left=pd.Timestamp('1970-01-01 00:00:00'),
                            right=pd.Timestamp('1971-01-01 00:00:00'),
                            closed='left')

    apollo11 = pd.Timestamp('1969-07-16')
    apollo13 = pd.Timestamp('1970-04-11')

    apollo11 in year_1970
    # False

    apollo13 in year_1970
    # True

    year_1970.length
    # Timedelta('365 days 00:00:00')


Text
====

Categorical
-----------
* Limited, fixed set of values

.. code-block:: python

    import pandas as pd


    iris = pd.Categorical(['setosa', 'virginica', 'versicolor'])
    # [setosa, virginica, versicolor]
    # Categories (3, object): [setosa, versicolor, virginica]

    'arctica' in iris
    # False

.. code-block:: python

    import pandas as pd


    moon_landings = pd.Categorical(['apollo11', 'apollo12', 'apollo14', 'apollo15', 'apollo16', 'apollo17'])
    # [apollo11, apollo12, apollo14, apollo15, apollo16, apollo17]
    # Categories (6, object): [apollo11, apollo12, apollo14, apollo15, apollo16, apollo17]

    'apollo11' in moon_landings
    # True

    'apollo13' in moon_landings
    # False

.. code-block:: python

    import pandas as pd


    status = pd.Categorical(['todo', 'done', 'todo', 'done'])
    # [todo, done, todo, done]
    # Categories (2, object): [done, todo]

    'in progress' in status
    # False

    'todo' in status
    # True

    status.categories
    # Index(['done', 'todo'], dtype='object')
