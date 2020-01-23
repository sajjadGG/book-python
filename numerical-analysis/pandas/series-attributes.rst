*****************
Series Attributes
*****************


.. code-block:: python

    import pandas as pd


    data = ['a', 'b', 'c']
    s = pd.Series(data)

    s.shape
    # (3,)

    s.ndim
    # 1

    s.index
    # RangeIndex(start=0, stop=3, step=1)

    s.values
    # array(['a', 'b', 'c'], dtype=object)


Assignments
===========
.. todo:: Create assignments
