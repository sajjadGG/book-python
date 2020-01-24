*****************
DataFrame Mapping
*****************

.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    df = pd.DataFrame(
        columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
        index = pd.date_range('1999-12-30', periods=7),
        data = np.random.randn(7, 4))

    df
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Map
===
* ``.map()`` works element-wise on a Series

.. code-block:: python

    df['Morning'].map(lambda value: round(value, 2))
    # 1999-12-30    1.76
    # 1999-12-31    1.87
    # 2000-01-01   -0.10
    # 2000-01-02    0.76
    # 2000-01-03    1.49
    # 2000-01-04   -2.55
    # 2000-01-05    2.27
    # Freq: D, Name: Morning, dtype: float64

.. code-block:: python

    df['Morning'].map(int)
    # 1999-12-30    1
    # 1999-12-31    1
    # 2000-01-01    0
    # 2000-01-02    0
    # 2000-01-03    1
    # 2000-01-04   -2
    # 2000-01-05    2
    # Freq: D, Name: Morning, dtype: int64


Apply
=====
* ``.apply()`` works on a row / column basis of a DataFrame

.. code-block:: python

    df['Morning'].apply(int)
    # 1999-12-30    1
    # 1999-12-31    1
    # 2000-01-01    0
    # 2000-01-02    0
    # 2000-01-03    1
    # 2000-01-04   -2
    # 2000-01-05    2
    # Freq: D, Name: Morning, dtype: int64

.. code-block:: python

    df['Morning'].apply(lambda value: round(value, 2))
    # 1999-12-30    1.76
    # 1999-12-31    1.87
    # 2000-01-01   -0.10
    # 2000-01-02    0.76
    # 2000-01-03    1.49
    # 2000-01-04   -2.55
    # 2000-01-05    2.27

Applymap
========
* ``.applymap()`` works element-wise on a DataFrame


Assignments
===========
.. todo:: Create assignments
