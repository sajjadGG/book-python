****************
DataFrame Create
****************


Create from List of Dicts
=========================
.. code-block:: python

    import pandas as pd

    pd.DataFrame([
        {'A': 1.0, 'B': 2.0},
        {'A': 3.0, 'B': 4.0},
    ])

    #      A    B
    # 0  1.0  2.0
    # 1  3.0  4.0

.. code-block:: python

    import pandas as pd

    pd.DataFrame([
        {'A': 1.0, 'B': 2.0},
        {'B': 3.0, 'C': 4.0},
    ])

    #      A    B    C
    # 0  1.0  2.0  NaN
    # 1  NaN  3.0  4.0

.. code-block:: python

    import pandas as pd

    pd.DataFrame([
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Jan', 'last_name': 'Twardowski'},
        {'first_name': 'Ivan', 'last_name': 'Ivanovic'},
        {'first_name': 'Melissa', 'last_name': 'Lewis'},
    ])

    #   first_name   last_name
    # 0       Mark      Watney
    # 1        Jan  Twardowski
    # 2       Ivan    Ivanovic
    # 3    Melissa       Lewis

Create from Dict
================
.. code-block:: python

    import pandas as pd

    pd.DataFrame({
        'A': ['a', 'b', 'c'],
        'B': [1.0, 2.0, 3.0],
        'C': [1, 2, 3],
    })

    #    A    B  C
    # 0  a  1.0  1
    # 1  b  2.0  2
    # 2  c  3.0  3

.. code-block:: python

    import pandas as pd

    pd.DataFrame({
        'first_name': ['Mark', 'Jan', 'Ivan', 'Melissa'],
        'last_name': ['Watney', 'Twardowski', 'Ivanovic', 'Lewis'],
    })

    #   first_name   last_name
    # 0       Mark      Watney
    # 1        Jan  Twardowski
    # 2       Ivan    Ivanovic
    # 3    Melissa       Lewis

.. code-block:: python

    import pandas as pd
    import numpy as np

    pd.DataFrame({
        'A': 1.,
        'B': pd.Timestamp('1961-04-12'),
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(["test", "train", "test", "train"]),
        'F': 'foo',
    })

    #      A           B    C  D      E    F
    # 0  1.0  1961-04-12  1.0  3   test  foo
    # 1  1.0  1961-04-12  1.0  3  train  foo
    # 2  1.0  1961-04-12  1.0  3   test  foo
    # 3  1.0  1961-04-12  1.0  3  train  foo


Assignments
===========

DataFrame Create
----------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/df_create.py`

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

