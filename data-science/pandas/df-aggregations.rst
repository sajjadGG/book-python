**********************
DataFrame Aggregations
**********************


* ``df.groupby('month', as_index=False).agg({"duration": "sum"})``

.. code-block:: python

    aggregations = {
        'duration':'sum',
        'date': lambda x: max(x) - 1
    }
    data.groupby('month').agg(aggregations)

.. code-block:: python

    aggregations = {
        'duration': [min, max, sum],        # find the min, max, and sum of the duration column
        'network_type': 'count',            # find the number of network type entries
        'date': [min, 'first', 'nunique']   # get the min, first, and number of unique dates per group
    }

    data.groupby(['month', 'item']).agg(aggregations)

.. todo:: https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
