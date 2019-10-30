*****************
Import and Export
*****************


Import data
===========
* File paths works also with URLs
* SQL functions uses SQLAlchemy, which supports many RDBMS

.. code-block:: python

    pd.read_csv()
    pd.read_excel()
    pd.read_html()
    pd.read_json()
    pd.read_sas()
    pd.read_sql()        # Read SQL query or database table into a DataFrame
    pd.read_sql_query()  # Read SQL query into a DataFrame
    pd.read_sql_table()  # Read SQL database table into a DataFrame


Export data
===========
* File paths works also with URLs
* SQL functions uses SQLAlchemy, which supports many RDBMS

.. code-block:: python

    DataFrame.to_csv()
    DataFrame.to_excel()
    DataFrame.to_html()
    DataFrame.to_json()
    DataFrame.to_latex()
    DataFrame.to_dict()
    DataFrame.to_sql()


Assignments
===========
.. todo:: Create assignments
