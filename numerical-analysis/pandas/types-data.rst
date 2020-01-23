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


    pd.Series([1., 2., 3., 4.])
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
        'B': [0, 1, 2, 3],
        'C': [0., 1., 2., 3.]})

    #    A  B    C
    # 0  a  0  0.0
    # 1  b  1  1.0
    # 2  c  2  2.0
    # 3  d  3  3.0
