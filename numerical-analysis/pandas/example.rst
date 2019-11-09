*******
Example
*******

.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    df = pd.read_excel(
        io='filename.xls',
        encoding='utf-8',
        parse_dates=['from', 'to'],  # list of columns to parse for dates
        sheet_name=['Sheet 1'],
        skip_blank_lines=True,
        skiprows=1,
    )

    # Rename Columns to match database columns
    df.rename(columns={
        'from': 'date_start',
        'to': 'date_end',
    }, inplace=True)

    # Drop all records where "Name" is empty (NaN)
    df.dropna(subset=['name'], how='all', inplace=True)

    # Add column ``blacklist`` with data
    df['blacklist'] = [True, False, True, False]

    # Change NaN to None
    df.fillna(None, inplace=True)

    # Choose columns
    columns = ['name', 'date_start', 'date_end', 'blacklist']

    return df[columns].to_dict('records')


Assignments
===========
.. todo:: Create assignments
