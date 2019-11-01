****************
DataFrame Create
****************


Create DataFrame
================
.. code-block:: python

    import pandas as pd


    df = pd.DataFrame({'A': ['a', 'b', 'c', 'd'],
                       'B': [0, 1, 2, 3],
                       'C': [0., 1., 2., 3.]})
    #    A  B    C
    # 0  a  0  0.0
    # 1  b  1  1.0
    # 2  c  2  2.0
    # 3  d  3  3.0


Indexes
=======

Integer index
-------------
.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    values = np.arange(16).reshape(4, 4)
    indexes = range(0, 4)
    columns = range(0, 4)

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #     0   1   2   3
    # 0   0   1   2   3
    # 1   4   5   6   7
    # 2   8   9  10  11
    # 3  12  13  14  15

Date indexes
------------
.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    values = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    indexes = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #                 Morning        Noon    Evening   Midnight
    # 1970-01-01     2.269755   -1.454366   0.045759  -0.187184
    # 1970-01-02     1.532779    1.469359   0.154947   0.378163
    # 1970-01-03    -0.887786   -1.980796  -0.347912   0.156349
    # 1970-01-04     1.230291    1.202380  -0.387327  -0.302303
    # 1970-01-05    -1.048553   -1.420018  -1.706270   1.950775
    # 1970-01-06    -0.509652   -0.438074  -1.252795   0.777490


Values
======

Custom values in columns
------------------------
.. code-block:: python

    pd.DataFrame({'A' : 1.,
                  'B' : pd.Timestamp('1961-04-12'),
                  'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                  'D' : np.array([3] * 4, dtype='int32'),
                  'E' : pd.Categorical(["test", "train", "test", "train"]),
                  'F' : 'foo' })
    #      A           B    C  D      E    F
    # 0  1.0  1961-04-12  1.0  3   test  foo
    # 1  1.0  1961-04-12  1.0  3  train  foo
    # 2  1.0  1961-04-12  1.0  3   test  foo
    # 3  1.0  1961-04-12  1.0  3  train  foo

With multiple rows
------------------
.. code-block:: python

    pd.DataFrame([{'A': 1, 'B': 2}, {'C': 3}])
    #      A    B    C
    # 0  1.0  2.0  NaN
    # 1  NaN  NaN  3.0


Assignments
===========

Cars
----
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 45 min
* Filename: :download:`solution/pandas_df_cars.py`

#. Stwórz ``DataFrame`` samochody z:

    - losową kolumną liczb całkowitych przebieg z przedziału [0, 200 000]
    - losową kolumną spalanie z przedziału [2, 20]

#. Dodaj kolumnę marka:

    - jeżeli samochód ma spalanie [0, 5] marka to VW
    - jeżeli samochód ma spalanie [6, 10] marka to Ford
    - jeżeli samochód ma spalanie 11 i więcej, marka to UAZ

#. Dodaj kolumnę pochodzenie:

    - jeżeli przebieg poniżej 100 km, pochodzenie nowy
    - jeżeli przebieg powyżej 100 km, pochodzenie uzywany
    - jeżeli przebieg powyżej 100 000 km, pochodzenie z niemiec

#. Przeanalizuj dane statystycznie

    - sprawdź liczność grup
    - wykonaj analizę statystyczną

#. Pogrupuj dane po marce i po pochodzenie
