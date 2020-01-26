****************
DataFrame Import
****************


Import data
===========
* File paths works also with URLs
* SQL functions uses SQLAlchemy, which supports many RDBMS

.. code-block:: python

    import pandas as pd


    # Important
    pd.read_csv()
    pd.read_excel()
    pd.read_html()
    pd.read_json()
    pd.read_sql()        # Read SQL query or database table into a DataFrame

    # Others
    pd.read_clipboard()
    pd.read_feather()
    pd.read_fwf()
    pd.read_gbq()
    pd.read_hdf()
    pd.read_msgpack()
    pd.read_parquet()
    pd.read_pickle()
    pd.read_sas()
    pd.read_spss()
    pd.read_sql_query()  # Read SQL query into a DataFrame
    pd.read_sql_table()  # Read SQL database table into a DataFrame
    pd.read_stata()
    pd.read_table()


Examples
========
.. code-block:: python

    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/iris.csv'

    df = pd.read_csv(DATA)

    df.head(3)
    #    sepal_length  sepal_width  petal_length  petal_width     species
    # 0           5.4          3.9           1.3          0.4      setosa
    # 1           5.9          3.0           5.1          1.8   virginica
    # 2           6.0          3.4           4.5          1.6  versicolor

.. code-block:: python

    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/iris-dirty.csv'

    df = pd.read_csv(DATA)

    df.head(3)
    #      150    4  setosa  versicolor  virginica
    # 0    5.4  3.9     1.3         0.4          0
    # 1    5.9  3.0     5.1         1.8          2
    # 2    6.0  3.4     4.5         1.6          1

    df = pd.read_csv(url, skiprows=1, names=['sepal_length', 'sepal_width',
                                             'petal_length', 'petal_width', 'species'])
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


Assignments
===========

Read
-----
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/pandas_read.py`

:English:
    #. Read data from given ``url`` (see below) to ``DataFrame``
    #. Use provided column names
    #. Read labels from the first row
    #. Replace data in ``label`` column with values extracted above
    #. Print ``DataFrame``
    #. Print first 5 and last 10 rows from ``DataFrame``

:Polish:
    #. Wczytaj dane z danego ``url`` (patrz poniżej) do ``DataFrame``
    #. Użyj podanych nazw kolumn
    #. Wczytaj nazwy labeli z pierwszego wiersza
    #. Podmień dane w kolumnie ``label`` na wartości wyciągnięte powyżej
    #. Wypisz pierwsze 5 i ostatnie 10 wierszy z ``DataFrame``

:Input:
    .. code-block:: python

        DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/breast-cancer.csv'

        column_names = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
                        'mean smoothness', 'mean compactness', 'mean concavity',
                        'mean concave points', 'mean symmetry', 'mean fractal dimension',
                        'radius error', 'texture error', 'perimeter error', 'area error',
                        'smoothness error', 'compactness error', 'concavity error',
                        'concave points error', 'symmetry error',
                        'fractal dimension error', 'worst radius', 'worst texture',
                        'worst perimeter', 'worst area', 'worst smoothness',
                        'worst compactness', 'worst concavity', 'worst concave points',
                        'worst symmetry', 'worst fractal dimension', 'label']

:The whys and wherefores:
    * Read Pandas ``DataFrame``

:Hint:
    * ``pd.read_csv(url, nrows=0).columns``
    * ``df['label'].replace({'from': 'to'})``

XSLT Transformation
-------------------
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/df_import_xml_xslt.py`

:English:
    #. Download :download:`data/plants.xml`
    #. Read data from file
    #. Using XSLT transformation convert it to pandas readable format
    #. Read data to ``pd.DataFrame``
    #. Make sure that columns and indexes are named properly
    #. Calculate average cost of flower

:Polish:
    #. Pobierz dane z pliku :download:`data/plants.xml`
    #. Zaczytaj dane z pliku
    #. Używając transformaty XSLT sprowadź je do formatu zrozumiałego dla Pandas
    #. Wczytaj dane do ``pd.DataFrame``
    #. Upewnij się, że nazwy kolumn i indeks są dobrze ustawione
    #. Wylicz średni koszt kwiatów
