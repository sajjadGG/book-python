****************
DataFrame Create
****************


Create DataFrame
================
.. code-block:: python

    import pandas as pd


    df = pd.DataFrame({'A': ['a', 'b', 'c', 'd'],
                       'B': [0, 1, 2, 3],
                       'C': [0., 1., 2., 3.]})
    #    A  B    C
    # 0  a  0  0.0
    # 1  b  1  1.0
    # 2  c  2  2.0
    # 3  d  3  3.0


Indexes
=======

Integer index
-------------
.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    data = np.arange(16).reshape(4, 4)
    index = range(0, 4)
    columns = range(0, 4)

    df = pd.DataFrame(data, index, columns)
    #     0   1   2   3
    # 0   0   1   2   3
    # 1   4   5   6   7
    # 2   8   9  10  11
    # 3  12  13  14  15

Date indexes
------------
.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    data = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    index = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(data, index, columns)
    #                 Morning        Noon    Evening   Midnight
    # 1970-01-01     2.269755   -1.454366   0.045759  -0.187184
    # 1970-01-02     1.532779    1.469359   0.154947   0.378163
    # 1970-01-03    -0.887786   -1.980796  -0.347912   0.156349
    # 1970-01-04     1.230291    1.202380  -0.387327  -0.302303
    # 1970-01-05    -1.048553   -1.420018  -1.706270   1.950775
    # 1970-01-06    -0.509652   -0.438074  -1.252795   0.777490


Values
======

Custom values in columns
------------------------
.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)

    pd.DataFrame({'A' : 1.,
                  'B' : pd.Timestamp('1961-04-12'),
                  'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                  'D' : np.array([3] * 4, dtype='int32'),
                  'E' : pd.Categorical(["test", "train", "test", "train"]),
                  'F' : 'foo' })
    #      A           B    C  D      E    F
    # 0  1.0  1961-04-12  1.0  3   test  foo
    # 1  1.0  1961-04-12  1.0  3  train  foo
    # 2  1.0  1961-04-12  1.0  3   test  foo
    # 3  1.0  1961-04-12  1.0  3  train  foo

With multiple rows
------------------
.. code-block:: python

    import pandas as pd

    pd.DataFrame([{'A': 1, 'B': 2}, {'C': 3}])
    #      A    B    C
    # 0  1.0  2.0  NaN
    # 1  NaN  NaN  3.0


Assignments
===========
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/df_create.py`

:English:
    #. Create ``DataFrame`` for input data

:Polish:
    #. Stwórz ``DataFrame`` dla danych wejściowych

:Input:
    .. csv-table::
        :header: "Crew", "Role", "Astronaut"

        "Prime", "CDR", "Neil Armstrong"
        "Prime", "LMP", "Buzz Aldrin"
        "Prime", "CMP", "Michael Collins"
        "Backup", "CDR", "James Lovell"
        "Backup", "LMP", "William Anders"
        "Backup", "CMP", "Fred Haise"

:Hint:
    * Use selection with ``alt`` key in your IDE
    * If it's not working use CSV:

        .. code-block:: csv

            "Crew", "Role", "Astronaut"
            "Prime", "CDR", "Neil Armstrong"
            "Prime", "LMP", "Buzz Aldrin"
            "Prime", "CMP", "Michael Collins"
            "Backup", "CDR", "James Lovell"
            "Backup", "LMP", "William Anders"
            "Backup", "CMP", "Fred Haise"

