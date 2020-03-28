**************
Series Mapping
**************


.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    s = pd.Series(
        index = pd.date_range('1999-12-30', periods=7),
        data = np.random.randn(7))

    s
    # 1999-12-30    1.764052
    # 1999-12-31    0.400157
    # 2000-01-01    0.978738
    # 2000-01-02    2.240893
    # 2000-01-03    1.867558
    # 2000-01-04   -0.977278
    # 2000-01-05    0.950088
    # Freq: D, dtype: float64


Map
===
* ``.map()`` works element-wise on a Series

.. code-block:: python

    s.map(int)
    # 1999-12-30    1
    # 1999-12-31    0
    # 2000-01-01    0
    # 2000-01-02    2
    # 2000-01-03    1
    # 2000-01-04    0
    # 2000-01-05    0
    # Freq: D, dtype: int64

.. code-block:: python

    s.map(lambda value: round(value, 2))
    # 1999-12-30    1.76
    # 1999-12-31    0.40
    # 2000-01-01    0.98
    # 2000-01-02    2.24
    # 2000-01-03    1.87
    # 2000-01-04   -0.98
    # 2000-01-05    0.95
    # Freq: D, dtype: float64


Apply
=====
* ``.apply()`` works on a row / column basis of a DataFrame

.. code-block:: python

    s.apply(int)
    # 1999-12-30    1
    # 1999-12-31    0
    # 2000-01-01    0
    # 2000-01-02    2
    # 2000-01-03    1
    # 2000-01-04    0
    # 2000-01-05    0
    # Freq: D, dtype: int64

.. code-block:: python

    s.apply(lambda value: round(value, 2))
    # 1999-12-30    1.76
    # 1999-12-31    0.40
    # 2000-01-01    0.98
    # 2000-01-02    2.24
    # 2000-01-03    1.87
    # 2000-01-04   -0.98
    # 2000-01-05    0.95
    # Freq: D, dtype: float64


Assignments
===========
.. todo:: Create Assignments
