********************
DataFrame Statistics
********************

.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    data = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    index = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(data, index, columns)

Arithmetic mean
---------------
.. code-block:: python

    df.mean()
    # A   -0.078742
    # B    0.241929
    # C    0.110231
    # D   -0.092946
    # dtype: float64

Descriptive stats
-----------------
.. code-block:: python

    df.describe()
    #               A          B          C          D
    # count  6.000000   6.000000   6.000000   6.000000
    # mean  -0.078742   0.241929   0.110231  -0.092946
    # std    0.690269   0.845521   0.746167   1.207483
    # min   -0.928127  -0.931601  -0.812575  -1.789321
    # 25%   -0.442016  -0.275899  -0.359650  -0.638282
    # 50%   -0.202288   0.287667  -0.045933  -0.332729
    # 75%    0.189195   0.882916   0.733453   0.902115
    # max    1.062487   1.190259   1.036800   1.323504

Percentiles
-----------
.. code-block:: python

    data = np.array([[1, 1], [2, 10], [3, 100], [4, 100]])
    columns = ['a', 'b']

    df = pd.DataFrame(data, columns)
    #    a    b
    # 0  1    1
    # 1  2   10
    # 2  3  100
    # 3  4  100

.. code-block:: python

    df.quantile(.1)
    # a    1.3
    # b    3.7
    # dtype: float64

.. code-block:: python

    df.quantile([.1, .5])
    #        a     b
    # 0.1  1.3   3.7
    # 0.5  2.5  55.0

Other methods
-------------
.. csv-table:: Descriptive statistics
    :header-rows: 1

    "Function", "Description"
    "``count``", "Number of non-null observations"
    "``sum``", "Sum of values"
    "``mean``", "Mean of values"
    "``mad``", "Mean absolute deviation"
    "``median``", "Arithmetic median of values"
    "``min``", "Minimum"
    "``max``", "Maximum"
    "``mode``", "Mode"
    "``abs``", "Absolute Value"
    "``prod``", "Product of values"
    "``std``", "Unbiased standard deviation"
    "``var``", "Unbiased variance"
    "``sem``", "Unbiased standard error of the mean"
    "``skew``", "Unbiased skewness (3rd moment)"
    "``kurt``", "Unbiased kurtosis (4th moment)"
    "``quantile``", "Sample quantile (value at %)"
    "``cumsum``", "Cumulative sum"
    "``cumprod``", "Cumulative product"
    "``cummax``", "Cumulative maximum"
    "``cummin``", "Cumulative minimum"


Assignments
===========

Cars
----
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 45 min
* Filename: :download:`solution/df_cars.py`

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
