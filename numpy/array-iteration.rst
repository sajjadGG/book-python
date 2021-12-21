Array Iteration
===============


1-dimensional Array
-------------------
>>> import numpy as np
>>>
>>>
>>> data = np.array([1, 2, 3])
>>>
>>> for value in data:
...     print(f'{value=}')
value=1
value=2
value=3


2-dimensional Array
-------------------
>>> import numpy as np
>>>
>>>
>>> data = np.array([[1, 2, 3],
...                  [4, 5, 6],
...                  [7, 8, 9]])
>>>
>>> for value in data:
...     print(f'{value=}')
value=[1 2 3]
value=[4 5 6]
value=[7 8 9]

>>> import numpy as np
>>>
>>>
>>> data = np.array([[1, 2, 3],
...                  [4, 5, 6],
...                  [7, 8, 9]])
>>>
>>> for row in data:
...     for value in row:
...     print(f'{value=}')
value=1
value=2
value=3
value=4
value=5
value=6
value=7
value=8
value=9


Flat
----
Flatten:

>>> import numpy as np
>>>
>>>
>>> data = np.array([[1, 2, 3],
...                  [4, 5, 6],
...                  [7, 8, 9]])
>>>
>>> for value in data.flatten():
...     print(f'{value=}')
value=1
value=2
value=3
value=4
value=5
value=6
value=7
value=8
value=9

Ravel:

>>> import numpy as np
>>>
>>>
>>> data = np.array([[1, 2, 3],
...                  [4, 5, 6],
...                  [7, 8, 9]])
>>>
>>> for value in data.ravel():
...     print(f'{value=}')
value=1
value=2
value=3
value=4
value=5
value=6
value=7
value=8
value=9


Enumerate
---------
>>> import numpy as np
>>>
>>>
>>> data = np.array([[1, 2, 3],
...                  [4, 5, 6],
...                  [7, 8, 9]])
>>>
>>> for i, value in enumerate(data):
...     print(f'{i=}, {value=}')
i=0, value=[1 2 3]
i=1, value=[4 5 6]
i=2, value=[7 8 9]

>>> import numpy as np
>>>
>>>
>>> data = np.array([[1, 2, 3],
...                  [4, 5, 6],
...                  [7, 8, 9]])
>>>
>>> for i, value in enumerate(data.ravel()):
...     print(f'{i=}, {value=}')
i=0, value=1
i=1, value=2
i=2, value=3
i=3, value=4
i=4, value=5
i=5, value=6
i=6, value=7
i=7, value=8
i=8, value=9

>>> import numpy as np
>>>
>>>
>>> data = np.array([[1, 2, 3],
...                  [4, 5, 6],
...                  [7, 8, 9]])
>>>
>>> for i, row in enumerate(data):
...     for j, value in enumerate(row):
...         print(f'{i=}, {j=}, {value=}')
i=0, j=0, value=1
i=0, j=1, value=2
i=0, j=2, value=3
i=1, j=0, value=4
i=1, j=1, value=5
i=1, j=2, value=6
i=2, j=0, value=7
i=2, j=1, value=8
i=2, j=2, value=9


Assignments
-----------
.. literalinclude:: assignments/numpy_iteration.py
    :caption: :download:`Solution <assignments/numpy_iteration.py>`
    :end-before: # Solution
