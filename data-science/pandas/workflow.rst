********
Workflow
********


Import
------
.. code-block:: python

    import pandas as pd

Set Variables
-------------
.. code-block:: python

    url = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'
    columns = [
        'Sepal length',
        'Sepal width',
        'Petal length',
        'Petal width',
        'Species'
    ]

Read data
---------
.. code-block:: python

    df = pd.read_csv(url, skiprows=1, names=columns)

First ``n`` records
-------------------
.. code-block:: python

    df.head(5)
    #    Sepal length  Sepal width  Petal length  Petal width  Species
    # 0           5.1          3.5           1.4          0.2        0
    # 1           4.9          3.0           1.4          0.2        0
    # 2           4.7          3.2           1.3          0.2        0
    # 3           4.6          3.1           1.5          0.2        0
    # 4           5.0          3.6           1.4          0.2        0

Last ``n`` records
------------------
.. code-block:: python

    df.tail(3)
    #      Sepal length  Sepal width  Petal length  Petal width  Species
    # 147           6.5          3.0           5.2          2.0        2
    # 148           6.2          3.4           5.4          2.3        2
    # 149           5.9          3.0           5.1          1.8        2

Change column Species values
----------------------------
.. code-block:: python

    df.Species.replace(to_replace={
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }, inplace=True)

Shuffle columns and reset indexes
---------------------------------
.. code-block:: python

    df = df.sample(frac=1.0).reset_index(drop=True)
    #      Sepal length  Sepal width     ...      Petal width     Species
    # 0             5.0          2.0     ...              1.0  versicolor
    # 1             6.4          2.7     ...              1.9   virginica
    # 2             5.6          3.0     ...              1.5  versicolor
    # 3             5.7          2.6     ...              1.0  versicolor
    # 4             6.4          3.1     ...              1.8   virginica
    # 5             4.6          3.6     ...              0.2      setosa
    # 6             5.9          3.0     ...              1.5  versicolor

Descriptive Statistics
----------------------
.. code-block:: python

    df.describe()
    #        Sepal length  Sepal width  Petal length  Petal width
    # count    150.000000   150.000000    150.000000   150.000000
    # mean       5.843333     3.057333      3.758000     1.199333
    # std        0.828066     0.435866      1.765298     0.762238
    # min        4.300000     2.000000      1.000000     0.100000
    # 25%        5.100000     2.800000      1.600000     0.300000
    # 50%        5.800000     3.000000      4.350000     1.300000
    # 75%        6.400000     3.300000      5.100000     1.800000
    # max        7.900000     4.400000      6.900000     2.500000



Pandas Workflow
===============
.. code-block:: python

    import pandas as pd


    FILE = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'

    df = pd.read_csv(FILE, skiprows=1)

    df.head(5)
    #      5.1  3.5  1.4  0.2  0
    # 0    4.9  3.0  1.4  0.2  0
    # 1    4.7  3.2  1.3  0.2  0
    # 2    4.6  3.1  1.5  0.2  0
    # 3    5.0  3.6  1.4  0.2  0
    # 4    5.4  3.9  1.7  0.4  0

    df.columns = [
        'Sepal length',
        'Sepal width',
        'Petal length',
        'Petal width',
        'Species'
    ]

    df.head(5)
    #    Sepal length  Sepal width  Petal length  Petal width  Species
    # 0           5.1          3.5           1.4          0.2        0
    # 1           4.9          3.0           1.4          0.2        0
    # 2           4.7          3.2           1.3          0.2        0
    # 3           4.6          3.1           1.5          0.2        0
    # 4           5.0          3.6           1.4          0.2        0

    df.tail(3)
    #      Sepal length  Sepal width  Petal length  Petal width  Species
    # 147           6.5          3.0           5.2          2.0        2
    # 148           6.2          3.4           5.4          2.3        2
    # 149           5.9          3.0           5.1          1.8        2

    df['Species'].replace({
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }, inplace=True)

    df = df.sample(frac=1.0)
    #      Sepal length  Sepal width  Petal length  Petal width     Species
    # 120           5.6          2.8           4.9          2.0   virginica
    # 9             5.4          3.7           1.5          0.2      setosa
    # 54            5.7          2.8           4.5          1.3  versicolor
    # 46            4.6          3.2           1.4          0.2      setosa
    # 2             4.6          3.1           1.5          0.2      setosa
    # ...

    df.reset_index(drop=True)
    #      Sepal length  Sepal width     ...      Petal width     Species
    # 0             5.0          2.0     ...              1.0  versicolor
    # 1             6.4          2.7     ...              1.9   virginica
    # 2             5.6          3.0     ...              1.5  versicolor
    # 3             5.7          2.6     ...              1.0  versicolor
    # 4             6.4          3.1     ...              1.8   virginica
    # ...

    df.describe()
    #        Sepal length  Sepal width  Petal length  Petal width
    # count    150.000000   150.000000    150.000000   150.000000
    # mean       5.843333     3.057333      3.758000     1.199333
    # std        0.828066     0.435866      1.765298     0.762238
    # min        4.300000     2.000000      1.000000     0.100000
    # 25%        5.100000     2.800000      1.600000     0.300000
    # 50%        5.800000     3.000000      4.350000     1.300000
    # 75%        6.400000     3.300000      5.100000     1.800000
    # max        7.900000     4.400000      6.900000     2.500000

Hist
----
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd


    INPUT = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/serialization/data/iris.csv'

    df = pd.read_csv(INPUT)
    df.hist()
    plt.show()

.. figure:: img/matplotlib-pd-hist.png
    :scale: 40%
    :align: center

    Visualization using hist

Density
-------
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd


    INPUT = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/serialization/data/iris.csv'


    df = pd.read_csv(INPUT)
    df.plot(kind='density', subplots=True, layout=(2,2), sharex=False)
    plt.show()

.. figure:: img/matplotlib-pd-density.png
    :scale: 40%
    :align: center

    Visualization using density

Box
---
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd


    INPUT = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/serialization/data/iris.csv'


    df = pd.read_csv(INPUT)
    df.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
    plt.show()

.. figure:: img/matplotlib-pd-box.png
    :scale: 40%
    :align: center

    Visualization using density

Scatter matrix
--------------
* The in ``pandas`` version ``0.22`` plotting module has been moved from ``pandas.tools.plotting`` to ``pandas.plotting``
* As of version ``0.19``, the ``pandas.plotting`` library did not exist

.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd
    from pandas.plotting import scatter_matrix


    INPUT = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/serialization/data/iris.csv'


    df = pd.read_csv(INPUT)
    scatter_matrix(df)
    plt.show()

.. figure:: img/matplotlib-pd-scatter-matrix.png
    :scale: 40%
    :align: center

    Visualization using density

Descriptive statistics
----------------------
.. csv-table:: Descriptive statistics
    :header: "Function", "Description"

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
