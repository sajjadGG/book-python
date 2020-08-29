***************
Method Chaining
***************


Inplace
=======
.. code-block:: python

    DATA = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]

    s = pd.Series(DATA)
    s.fillna(0, inplace=True)
    s.drop([2,4,6], inplace=True)
    s.drop_duplicates(inplace=True)
    s.reset_index(drop=True, inplace=True)
    s
    # 0    1.0
    # 1    0.0
    # 2    2.0
    # 3    inf
    # dtype: float64

Endl
====
.. code-block:: python

    DATA = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]

    s = pd.Series(DATA) \
            .fillna(0) \
            .drop([2,4,6]) \
            .drop_duplicates() \
            .reset_index(drop=True)

    s
    # 0    1.0
    # 1    0.0
    # 2    2.0
    # 3    inf
    # dtype: float64


Chain
=====
.. code-block:: python

    DATA = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]

    s = (pd.Series(DATA)
            .fillna(0)
            .drop([2,4,6])
            .drop_duplicates()
            .reset_index(drop=True))

    s
    # 0    1.0
    # 1    0.0
    # 2    2.0
    # 3    inf
    # dtype: float64


Further Reading
===============
* https://stackoverflow.com/a/59335777


Assignments
===========
.. todo:: Create assignments
