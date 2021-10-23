Pandas Read CSV
===============


Rationale
---------
* File paths works also with URLs


Header
------
.. code-block:: python

    import pandas as pd


    DATA = 'https://python.astrotech.io/_static/iris-clean.csv'
    header = pd.read_csv(DATA, nrows=0).columns


Content
-------
.. code-block:: python

    import pandas as pd


    DATA = 'https://python.astrotech.io/_static/iris-clean.csv'
    df = pd.read_csv(DATA)

    df.head(3)
    #    sepal_length  sepal_width  petal_length  petal_width     species
    # 0           5.4          3.9           1.3          0.4      setosa
    # 1           5.9          3.0           5.1          1.8   virginica
    # 2           6.0          3.4           4.5          1.6  versicolor


Rename Columns
--------------
.. code-block:: python

    import pandas as pd


    DATA = 'https://python.astrotech.io/_static/iris-dirty.csv'
    COLUMNS =  ['sepal_length', 'sepal_width',
                'petal_length', 'petal_width', 'species']

    df = pd.read_csv(DATA)
    df.head(3)
    #      150    4  setosa  versicolor  virginica
    # 0    5.4  3.9     1.3         0.4          0
    # 1    5.9  3.0     5.1         1.8          2
    # 2    6.0  3.4     4.5         1.6          1

    df = pd.read_csv(url, skiprows=1, names=COLUMNS)
    df.head(3)
    #    sepal_length  sepal_width  petal_length  petal_width  species
    # 0           5.4          3.9           1.3          0.4        0
    # 1           5.9          3.0           5.1          1.8        2
    # 2           6.0          3.4           4.5          1.6        1

    df['species'].replace({
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica',
    }, inplace=True)
    #    sepal_length  sepal_width  petal_length  petal_width  species
    # 0           5.4          3.9           1.3          0.4        setosa
    # 1           5.9          3.0           5.1          1.8        virginica
    # 2           6.0          3.4           4.5          1.6        versicolor


Compressed
----------
* If the extension is ``.gz``, ``.bz2``, ``.zip``, and ``.xz``, the corresponding compression method is automatically selected

.. code-block:: python

    df = pd.read_csv('myfile.gz', compression='infer')



Use Case
--------
.. code-block:: python

    DATA = 'https://python.astrotech.io/_static/iris-dirty.csv'

    COLUMNS =  ['sepal_length', 'sepal_width',
                'petal_length', 'petal_width', 'species']


    species = pd.read_csv(DATA, nrows=0)
    species = dict(enumerate(species.columns[2:]))

    df = pd.read_csv(DATA, names=COLUMNS, skiprows=1)
    df['species'].replace(species, inplace=True)


Assignments
-----------
.. literalinclude:: assignments/pandas_read_csv_dates.py
    :caption: :download:`Solution <assignments/pandas_read_csv_dates.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_read_csv_replace.py
    :caption: :download:`Solution <assignments/pandas_read_csv_replace.py>`
    :end-before: # Solution
