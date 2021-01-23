Series Attributes
*****************


Size
====
.. code-block:: python

    import pandas as pd

    s = pd.Series(['a', 'b', 'c'])

    s.size
    # 3


NDim
====
* Number of Dimensions

.. code-block:: python

    import pandas as pd

    s = pd.Series(['a', 'b', 'c'])

    s.ndim
    # 1


Shape
=====
.. code-block:: python

    import pandas as pd

    s = pd.Series(['a', 'b', 'c'])

    s.shape
    # (3,)



Index
=====
* More information in :ref:`Pandas Series Index`.

.. code-block:: python

    import pandas as pd

    s = pd.Series(['a', 'b', 'c'])

    s
    # 0    a
    # 1    b
    # 2    c
    # dtype: object

    s.index
    # RangeIndex(start=0, stop=3, step=1)


Values
======
.. code-block:: python

    import pandas as pd

    s = pd.Series(['a', 'b', 'c'])

    s.values
    # array(['a', 'b', 'c'], dtype=object)


Assignments
===========
.. literalinclude:: assignments/pandas_series_attributes.py
    :caption: :download:`Solution <assignments/pandas_series_attributes.py>`
    :end-before: # Solution
