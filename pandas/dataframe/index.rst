DataFrame Index
===============


Rationale
---------
* Range Index
* Integer Index
* String Index
* Datetime Index

* Int64Index, UInt64Index and Float64Index have been deprecated in favor of
  the base Index class and will be removed in Pandas 2.0 [#pd14releasenotes]_

Replace:

>>> pd.Int64Index([1, 2, 3])

With:

>>> pd.Index([1, 2, 3], dtype='int64')


Range Index
-----------
>>> import pandas as pd
>>>
>>>
>>> df = pd.DataFrame({
...     'A': [10, 11, 12],
...     'B': [20, 21, 22],
...     'C': [30, 31, 32]})
>>>
>>> df
    A   B   C
0  10  20  30
1  11  21  31
2  12  22  32
>>>
>>> df.index
RangeIndex(start=0, stop=3, step=1)


Integer Index
-------------
* Int64Index, UInt64Index and Float64Index have been deprecated in favor of
  the base Index class and will be removed in Pandas 2.0 [#pd14releasenotes]_

>>> import pandas as pd
>>> import numpy as np
>>>
>>>
>>> df = pd.DataFrame(
...     data = np.arange(16).reshape(4,4),
...     index = [99, 88, 77, 66],
...     columns = ['A', 'B', 'C', 'D'])
>>>
>>> df
     A   B   C   D
99   0   1   2   3
88   4   5   6   7
77   8   9  10  11
66  12  13  14  15
>>>
>>> df.index
Int64Index([99, 88, 77, 66], dtype='int64')


String Index
------------
>>> import pandas as pd
>>> import numpy as np
>>>
>>>
>>> df = pd.DataFrame(
...     data = np.arange(16).reshape(4,4),
...     index = ['a', 'b', 'c', 'd'],
...     columns = ['A', 'B', 'C', 'D'])
>>>
>>> df
    A   B   C   D
a   0   1   2   3
b   4   5   6   7
c   8   9  10  11
d  12  13  14  15
>>>
>>> df.index
Index(['a', 'b', 'c', 'd'], dtype='object')


Datetime Index
--------------
>>> import pandas as pd
>>> import numpy as np
>>> np.random.seed(0)
>>>
>>>
>>> df = pd.DataFrame(
...     columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
...     index = pd.date_range('1999-12-30', periods=7),
...     data = np.random.randn(7, 4))
>>>
>>> df
             Morning      Noon   Evening  Midnight
1999-12-30  1.764052  0.400157  0.978738  2.240893
1999-12-31  1.867558 -0.977278  0.950088 -0.151357
2000-01-01 -0.103219  0.410599  0.144044  1.454274
2000-01-02  0.761038  0.121675  0.443863  0.333674
2000-01-03  1.494079 -0.205158  0.313068 -0.854096
2000-01-04 -2.552990  0.653619  0.864436 -0.742165
2000-01-05  2.269755 -1.454366  0.045759 -0.187184
>>>
>>> df.index
DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-01', '2000-01-02',
               '2000-01-03', '2000-01-04', '2000-01-05'],
              dtype='datetime64[ns]', freq='D')


Set Index
---------
>>> import pandas as pd
>>>
>>>
>>> df = pd.DataFrame([
...     {'id': 1, 'firstname': 'Mark', 'lastname': 'Watney'},
...     {'id': 2, 'firstname': 'Melissa', 'lastname': 'Lewis'},
...     {'id': 3, 'firstname': 'Rick', 'lastname': 'Martinez'},
...     {'id': 4, 'firstname': 'Alex', 'lastname': 'Vogel'},
... ])
>>>
>>> df
   id  firstname    lastname
0   1       Mark      Watney
1   2    Melissa       Lewis
2   3       Rick    Martinez
3   4       Alex       Vogel
>>>
>>> df.set_index('id')
    firstname    lastname
id
1       Mark      Watney
2    Melissa       Lewis
3       Rick    Martinez
4       Alex       Vogel


References
----------
.. [#pd14releasenotes] https://pandas.pydata.org/pandas-docs/dev/whatsnew/v1.4.0.html#deprecated-int64index-uint64index-float64index


Assignments
-----------
.. todo:: Create assignments
