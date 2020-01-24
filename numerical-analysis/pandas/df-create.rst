****************
DataFrame Create
****************


Indexes
=======

Range Index
-----------
.. code-block:: python

    import pandas as pd

    pd.DataFrame({
        'A': [10, 11, 12],
        'B': [20, 21, 22],
        'C': [30, 31, 32]})
    #     A   B   C
    # 0  10  20  30
    # 1  11  21  31
    # 2  12  22  32

Integer Index
-------------
.. code-block:: python

    import pandas as pd
    import numpy as np

    data = np.arange(16).reshape(4,4)
    index = [99, 88, 77, 66]
    columns = ['A', 'B', 'C', 'D']

    pd.DataFrame(data, index, columns)
    #      A   B   C   D
    # 99   0   1   2   3
    # 88   4   5   6   7
    # 77   8   9  10  11
    # 66  12  13  14  15

String Index
------------
.. code-block:: python

    import pandas as pd
    import numpy as np

    data = np.arange(16).reshape(4,4)
    index = ['a', 'b', 'c', 'd']
    columns = ['A', 'B', 'C', 'D']

    pd.DataFrame(data, index, columns)
    #     A   B   C   D
    # a   0   1   2   3
    # b   4   5   6   7
    # c   8   9  10  11
    # d  12  13  14  15

Date indexes
------------
.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    index = pd.date_range('1999-12-30', periods=7)
    data = np.random.randn(7, 4)

    pd.DataFrame(data, index, columns)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Values
======

Custom values in columns
------------------------
.. code-block:: python

    import pandas as pd
    import numpy as np

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

    pd.DataFrame([
        {'A': 1.0, 'B': 2.0},
        {'B': 3.0, 'C': 4.0},
    ])
    #      A    B    C
    # 0  1.0  2.0  NaN
    # 1  NaN  3.0  4.0


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

        .. code-block:: text

            "Crew", "Role", "Astronaut"
            "Prime", "CDR", "Neil Armstrong"
            "Prime", "LMP", "Buzz Aldrin"
            "Prime", "CMP", "Michael Collins"
            "Backup", "CDR", "James Lovell"
            "Backup", "LMP", "William Anders"
            "Backup", "CMP", "Fred Haise"

