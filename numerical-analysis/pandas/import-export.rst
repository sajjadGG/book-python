**********************
Import and Export Data
**********************


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


Export data
===========
* File paths works also with URLs
* SQL functions uses SQLAlchemy, which supports many RDBMS

.. code-block:: python

    import pandas as pd


    df = pd.DataFrame()

    # Important
    df.to_csv()
    df.to_dict()
    df.to_excel()
    df.to_json()
    df.to_sql()

    # Other
    df.to_clipboard()
    df.to_dense()
    df.to_feather()
    df.to_gbq()
    df.to_hdf()
    df.to_html()
    df.to_latex()
    df.to_msgpack()
    df.to_numpy()
    df.to_parquet()
    df.to_period()
    df.to_pickle()
    df.to_records()
    df.to_sparse()
    df.to_stata()
    df.to_string()
    df.to_timestamp()
    df.to_xarray()


Usage
=====
.. code-block:: python

    import pandas as pd

    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/iris.csv'

    df = pd.read_csv(url)

    df.head(3)
    #    sepal_length  sepal_width  petal_length  petal_width     species
    # 0           5.4          3.9           1.3          0.4      setosa
    # 1           5.9          3.0           5.1          1.8   virginica
    # 2           6.0          3.4           4.5          1.6  versicolor

.. code-block:: python

    import pandas as pd

    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/iris-dirty.csv'

    df = pd.read_csv(url)
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


Assignments
===========
.. todo:: Create assignments
