**********************
DataFrame Aggregations
**********************


* ``df.groupby('month', as_index=False).agg({"duration": "sum"})``

Example
=======
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


Case Study
==========
* :cite:`PandasAggregations`

Data
----
* :download:`data/phones.csv`

.. csv-table:: Data
    :header: Column, Description
    :widths: 10, 90

    "date", "The date and time of the entry"
    "duration", "The duration (in seconds) for each call, the amount of data (in MB) for each data entry, and the number of texts sent (usually 1) for each sms entry."
    "item", "A description of the event occurring – can be one of call, sms, or data."
    "month", "The billing month that each entry belongs to – of form ‘YYYY-MM’."
    "network", "The mobile network that was called/texted for each entry.
    "network_type", "Whether the number being called was a mobile, international (‘world’), voicemail, landline, or other (‘special’) number."

Read DataFrame
--------------
.. code-block:: python

    import pandas as pd

    data = pd.DataFrame.from_csv('phones.csv')

Clean Dates
-----------
.. code-block:: python
    :caption: Convert date from string to date times

    import dateutil

    data['date'] = data['date'].apply(dateutil.parser.parse, dayfirst=True)

Summarising the DataFrame
-------------------------
.. code-block:: python
    :caption: How many rows the dataset

    data['item'].count()
    # 830

.. code-block:: python
    :caption: What was the longest phone call / data entry?

    data['duration'].max()
    # 10528.0

.. code-block:: python
    :caption: How many seconds of phone calls are recorded in total?

    data['duration'][data['item'] == 'call'].sum()
    # 92321.0

.. code-block:: python
    :caption: How many entries are there for each month?

    data['month'].value_counts()
    # 2014-11    230
    # 2015-01    205
    # 2014-12    157
    # 2015-02    137
    # 2015-03    101
    # dtype: int64

.. code-block:: python
    :caption: Number of non-null unique network entries

    data['network'].nunique()
    # 9

Summarising Groups
------------------
.. code-block:: python

    data.groupby(['month']).groups.keys()
    # ['2014-12', '2014-11', '2015-02', '2015-03', '2015-01']

    len(data.groupby(['month']).groups['2014-11'])
    # 230

.. code-block:: python
    :caption: Get the first entry for each month

    data.groupby('month').first()
    #                        date  duration  item   network network_type
    # month
    # 2014-11 2014-10-15 06:58:00    34.429  data      data         data
    # 2014-12 2014-11-13 06:58:00    34.429  data      data         data
    # 2015-01 2014-12-13 06:58:00    34.429  data      data         data
    # 2015-02 2015-01-13 06:58:00    34.429  data      data         data
    # 2015-03 2015-02-12 20:15:00    69.000  call  landline     landline

.. code-block:: python
    :caption: Get the sum of the durations per month

    data.groupby('month')['duration'].sum()
    # month
    # 2014-11    26639.441
    # 2014-12    14641.870
    # 2015-01    18223.299
    # 2015-02    15522.299
    # 2015-03    22750.441
    # Name: duration, dtype: float64

.. code-block:: python
    :caption: Get the number of dates / entries in each month

    data.groupby('month')['date'].count()
    # month
    # 2014-11    230
    # 2014-12    157
    # 2015-01    205
    # 2015-02    137
    # 2015-03    101
    # Name: date, dtype: int64

.. code-block:: python
    :caption: What is the sum of durations, for calls only, to each network

    data[data['item'] == 'call'].groupby('network')['duration'].sum()
    # network
    # Meteor 7200
    # Tesco 13828
    # Three 36464
    # Vodafone 14621
    # landline 18433
    # voicemail 1775
    # Name: duration, dtype: float64

.. code-block:: python
    :caption: How many calls, sms, and data entries are in each month?

    data.groupby(['month', 'item'])['date'].count()
    # month    item
    # 2014-11  call    107
    #          data     29
    #          sms      94
    # 2014-12  call     79
    #          data     30
    #          sms      48
    # 2015-01  call     88
    #          data     31
    #          sms      86
    # 2015-02  call     67
    #          data     31
    #          sms      39
    # 2015-03  call     47
    #          data     29
    #          sms      25
    # Name: date, dtype: int64

