Comprehension List
==================


Short Syntax
------------
>>> [x+1 for x in range(0,5)]
[1, 2, 3, 4, 5]

>>> [x-1 for x in range(0,5)]
[-1, 0, 1, 2, 3]

>>> [x**2 for x in range(0,5)]
[0, 1, 4, 9, 16]

>>> [2**x for x in range(0,5)]
[1, 2, 4, 8, 16]


Long Syntax
-----------
>>> list(x+1 for x in range(0,5))
[1, 2, 3, 4, 5]

>>> list(x-1 for x in range(0,5))
[-1, 0, 1, 2, 3]

>>> list(x**2 for x in range(0,5))
[0, 1, 4, 9, 16]

>>> list(2**x for x in range(0,5))
[1, 2, 4, 8, 16]


Use Case - Increment
--------------------
>>> [x+1 for x in range(0,5)]
[1, 2, 3, 4, 5]

Use Case - Decrement
--------------------
>>> [x-1 for x in range(0,5)]
[-1, 0, 1, 2, 3]

Use Case - Sum
--------------
>>> sum(x for x in range(0,5))
10


Assignments
-----------
.. literalinclude:: assignments/loop_comprehension_a.py
    :caption: :download:`Solution <assignments/loop_comprehension_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_comprehension_b.py
    :caption: :download:`Solution <assignments/loop_comprehension_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_comprehension_c.py
    :caption: :download:`Solution <assignments/loop_comprehension_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_comprehension_d.py
    :caption: :download:`Solution <assignments/loop_comprehension_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_comprehension_e.py
    :caption: :download:`Solution <assignments/loop_comprehension_e.py>`
    :end-before: # Solution
