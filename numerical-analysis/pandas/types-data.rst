************
Types Basics
************


Series
======
* 1-dimensional data structure similar to ``ndarray``
* Has index
* Can have name

.. code-block:: python

    import pandas as pd


    pd.Series([1.0, 2.0, 3.0, 4.0])
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    4.0
    # dtype: float64


DataFrame
=========
* 2-dimensional object
* All columns share the same index
* List of ``Series``
* Each column must have name
* Operations can be executed on columns or rows

.. code-block:: python

    import pandas as pd

    df = pd.DataFrame({
        'A': ['a', 'b', 'c', 'd'],
        'B': [11, 22, 33, 44],
        'C': [1.1, 2.2, 3.3, 4.4]})

    #    A   B    C
    # 0  a  11  1.1
    # 1  b  22  2.2
    # 2  c  33  3.3
    # 3  d  44  4.4
