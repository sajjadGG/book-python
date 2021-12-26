DataFrame Create
================


Rationale
---------


SetUp
-----
>>> import pandas as pd
>>> import numpy as np


Create from List of Dicts
-------------------------
>>> pd.DataFrame([
...     {'A': 1.0, 'B': 2.0},
...     {'A': 3.0, 'B': 4.0},
... ])
     A    B
0  1.0  2.0
1  3.0  4.0

>>> pd.DataFrame([
...     {'A': 1.0, 'B': 2.0},
...     {'B': 3.0, 'C': 4.0},
... ])
     A    B    C
0  1.0  2.0  NaN
1  NaN  3.0  4.0

>>> pd.DataFrame([
...     {'firstname': 'Mark', 'lastname': 'Watney'},
...     {'firstname': 'Jan', 'lastname': 'Twardowski'},
...     {'firstname': 'Ivan', 'lastname': 'Ivanovic'},
...     {'firstname': 'Melissa', 'lastname': 'Lewis'},
... ])
   firstname    lastname
0       Mark      Watney
1        Jan  Twardowski
2       Ivan    Ivanovic
3    Melissa       Lewis


Create from Dict
----------------
>>> pd.DataFrame({
...     'A': ['a', 'b', 'c'],
...     'B': [1.0, 2.0, 3.0],
...     'C': [1, 2, 3],
... })
   A    B  C
0  a  1.0  1
1  b  2.0  2
2  c  3.0  3

>>> pd.DataFrame({
...     'firstname': ['Mark', 'Jan', 'Ivan', 'Melissa'],
...     'lastname': ['Watney', 'Twardowski', 'Ivanovic', 'Lewis'],
... })
   firstname    lastname
0       Mark      Watney
1        Jan  Twardowski
2       Ivan    Ivanovic
3    Melissa       Lewis


Create from NDArray
-------------------
>>> import pandas as pd
>>> import numpy as np
>>> np.random.seed(0)
>>>
>>>
>>> df = pd.DataFrame(np.random.randn(7, 4))
>>>
>>> df
          0         1         2         3
0  1.764052  0.400157  0.978738  2.240893
1  1.867558 -0.977278  0.950088 -0.151357
2 -0.103219  0.410599  0.144044  1.454274
3  0.761038  0.121675  0.443863  0.333674
4  1.494079 -0.205158  0.313068 -0.854096
5 -2.552990  0.653619  0.864436 -0.742165
6  2.269755 -1.454366  0.045759 -0.187184


Use Case - 0x01
---------------
>>> import pandas as pd
>>> import numpy as np
>>>
>>>
>>> pd.DataFrame({
...     'A': 1.,
...     'B': pd.Timestamp('1961-04-12'),
...     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
...     'D': np.array([3] * 4, dtype='int32'),
...     'E': pd.Categorical(["test", "train", "test", "train"]),
...     'F': 'foo',
...     'G': [1,2,3,4],
... })
     A           B    C  D      E    F  G
0  1.0  1961-04-12  1.0  3   test  foo  1
1  1.0  1961-04-12  1.0  3  train  foo  2
2  1.0  1961-04-12  1.0  3   test  foo  3
3  1.0  1961-04-12  1.0  3  train  foo  4


Use Case - 0x02
---------------
>>> import pandas as pd
>>> import numpy as np
>>> np.random.seed(0)
>>>
>>>
>>> df = pd.DataFrame(
...     columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
...     index = pd.date_range('1999-12-30', periods=7),
...     data = np.random.randn(7, 4))
...
>>> df
             Morning      Noon   Evening  Midnight
1999-12-30  1.764052  0.400157  0.978738  2.240893
1999-12-31  1.867558 -0.977278  0.950088 -0.151357
2000-01-01 -0.103219  0.410599  0.144044  1.454274
2000-01-02  0.761038  0.121675  0.443863  0.333674
2000-01-03  1.494079 -0.205158  0.313068 -0.854096
2000-01-04 -2.552990  0.653619  0.864436 -0.742165
2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Assignments
-----------
.. literalinclude:: assignments/pandas_df_create_a.py
    :caption: :download:`Solution <assignments/pandas_df_create_a.py>`
    :end-before: # Solution
