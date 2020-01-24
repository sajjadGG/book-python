**************
DataFrame Sort
**************


.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    data = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    index = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(data, index, columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

Sort Rows
=========
* Works with ``inplace=True``

.. code-block:: python
    :caption: Sort descending

    df.sort_index(ascending=False)
    df.sort_index(ascending=False, axis=0)
    df.sort_index(ascending=False, axis='rows')

.. code-block:: python
    :caption: Sort ascending

    df.sort_index(ascending=True)
    df.sort_index(ascending=True, axis=0)
    df.sort_index(ascending=True, axis='rows')

Sort Columns
============
* Works with ``inplace=True``

.. code-block:: python
    :caption: Sort descending

    df.sort_index(ascending=False, axis=1)
    df.sort_index(ascending=False, axis='columns')

.. code-block:: python
    :caption: Sort ascending

    df.sort_index(ascending=True, axis=1)
    df.sort_index(ascending=True, axis='columns')


Sort Values
===========
* Works with ``inplace=True``

.. code-block:: python
    :caption: Sorting values by column

    df.sort_values('Morning', ascending=True)
    df.sort_values('Morning', ascending=False)

.. code-block:: python
    :caption: Sorting values by multiple columns (if values are equal in first column, than compare second)

    df.sort_values(['Morning', 'Evening'], ascending=True)
    df.sort_values(['Morning', 'Evening'], ascending=False)

.. code-block:: python
    :caption: Sorting whole DataFrame, according to values by in row (change column order)

    df.sort_values('1970-01-05', ascending=True, axis=1)
    df.sort_values('1970-01-05', ascending=True, axis='columns')

Assignments
===========
.. todo:: Create assignments
