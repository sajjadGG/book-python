Comprehension List
==================


Short Syntax
------------
>>> [x+1 for x in range(0,5)]
[1, 2, 3, 4, 5]

>>> [x-1 for x in range(0,5)]
[-1, 0, 1, 2, 3]


Long Syntax
-----------
>>> list(x+1 for x in range(0,5))
[1, 2, 3, 4, 5]

>>> list(x-1 for x in range(0,5))
[-1, 0, 1, 2, 3]


Use Case - Increment
--------------------
>>> [x+1 for x in range(0,5)]
[1, 2, 3, 4, 5]


Use Case - Decrement
--------------------
>>> [x-1 for x in range(0,5)]
[-1, 0, 1, 2, 3]


Use Case - Power
----------------
>>> [x**2 for x in range(0,5)]
[0, 1, 4, 9, 16]
>>>
>>> [2**x for x in range(0,5)]
[1, 2, 4, 8, 16]

>>> list(x**2 for x in range(0,5))
[0, 1, 4, 9, 16]
>>>
>>> list(2**x for x in range(0,5))
[1, 2, 4, 8, 16]


Use Case - Sum
--------------
>>> sum(x for x in range(0,5))
10


Use Case - Join String
----------------------
>>> DATA = ['hello', 'world']
>>>
>>>
>>> ','.join(DATA)
'hello,world'
>>>
>>> '\n'.join(DATA)
'hello\nworld'

>>> DATA = ['hello', 'world']
>>>
>>>
>>> str.join(',', DATA)
'hello,world'


Use Case - Species
------------------
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>>
>>> [row[-1] for row in DATA[1:]]  # doctest: +NORMALIZE_WHITESPACE
['virginica',
 'setosa',
 'versicolor',
 'virginica',
 'versicolor',
 'setosa',
 'versicolor']

Assignments
-----------
.. literalinclude:: assignments/comprehension_list_a.py
    :caption: :download:`Solution <assignments/comprehension_list_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/comprehension_list_b.py
    :caption: :download:`Solution <assignments/comprehension_list_b.py>`
    :end-before: # Solution
