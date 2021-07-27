Pandas Read
===========


Rationale
---------
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
