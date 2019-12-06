*****************
Series Attributes
*****************


Shape
=====

.. code-block:: python

    import pandas as pd

    data = [1, 2, 3]
    s = pd.Series(data)

    s.shape
    # (3,)

    s.ndim
    # 1

.. code-block:: python

    import pandas as pd


    space_race = pd.date_range(start='1961-04-12', end='1969-07-21', freq='D')

    len(space_race)
    # 3023

    space_race.shape
    # (3023,)

    space_race.ndim
    # 1


Dtype
=====
.. code-block:: python

    import pandas as pd


    space_race = pd.date_range(start='1961-04-12', end='1969-07-21', freq='D')

    space_race.dtype
    # dtype('<M8[ns]')


Date
====
.. code-block:: python

    import pandas as pd


    space_race = pd.date_range(start='1961-04-12', end='1969-07-21', freq='D')

    space_race.freq
    # <Day>

    space_race.array
    # <DatetimeArray>
    # ['1961-04-12 00:00:00', '1961-04-13 00:00:00', '1961-04-14 00:00:00',
    #  '1961-04-15 00:00:00', '1961-04-16 00:00:00', '1961-04-17 00:00:00',
    #  '1961-04-18 00:00:00', '1961-04-19 00:00:00', '1961-04-20 00:00:00',
    #  '1961-04-21 00:00:00',
    #  ...
    #  '1969-07-12 00:00:00', '1969-07-13 00:00:00', '1969-07-14 00:00:00',
    #  '1969-07-15 00:00:00', '1969-07-16 00:00:00', '1969-07-17 00:00:00',
    #  '1969-07-18 00:00:00', '1969-07-19 00:00:00', '1969-07-20 00:00:00',
    #  '1969-07-21 00:00:00']
    # Length: 3023, dtype: datetime64[ns]

    space_race.values
    # array(['1961-04-12T00:00:00.000000000', '1961-04-13T00:00:00.000000000',
    #        '1961-04-14T00:00:00.000000000', ...,
    #        '1969-07-19T00:00:00.000000000', '1969-07-20T00:00:00.000000000',
    #        '1969-07-21T00:00:00.000000000'], dtype='datetime64[ns]')



Assignments
===========
.. todo:: Create assignments
