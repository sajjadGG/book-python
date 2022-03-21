Boolean Membership
==================


Important
---------
* ``in`` checks whether value is in sequence
* works with ``str``, ``list``, ``tuple``, ``set``, ``dict``
* Computational complexity for checking if sequence "contains":

    * O(n) - ``in str``
    * O(n) - ``in list``
    * O(n) - ``in tuple``
    * O(1) - ``in set``
    * O(1) - ``in dict``

* More information in `Performance Optimization Contains`


Contains
--------
* ``in`` - Contains

Contains with ``str``:

>>> 'x' in 'Python'
False
>>> 'P' in 'Python'
True
>>> 'p' in 'Python'
False

>>> ('x') in 'Python'
False
>>> ('P') in 'Python'
True
>>> ('p') in 'Python'
False

>>> ('x',) in 'Python'
Traceback (most recent call last):
TypeError: 'in <string>' requires string as left operand, not tuple
>>> ('P',) in 'Python'
Traceback (most recent call last):
TypeError: 'in <string>' requires string as left operand, not tuple
>>> ('p',) in 'Python'
Traceback (most recent call last):
TypeError: 'in <string>' requires string as left operand, not tuple

>>> 'Python' in 'Python'
True
>>> 'Py' in 'Python'
True

Contains with ``list``:

>>> 1 in [1, 2]
True
>>> 2 in [1, 2]
True
>>> 3 in [1, 2]
False

>>> [1] in [1, 2]
False
>>> [2] in [1, 2]
False
>>> [3] in [1, 2]
False

>>> [1,] in [1, 2]
False
>>> [2,] in [1, 2]
False
>>> [3,] in [1, 2]
False

>>> [1, 2] in [1, 2]
False
>>> [3, 4] in [1, 2, [3, 4]]
True

Contains with ``tuple``:

>>> 1 in (1, 2)
True
>>> 2 in (1, 2)
True
>>> 3 in (1, 2)
False

>>> (1) in (1, 2)
True
>>> (2) in (1, 2)
True
>>> (3) in (1, 2)
False

>>> (1,) in (1, 2)
False
>>> (2,) in (1, 2)
False
>>> (3,) in (1, 2)
False

>>> (1, 2) in (1, 2)
False
>>> (3, 4) in (1, 2, (3, 4))
True

Contains with ``set``:

>>> 1 in {1, 2}
True
>>> 2 in {1, 2}
True
>>> 3 in {1, 2}
False

>>> {1} in {1, 2}
False
>>> {2} in {1, 2}
False
>>> {3} in {1, 2}
False

>>> {1,} in {1, 2}
False
>>> {2,} in {1, 2}
False
>>> {3,} in {1, 2}
False

>>> {1, 2} in {1, 2}
False
>>> {3, 4} in {1,2, {3, 4}}
Traceback (most recent call last):
TypeError: unhashable type: 'set'

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>> 'commander' in crew
True
>>> 'chemist' in crew
False
>>> 'Melissa Lewis' in crew
False

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>> 'commander' in crew.keys()
True
>>> 'Melissa Lewis' in crew.values()
True


Missing
-------
* ``not in`` - Missing

``str``:

>>> 'P' not in 'Python'
False
>>> 'p' not in 'Python'
True

>>> 'py' not in 'Python'
True
>>> 'Py' not in 'Python'
False

``list``:

>>> 1 not in [1, 2]
False
>>> 3 not in [1, 2]
True

>>> [2] not in [1, 2]
True
>>> [1, 2] not in [1, 2]
True

``tuple``:

>>> 1 not in (1, 2)
False
>>> 3 not in (1, 2)
True

>>> (2) not in (1, 2)
False
>>> (1, 2) not in (1, 2)
True

``set``:

>>> 1 not in {1, 2}
False
>>> 3 not in {1, 2}
True

>>> {2} not in {1, 2}
True
>>> {1, 2} not in {1, 2}
True

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>> 'commander' in crew
True
>>> 'Melissa Lewis' in crew
False
>>>
>>> 'Melissa Lewis' in crew.keys()
False
>>> 'Melissa Lewis' in crew.values()
True


Control Flow
------------
>>> text = 'Monty Python'
>>>
>>> if 'Python' in text:
...     print('Yes')
... else:
...     print('No')
Yes

>>> crew = ['Watney', 'Lewis', 'Martinez']
>>>
>>> if 'Twardowski' in crew:
...     print('Yes')
... else:
...     print('No')
No

>>> crew = {'Watney', 'Lewis', 'Martinez'}
>>>
>>> if 'Twardowski' in crew:
...     print('Yes')
... else:
...     print('No')
No


.. todo:: Assignments
