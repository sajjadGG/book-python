******************
DataFrame Group By
******************


.. code-block:: python

    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/phones.csv'

    df = pd.read_csv(DATA, parse_dates=['date'])
    df.drop(columns='index', inplace=True)

.. csv-table:: Data
    :header: Column, Description
    :widths: 10, 90

    "date", "The date and time of the entry"
    "duration", "The duration (in seconds) for each call, the amount of data (in MB) for each data entry, and the number of texts sent (usually 1) for each sms entry"
    "item", "A description of the event occurring – can be one of call, sms, or data"
    "month", "The billing month that each entry belongs to – of form ``YYYY-MM``"
    "network", "The mobile network that was called/texted for each entry"
    "network_type", "Whether the number being called was a mobile, international ('world'), voicemail, landline, or other ('special') number."


Grouping
========
.. code-block:: python

    df.groupby('item')
    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x12975df90>

.. code-block:: python

    df.groupby(['month', 'item'])
    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x12973aa10>


Groupby Methods
===============
* Group series using mapper (dict or key function, apply given function to group, return result as series) or by a series of columns
* ``.size()``
* ``.mean()``
* ``.nunique()``
* ``.sum()``
* ``.count()``
* ``.max()``
* ``.first()``

Size
----
.. code-block:: python

    df.groupby('item').size()
    # item
    # call    388
    # data    150
    # sms     292
    # dtype: int64

Mean
----
.. code-block:: python

    df.groupby('item').mean()
    #         duration
    # item
    # call  237.940722
    # data   34.429000
    # sms     1.000000

Number of Uniques
-----------------
.. code-block:: python

    df.groupby('item').nunique()
    #       date  duration  item  month  network  network_type
    # item
    # call   378       220     1      5        6             3
    # data   150         1     1      5        1             1
    # sms    222         1     1      5        6             3

Sum
---
.. code-block:: python

    df.groupby('item').sum()
    #       duration
    # item
    # call  92321.00
    # data   5164.35
    # sms     292.00

Count
-----
.. code-block:: python

    df.groupby('item').count()
    #       date  duration  month  network  network_type
    # item
    # call   388       388    388      388           388
    # data   150       150    150      150           150
    # sms    292       292    292      292           292

Maximum
-------
.. code-block:: python

    df.groupby('item').max()
    #                     date   duration    month    network network_type
    # item
    # call 2015-12-02 20:51:00  10528.000  2015-03  voicemail    voicemail
    # data 2015-12-03 06:58:00     34.429  2015-03       data         data
    # sms  2015-12-01 18:26:00      1.000  2015-03      world        world

First
-----
.. code-block:: python

    df.groupby('item').first()
    #                     date  duration    month   network network_type
    # item
    # call 2014-10-15 06:58:00    13.000  2014-11  Vodafone       mobile
    # data 2014-10-15 06:58:00    34.429  2014-11      data         data
    # sms  2014-10-16 22:18:00     1.000  2014-11    Meteor       mobile



Assignments
===========

Astronauts
----------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/df_groupby_astronauts.py`

:English:
    #. Download astronauts dataset :download:`data/astronauts.csv`
    #. Create ranking of the most experienced astronauts (number of flights)

:Polish:
    #. Pobierz zbiór danych astronautów :download:`data/astronauts.csv`
    #. Stwórz ranking najbardziej doświadczonych astronautów (liczba lotów)

EVA
---
* Complexity level: hard
* Lines of code to write: 30 lines
* Estimated time of completion: 40 min
* Filename: :download:`solution/df_groupby_eva.py`

:English:
    #. Download spacewalk (EVA) dataset :download:`data/eva.csv`
    #. Create ranking of astronauts with the most time spent on EVA

:Polish:
    #. Pobierz zbiór danych spacerów kosmicznych (EVA) :download:`data/eva.csv`
    #. Stwórz ranking astronautów z największym czasem EVA

:Hint:
    * Parse CSV and replace newlines inside fields with ``","``
    * Split names into separate columns for each spacewalker (first, second, third)
    * Split names into separate rows for each spacewalker (use ffill)
    * Split times into separate columns (hours, minutes)
