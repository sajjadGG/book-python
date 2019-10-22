**************
DataFrame Join
**************

.. figure:: img/sql-joins.png
    :scale: 50%
    :align: center

    Joins

.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df1 = pd.DataFrame(values, index=indexes, columns=columns)
    df2 = pd.DataFrame([ {'A': 1, 'B': 2},
                         {'C': 3}])

Left Join
---------
.. code-block:: python

    df1.join(df2, how='left', rsuffix='_2')  # gdyby była kolizja nazw kolumn, to dodaj suffix '_2'

.. code-block:: python

    df1.merge(df2, right_index=True, left_index=True, how='left', suffixes=('', '_2'))

Outer Join
----------
.. code-block:: python

    df1.merge(df2)
    df1.merge(df2, how='outer')

Append
------
* jak robi appenda, to nie zmienia indeksów (uwaga na indeksy powtórzone)
* nowy dataframe będzie miał kolejne indeksy

.. code-block:: python

    df1.append(df2)
    df1.append(df2, ignore_index=True)

Concat
------
* Przydatne przy łączeniu dataframe wczytanych z wielu plików

.. code-block:: python

    pd.concat([df1, df2])
    pd.concat([df1, df2], ignore_index=True)
    pd.concat([df1, df2], join='inner')


Assignments
===========

EVA
---
* Complexity level: medium
* Lines of code to write: 25 lines
* Estimated time of completion: 30 min
* Filename: :download:`solution/pandas_df_eva.py`

#. Na podstawie podanych URL:

    * https://www.worldspaceflight.com/bios/eva/eva.php
    * https://www.worldspaceflight.com/bios/eva/eva2.php
    * https://www.worldspaceflight.com/bios/eva/eva3.php
    * https://www.worldspaceflight.com/bios/eva/eva4.php

#. Scrappuj stronę wykorzystując ``pandas.read_html()``
#. Połącz dane wykorzystując ``pd.concat``
#. Przygotuj plik ``CSV`` z danymi dotyczącymi spacerów kosmicznych
