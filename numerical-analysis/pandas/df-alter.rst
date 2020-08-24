***************
DataFrame Alter
***************


Add Rows and Columns
====================
.. code-block:: python
    :caption: Add Column

    import pandas as pd

    df = pd.DataFrame({
        'A': [10, 11, 12],
        'B': [20, 21, 22],
        'C': [30, 31, 32]})

    df
    #     A   B   C
    # 0  10  20  30
    # 1  11  21  31
    # 2  12  22  32

    df['Z'] = np.arange(3.0)
    #     A   B   C    Z
    # 0  10  20  30  0.0
    # 1  11  21  31  1.0
    # 2  12  22  32  2.0

    df['X'] = ['a', 'b']
    # ValueError: Length of values does not match length of index

    df['X'] = ['a', 'b', 'c']
    #     A   B   C    Z  X
    # 0  10  20  30  0.0  a
    # 1  11  21  31  1.0  b
    # 2  12  22  32  2.0  c

.. code-block:: python
    :caption: Add Row

    import pandas as pd

    df = pd.DataFrame({
        'A': [10, 11, 12],
        'B': [20, 21, 22],
        'C': [30, 31, 32]})

    df
    #     A   B   C
    # 0  10  20  30
    # 1  11  21  31
    # 2  12  22  32

    df.append({'A': 77, 'B': 88, 'C': 99})
    # TypeError: Can only append a Series if ignore_index=True or if the Series has a name

    df.append({'A': 77, 'B': 88, 'C': 99}, ignore_index=True)
    #     A   B   C
    # 0  10  20  30
    # 1  11  21  31
    # 2  12  22  32
    # 3  77  88  99


Drop Rows and Columns
=====================
* Works with ``inplace=True``

.. code-block:: python
    :caption: Drop Column

    import pandas as pd

    df = pd.DataFrame({
        'A': [10, 11, 12],
        'B': [20, 21, 22],
        'C': [30, 31, 32]})

    df
    #     A   B   C
    # 0  10  20  30
    # 1  11  21  31
    # 2  12  22  32

    df.drop('A', axis='columns')
    #     B   C
    # 0  20  30
    # 1  21  31
    # 2  22  32

    df.drop(columns='A')
    #     B   C
    # 0  20  30
    # 1  21  31
    # 2  22  32

    df.drop(columns=['A', 'B'])
    #     C
    # 0  30
    # 1  31
    # 2  32

.. code-block:: python
    :caption: Drop Row

    import pandas as pd

    df = pd.DataFrame({
        'A': [10, 11, 12],
        'B': [20, 21, 22],
        'C': [30, 31, 32]})

    df
    #     A   B   C
    # 0  10  20  30
    # 1  11  21  31
    # 2  12  22  32

    df.drop(1)
    #     A   B   C
    # 0  10  20  30
    # 2  12  22  32

    df.drop([0,2])
    #     A   B   C
    # 1  11  21  31

    rows = df1[:2].index
    df.drop(rows)
    #     A   B   C
    # 2  12  22  32

.. code-block:: python
    :caption: Drop from Timeseries

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

    df.drop(pd.Timestamp('1999-12-30'))
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Transpose
=========
* ``df.transpose()`` or ``df.T``
* ``df.transpose()`` is preferred

.. code-block:: python

    import pandas as pd

    df = pd.DataFrame({
        'A': [10, 11, 12],
        'B': [20, 21, 22],
        'C': [30, 31, 32]})

    df
    #     A   B   C
    # 0  10  20  30
    # 1  11  21  31
    # 2  12  22  32

    df.transpose()
    #     0   1   2
    # A  10  11  12
    # B  20  21  22
    # C  30  31  32

    df.T
    #     0   1   2
    # A  10  11  12
    # B  20  21  22
    # C  30  31  32

.. note:: In Pandas you can select columns by either ``df.A`` or ``df['A']``

.. code-block:: python

    df = pd.DataFrame({
        'A': [10, 11, 12],
        'B': [20, 21, 22],
        'C': [30, 31, 32]})

    df['A']         # will select column A
    df.A            # will select column A

    df.T            # will transpose data
    df.transpose()  # will transpose data

.. code-block:: python

    df = pd.DataFrame({
        'R': [10, 11, 12],
        'S': [20, 21, 22],
        'T': [30, 31, 32]})

    df['T']         # will select column T
    df.T            # will select column T
    df.transpose()  # will transpose data


Assignments
===========
.. todo:: Create assignments
