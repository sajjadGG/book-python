*************
Series Update
*************


.. code-block:: python

    import pandas as pd
    import numpy as np

    s = pd.Series([1.0, np.nan, np.nan, 4.0, np.nan, 6.0])

    s
    # 0    1.0
    # 1    NaN
    # 2    NaN
    # 3    4.0
    # 4    NaN
    # 5    6.0
    # dtype: float64


Fill NaN - Scalar value
=======================
* Can use with ``inplace=True``

.. code-block:: python

    s.fillna(0.0)
    # 0    1.0
    # 1    0.0
    # 2    0.0
    # 3    4.0
    # 4    0.0
    # 5    6.0
    # dtype: float64


Fill NaN - Forward Fill
=======================
* Can use with ``inplace=True``

.. code-block:: python

    s.ffill()
    # 0    1.0
    # 1    1.0
    # 2    1.0
    # 3    4.0
    # 4    4.0
    # 5    6.0
    # dtype: float64


Fill NaN - Backward Fill
========================
* Can use with ``inplace=True``

.. code-block:: python

    s.bfill()
    # 0    1.0
    # 1    4.0
    # 2    4.0
    # 3    4.0
    # 4    6.0
    # 5    6.0
    # dtype: float64


Fill NaN - Interpolate
======================
* ``method: str``, default ``linear``

.. list-table:: Interpolation techniques
    :widths: 25, 75
    :header-rows: 1

    * - Method
      - Description

    * - ``linear``
      - Ignore the index and treat the values as equally spaced. This is the only method supported on MultiIndexes

    * - ``time``
      - Works on daily and higher resolution data to interpolate given length of interval

    * - ``index``, ``values``
      - use the actual numerical values of the index.

    * - ``pad``
      - Fill in NaNs using existing values

    * - ``nearest``, ``zero``, ``slinear``, ``quadratic``, ``cubic``, ``spline``, ``barycentric``, ``polynomial``
      - Passed to ``scipy.interpolate.interp1d``. These methods use the numerical values of the index.  Both ``polynomial`` and ``spline`` require that you also specify an ``order`` (int), e.g. ``df.interpolate(method='polynomial', order=5)``

    * - ``krogh``, ``piecewise_polynomial``, ``spline``, ``pchip``, ``akima``
      - Wrappers around the SciPy interpolation methods of similar names

    * - ``from_derivatives``
      - Refers to ``scipy.interpolate.BPoly.from_derivatives`` which replaces ``piecewise_polynomial`` interpolation method in scipy 0.18.

.. code-block:: python

    s.interpolate()
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    4.0
    # 4    5.0
    # 5    6.0
    # dtype: float64

    s.interpolate('nearest')
    # 0    1.0
    # 1    1.0
    # 2    4.0
    # 3    4.0
    # 4    4.0
    # 5    6.0
    # dtype: float64

    s.interpolate('polynomial', order=2)
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    4.0
    # 4    5.0
    # 5    6.0
    # dtype: float64
