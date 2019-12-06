***************
DataFrame Alter
***************


Add Column
==========
.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df['Z'] = np.arange(7.0)
    #      A    B    C   D    Z
    # 0  1.0  1.1    a NaN  0.0
    # 1  2.0  2.2    b NaN  1.0
    # 2  NaN  NaN  NaN NaN  2.0
    # 3  NaN  NaN  NaN NaN  3.0
    # 4  3.0  3.3    c NaN  4.0
    # 5  NaN  NaN  NaN NaN  5.0
    # 6  4.0  4.4    d NaN  6.0

    df['X'] = ['a', 'b', 'c']
    # ValueError: Length of values does not match length of index

    df['X'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    #      A    B    C   D    Z  X
    # 0  1.0  1.1    a NaN  0.0  a
    # 1  2.0  2.2    b NaN  1.0  b
    # 2  NaN  NaN  NaN NaN  2.0  c
    # 3  NaN  NaN  NaN NaN  3.0  d
    # 4  3.0  3.3    c NaN  4.0  e
    # 5  NaN  NaN  NaN NaN  5.0  f
    # 6  4.0  4.4    d NaN  6.0  g


Add Row
=======
.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df.append({'A':1, 'B':2, 'C':3, 'D':4})
    # TypeError: Can only append a Series if ignore_index=True or if the Series has a name

    df.append({'A':1, 'B':2, 'C':3, 'D':4}, ignore_index=True)
    #      A    B    C    D
    # 0  1.0  1.1    a  NaN
    # 1  2.0  2.2    b  NaN
    # 2  NaN  NaN  NaN  NaN
    # 3  NaN  NaN  NaN  NaN
    # 4  3.0  3.3    c  NaN
    # 5  NaN  NaN  NaN  NaN
    # 6  4.0  4.4    d  NaN
    # 7  1.0  2.0    3  4.0


Drop Columns
============
.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df.drop(columns=['A', 'B'])
    #      C    D
    # 0    a  NaN
    # 1    0  0.0
    # 2    0  0.0
    # 3    0  0.0
    # 4    c  NaN
    # 5  NaN  NaN
    # 6    d  NaN


Drop Row
========
.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df.drop(1)
    #      A    B    C    D
    # 0  1.0  1.1    a  NaN
    # 2  0.0  0.0    0  0.0
    # 3  0.0  0.0    0  0.0
    # 4  3.0  3.3    c  NaN
    # 5  NaN  NaN  NaN  NaN
    # 6  4.0  4.4    d  NaN

    df.drop([1,2,3])
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN


Assignments
===========
.. todo:: Create assignments
