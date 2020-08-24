*********
Series NA
*********


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


Select
======
.. code-block:: python

    s.any()
    s.all()
    s.isnull()
    s.isna()


Update
======
.. code-block:: python
    :caption: Fill NA - Scalar value. Has ``inplace=True`` parameter.

    s.fillna(0.0)
    # 0    1.0
    # 1    0.0
    # 2    0.0
    # 3    4.0
    # 4    0.0
    # 5    6.0
    # dtype: float64

.. code-block:: python
    :caption: Forward Fill. ``ffill``: propagate last valid observation forward. Has ``inplace=True`` parameter.

    s.ffill()
    # 0    1.0
    # 1    1.0
    # 2    1.0
    # 3    4.0
    # 4    4.0
    # 5    6.0
    # dtype: float64

.. code-block:: python
    :caption: Backward Fill. ``bfill``: use NEXT valid observation to fill gap.  Has ``inplace=True`` parameter.

    s.bfill()
    # 0    1.0
    # 1    4.0
    # 2    4.0
    # 3    4.0
    # 4    6.0
    # 5    6.0
    # dtype: float64

.. code-block:: python
    :caption: Interpolate. ``method: str``, default ``linear``

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
      - Fill in NA using existing values

    * - ``nearest``, ``zero``, ``slinear``, ``quadratic``, ``cubic``, ``spline``, ``barycentric``, ``polynomial``
      - Passed to ``scipy.interpolate.interp1d``. These methods use the numerical values of the index.  Both ``polynomial`` and ``spline`` require that you also specify an ``order`` (int), e.g. ``df.interpolate(method='polynomial', order=5)``

    * - ``krogh``, ``piecewise_polynomial``, ``spline``, ``pchip``, ``akima``
      - Wrappers around the SciPy interpolation methods of similar names

    * - ``from_derivatives``
      - Refers to ``scipy.interpolate.BPoly.from_derivatives`` which replaces ``piecewise_polynomial`` interpolation method in scipy 0.18.


Drop
====
.. code-block:: python
    :caption: Drop Rows. Has ``inplace=True`` parameter.

    import pandas as pd
    import numpy as np

    s = pd.Series([1.0, 2.0, 3.0, np.nan, 5.0])

    s.dropna()
    # 0    1.0
    # 1    2.0
    # 2    2.0
    # 4    5.0
    # dtype: float64


Assignments
===========
.. todo:: Create Assignments
