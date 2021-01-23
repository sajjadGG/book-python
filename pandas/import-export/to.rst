DataFrame Export
================


Export data
-------------------------------------------------------------------------------
* File paths works also with DATAs
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


Assignments
-------------------------------------------------------------------------------
.. literalinclude:: assignments/pandas_to_csv.py
    :caption: :download:`Solution <assignments/pandas_to_csv.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_to_json.py
    :caption: :download:`Solution <assignments/pandas_to_json.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_to_pickle.py
    :caption: :download:`Solution <assignments/pandas_to_pickle.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_to_sql.py
    :caption: :download:`Solution <assignments/pandas_to_sql.py>`
    :end-before: # Solution
