******************
DataFrame Group By
******************

* Group series using mapper (dict or key function, apply given function to group, return result as series) or by a series of columns
* Check:

    - ``.value_counts()``
    - ``.nunique()``
    - ``.sum()``
    - ``.count()``
    - ``.max()``
    - ``.first()``

.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    data = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    index = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(data, index, columns)

By count of elements
--------------------
.. code-block:: python

    df.groupby('D').size()
    #         D
    # -1.789321    1
    # -0.709686    1
    # -0.424071    1
    # -0.241387    1
    #  1.283282    1
    #  1.323504    1
    # dtype: int64

By mean of elements
-------------------
.. code-block:: python

    df.groupby('D').mean()
    #         D          A          B          C
    # -1.789321   0.257330   1.190259   0.074459
    # -0.709686  -0.459565   0.827296   0.953118
    # -0.424071   1.062487  -0.251961  -0.424092
    # -0.241387  -0.928127  -0.931601   1.036800
    # 1.283282   -0.015208   0.901456  -0.812575
    # 1.323504   -0.389369  -0.283878  -0.166324

Example
-------
.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                       'C' : np.random.randn(8),
                       'D' : np.random.randn(8)})

    #      A      B          C          D
    # 0  foo    one   0.239653  -1.505271
    # 1  bar    one   0.567327  -0.109503
    # 2  foo    two   1.726200  -0.401514
    # 3  bar  three  -1.145225   1.379611
    # 4  foo    two  -0.808037   1.148953
    # 5  bar    two   0.883013  -0.347327
    # 6  foo    one   0.225142  -0.995694
    # 7  foo  three  -0.484968  -0.547152

    df.groupby('A').mean()
    #   A         C          D
    # bar  0.101705   0.307594
    # foo  0.179598  -0.460136


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