.. code-block:: python
    :caption: How many calls, texts, and data are sent per month, split by network_type?

    data.groupby(['month', 'network_type'])['date'].count()
    # month network_type
    # 2014-11 data 29
    #  landline 5
    #  mobile 189
    #  special 1
    #  voicemail 6
    # 2014-12 data 30
    #  landline 7
    #  mobile 108
    #  voicemail 8
    #  world 4
    # 2015-01 data 31
    #  landline 11
    #  mobile 160
    # ....

Groupby output format
---------------------
* Series or DataFrame?

.. code-block:: python
    :caption: produces Pandas Series

    data.groupby('month')['duration'].sum()

.. code-block:: python
    :caption: Produces Pandas DataFrame

    data.groupby('month')[['duration']].sum()

.. code-block:: python
    :caption: The groupby output will have an index or multi-index on rows corresponding to your chosen grouping variables. To avoid setting this index, pass ``as_index=False`` to the groupby operation.

    data.groupby('month', as_index=False).agg({"duration": "sum"})

Multiple Statistics per Group
-----------------------------
.. code-block:: python
    :caption: Group the data frame by month and item and extract a number of stats from each group

    data.groupby(
       ['month', 'item']
    ).agg(
        {
             'duration':sum,    # Sum duration per group
             'network_type': "count",  # get the count of networks
             'date': 'first'  # get the first date per group
        }
    )

.. code-block:: python
    :caption: Define the aggregation procedure outside of the groupby operation

    aggregations = {
        'duration':'sum',
        'date': lambda x: max(x) - 1
    }
    data.groupby('month').agg(aggregations)

Applying multiple functions to columns in groups
------------------------------------------------
.. code-block:: python
    :caption: Group the data frame by month and item and extract a number of stats from each group

    data.groupby(
        ['month', 'item']
    ).agg(
        {
            # Find the min, max, and sum of the duration column
            'duration': [min, max, sum],
            # find the number of network type entries
            'network_type': "count",
            # minimum, first, and number of unique dates
            'date': [min, 'first', 'nunique']
        }
    )

Named Aggregations
------------------
.. code-block:: python
    :caption: Named Aggregations

    data[data['item'] == 'call'].groupby('month').agg(

        # Get max of the duration column for each group
        max_duration=('duration', max),

        # Get min of the duration column for each group
        min_duration=('duration', min),

        # Get sum of the duration column for each group
        total_duration=('duration', sum),

        # Apply a lambda to date column
        num_days=("date", lambda x: (max(x) - min(x)).days)
    )

.. code-block:: python
    :caption: Pandas also provides the NamedAggregation named-tuple, which can be used to achieve the same as normal tuples

    data[data['item'] == 'call'].groupby('month').agg(
        max_duration=pd.NamedAgg(column='duration', aggfunc=max),
        min_duration=pd.NamedAgg(column='duration', aggfunc=min),
        total_duration=pd.NamedAgg(column='duration', aggfunc=sum),
        num_days=pd.NamedAgg(
            column="date",
            aggfunc=lambda x: (max(x) - min(x)).days)
    )

Renaming index
--------------
* using droplevel and ravel
* Dictionary groupby format is deprecated

.. code-block:: python
    :caption: Drop the top level (using ``.droplevel()``) of the newly created multi-index on columns using

    grouped = data.groupby('month').agg("duration": [min, max, mean])
    grouped.columns = grouped.columns.droplevel(level=0)
    grouped.rename(columns={
        "min": "min_duration", "max": "max_duration", "mean": "mean_duration"
    })
    grouped.head()

.. code-block:: python
    :caption: Quick renaming of grouped columns from the groupby() multi-index can be achieved using the ravel() function.

    grouped = data.groupby('month').agg("duration": [min, max, mean])
    # Using ravel, and a string join, we can create better names for the columns:
    grouped.columns = ["_".join(x) for x in grouped.columns.ravel()]


Assignments
===========
.. todo:: Create assignments
