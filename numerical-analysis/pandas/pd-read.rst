***********
Pandas Read
***********


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
    header = pd.read_csv(DATA, nrows=0).columns

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
==========
* If the extension is ``.gz``, ``.bz2``, ``.zip``, and ``.xz``, the corresponding compression method is automatically selected

.. code-block:: python

    df = pd.read_json('sample_file.gz', compression='infer')


Assignments
===========

Pandas Read CSV
---------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/pandas_read_csv_dates.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``URL`` to ``df: pd.DataFrame``
    #. Parse dates in "Mission Date" column

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``URL`` do ``df: pd.DataFrame``
    #. Sparsuj daty w kolumnie "Mission Date"

:Input:
    .. code-block:: python

        URL = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/astro-dates.csv'

:Hint:
    * ``parse_dates`` argument

Pandas Read CSV
---------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/pandas_read_csv_replace.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``URL`` to ``DataFrame``
    #. Use provided column names in ``COLUMNS``
    #. Read labels from the first row
    #. Replace data in ``label`` column with values extracted above
    #. Print ``DataFrame``
    #. Print first 5 and last 10 rows from ``df: pd.DataFrame``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``URL`` do ``DataFrame``
    #. Użyj podanych w ``COLUMNS`` nazw kolumn
    #. Wczytaj nazwy labeli z pierwszego wiersza
    #. Podmień dane w kolumnie ``label`` na wartości wyciągnięte powyżej
    #. Wypisz pierwsze 5 i ostatnie 10 wierszy z ``df: pd.DataFrame``

:Input:
    .. code-block:: python

        URL = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/breast-cancer.csv'

        COLUMNS = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
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
    * ``df['label'].replace({'from': 'to'}, inplace=True)``
    * ``df.last()``

Pandas Read JSON
----------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/pandas_read_json.py`

:English:
    #. Use data from "Input" section (see below)
    #. Using ``pd.read_json()`` read data from ``URL``
    #. Print ``df: pd.DataFrame``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Za pomocą ``pd.read_json()`` wczytaj dane z ``URL``
    #. Wypisz ``df: pd.DataFrame``

:Input:
    .. code-block:: python

        URL = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/iris.json'

Pandas Read HTML
----------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/pandas_read_html.py`

:English:
    #. Use data from "Input" section (see below)
    #. Using ``pd.read_html()`` read data from ``URL``
    #. Print ``df: pd.DataFrame`` with active European Space Agency astronauts

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Za pomocą ``pd.read_html()`` wczytaj dane z ``URL``
    #. Wypisz ``df: pd.DataFrame`` z aktywnymi astronautami Europejskiej Agencji Kosmicznej

:Input:
    .. code-block:: python

        URL = 'https://en.wikipedia.org/wiki/European_Astronaut_Corps'

:Hint:
    * Might require ``lxml``: ``pip install lxml``
    * 3rd table

Pandas Read XML XSLT
--------------------
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/pandas_read_xml_xslt.py`

:English:
    #. Download :download:`data/plants.xml`
    #. Read data from file
    #. Using XSLT transformation convert it to pandas readable format
    #. Read data to ``df: pd.DataFrame``
    #. Make sure that columns and indexes are named properly
    #. Calculate average cost of flower

:Polish:
    #. Pobierz dane z pliku :download:`data/plants.xml`
    #. Zaczytaj dane z pliku
    #. Używając transformaty XSLT sprowadź je do formatu zrozumiałego dla Pandas
    #. Wczytaj dane do ``df: pd.DataFrame``
    #. Upewnij się, że nazwy kolumn i indeks są dobrze ustawione
    #. Wylicz średni koszt kwiatów

:Hint:
    * Require ``lxml``: ``pip install lxml``
