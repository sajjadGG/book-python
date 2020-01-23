*********************
DataFrame Export Data
*********************


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


Assignments
===========
.. todo:: Create Assignments
