*************
DataFrame NaN
*************


.. code-block:: python

    import pandas as pd
    import numpy as np

    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C    D
    # 0  1.0  1.1    a  NaN
    # 1  2.0  2.2    b  NaN
    # 2  NaN  NaN  NaN  NaN
    # 3  NaN  NaN  NaN  NaN
    # 4  3.0  3.3    c  NaN
    # 5  NaN  NaN  NaN  NaN
    # 6  4.0  4.4    d  NaN


Find NaN
========

Any
---
.. code-block:: python

    df.any()
    # A     True
    # B     True
    # C     True
    # D    False
    # dtype: bool

All
---
.. code-block:: python

    df.all()
    # A    True
    # B    True
    # C    True
    # D    True
    # dtype: bool

Is Null
-------
.. code-block:: python

    df.isnull()
    #        A      B      C     D
    # 0  False  False  False  True
    # 1  False  False  False  True
    # 2   True   True   True  True
    # 3   True   True   True  True
    # 4  False  False  False  True
    # 5   True   True   True  True
    # 6  False  False  False  True

Is NA
-----
.. code-block:: python

    df.isna()
    #        A      B      C     D
    # 0  False  False  False  True
    # 1  False  False  False  True
    # 2   True   True   True  True
    # 3   True   True   True  True
    # 4  False  False  False  True
    # 5   True   True   True  True
    # 6  False  False  False  True


Fill NaN
========

With scalar value
-----------------
* ``axis=0`` - rows
* ``axis=1`` - columns

.. code-block:: python

    df.fillna(0.0)
    #      A    B  C    D
    # 0  1.0  1.1  a  0.0
    # 1  2.0  2.2  b  0.0
    # 2  0.0  0.0  0  0.0
    # 3  0.0  0.0  0  0.0
    # 4  3.0  3.3  c  0.0
    # 5  0.0  0.0  0  0.0
    # 6  4.0  4.4  d  0.0

With dict values
----------------
* ``axis=0`` - rows
* ``axis=1`` - columns

.. code-block:: python

    df.fillna({
        'A': 99,
        'B': 88,
        'C': 77
    })
    #       A     B   C    D
    # 0   1.0   1.1   a  NaN
    # 1   2.0   2.2   b  NaN
    # 2  99.0  88.0  77  NaN
    # 3  99.0  88.0  77  NaN
    # 4   3.0   3.3   c  NaN
    # 5  99.0  88.0  77  NaN
    # 6   4.0   4.4   d  NaN

Forward Fill
------------
* Values from previous row
* ``ffill``: propagate last valid observation forward

.. code-block:: python

    df.fillna(method='ffill')
    #      A    B  C    D
    # 0  1.0  1.1  a  NaN
    # 1  2.0  2.2  b  NaN
    # 2  2.0  2.2  b  NaN
    # 3  2.0  2.2  b  NaN
    # 4  3.0  3.3  c  NaN
    # 5  3.0  3.3  c  NaN
    # 6  4.0  4.4  d  NaN

Backward Fill
-------------
* Values from next row
* ``bfill``: use NEXT valid observation to fill gap

.. code-block:: python

    df.fillna(method='bfill')
    #      A    B  C    D
    # 0  1.0  1.1  a  NaN
    # 1  2.0  2.2  b  NaN
    # 2  3.0  3.3  c  NaN
    # 3  3.0  3.3  c  NaN
    # 4  3.0  3.3  c  NaN
    # 5  4.0  4.4  d  NaN
    # 6  4.0  4.4  d  NaN

Interpolate
-----------
.. code-block:: python

    df.interpolate()
    #           A         B    C    D
    # 0  1.000000  1.100000    a  NaN
    # 1  2.000000  2.200000    b  NaN
    # 2  2.333333  2.566667  NaN  NaN
    # 3  2.666667  2.933333  NaN  NaN
    # 4  3.000000  3.300000    c  NaN
    # 5  3.500000  3.850000  NaN  NaN
    # 6  4.000000  4.400000    d  NaN


Drop NaN
========

Drop Rows
---------
* ``axis=0`` - rows

.. code-block:: python

    df.dropna(how='all')
    #      A    B  C    D
    # 0  1.0  1.1  a  NaN
    # 1  2.0  2.2  b  NaN
    # 4  3.0  3.3  c  NaN
    # 6  4.0  4.4  d  NaN

    df.dropna(how='all', axis='rows')
    #      A    B  C    D
    # 0  1.0  1.1  a  NaN
    # 1  2.0  2.2  b  NaN
    # 4  3.0  3.3  c  NaN
    # 6  4.0  4.4  d  NaN

    df.dropna(how='all', axis=0)
    #      A    B  C    D
    # 0  1.0  1.1  a  NaN
    # 1  2.0  2.2  b  NaN
    # 4  3.0  3.3  c  NaN
    # 6  4.0  4.4  d  NaN

.. code-block:: python

    df.dropna(how='any')
    # Empty DataFrame
    # Columns: [A, B, C, D]
    # Index: []

    df.dropna(how='any', axis=0)
    # Empty DataFrame
    # Columns: [A, B, C, D]
    # Index: []

    df.dropna(how='any', axis='rows')
    # Empty DataFrame
    # Columns: [A, B, C, D]
    # Index: []

Drop Column
-----------
* ``axis=1`` - columns

.. code-block:: python

    df.dropna(how='all', axis='columns')
    #      A    B    C
    # 0  1.0  1.1    a
    # 1  2.0  2.2    b
    # 2  NaN  NaN  NaN
    # 3  NaN  NaN  NaN
    # 4  3.0  3.3    c
    # 5  NaN  NaN  NaN
    # 6  4.0  4.4    d

    df.dropna(how='all', axis=1)
    #      A    B    C
    # 0  1.0  1.1    a
    # 1  2.0  2.2    b
    # 2  NaN  NaN  NaN
    # 3  NaN  NaN  NaN
    # 4  3.0  3.3    c
    # 5  NaN  NaN  NaN
    # 6  4.0  4.4    d

    df.dropna(how='all', axis=-1)
    # ValueError: No axis named -1 for object type <class 'pandas.core.frame.DataFrame'>

.. code-block:: python

    df.dropna(how='any', axis='columns')
    # Empty DataFrame
    # Columns: []
    # Index: [0, 1, 2, 3, 4, 5, 6]

    df.dropna(how='any', axis=1)
    # Empty DataFrame
    # Columns: []
    # Index: [0, 1, 2, 3, 4, 5, 6]

    df.dropna(how='any', axis=-1)
    # ValueError: No axis named -1 for object type <class 'pandas.core.frame.DataFrame'>


Assignments
===========

Iris Dirty
----------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/df_update.py`


#. Pobierz dane Irysów: :download:`data/iris-dirty.csv`
#. Mając dane Irysów przekonwertuj je na ``DataFrame``
#. Pomiń pierwszą linię z metadanymi
#. Zmień nazwy kolumn na:

    * Sepal length
    * Sepal width
    * Petal length
    * Petal width
    * Species

#. Podmień wartości w kolumnie species

    - 0 -> 'setosa',
    - 1 -> 'versicolor',
    - 2 -> 'virginica'

#. Zastąp ustaw na ``NaN`` wszystkie wartości wartości w kolumnie 'Petal length' mniejsze od 4
#. Interpoluj liniowo wszystkie wartości ``NaN``
#. Usuń wiersze z pozostałymi wartościami ``NaN``
#. Wyświetl pierwsze 2 i ostatni wiersz
#. Wykreśl podstawowe statystyki opisowe

