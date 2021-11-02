Comprehension Dict
==================


Syntax
------
``dict`` comprehension approach to applying function to elements:

>>> {x+10:x for x in range(0,5)}
{10: 0, 11: 1, 12: 2, 13: 3, 14: 4}

>>> dict((x+10,x) for x in range(0,5))
{10: 0, 11: 1, 12: 2, 13: 3, 14: 4}

``dict`` comprehension approach to applying function to elements:

>>> {x:x+10 for x in range(0,5)}
{0: 10, 1: 11, 2: 12, 3: 13, 4: 14}

>>> dict((x,x+10) for x in range(0,5))
{0: 10, 1: 11, 2: 12, 3: 13, 4: 14}

``dict`` Comprehension approach to applying function to elements:

>>> {x+10:x+10 for x in range(0,5)}
{10: 10, 11: 11, 12: 12, 13: 13, 14: 14}

>>> dict((x+10,x+10) for x in range(0,5))
{10: 10, 11: 11, 12: 12, 13: 13, 14: 14}


Reverse Dict
------------
Reversing ``dict`` keys with values:

>>> DATA = {'a': 1, 'b': 2}
>>>
>>>
>>> list(DATA.items())  # doctest: +NORMALIZE_WHITESPACE
[('a', 1),
 ('b', 2)]
>>>
>>> [(k,v) for k,v in DATA.items()]  # doctest: +NORMALIZE_WHITESPACE
[('a', 1),
 ('b', 2)]
>>>
>>> [(v,k) for k,v in DATA.items()]  # doctest: +NORMALIZE_WHITESPACE
[(1, 'a'),
 (2, 'b')]

>>> DATA = {'a': 1, 'b': 2}
>>>
>>>
>>> {v:k for k,v in DATA.items()}
{1: 'a', 2: 'b'}


Value collision while reversing ``dict``:

>>> DATA = {'a': 1, 'b': 2, 'c': 2}
>>>
>>> {v:k for k,v in DATA.items()}
{1: 'a', 2: 'c'}


Assignments
-----------
.. literalinclude:: assignments/comprehension_dict_a.py
    :caption: :download:`Solution <assignments/comprehension_dict_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/comprehension_dict_b.py
    :caption: :download:`Solution <assignments/comprehension_dict_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/comprehension_dict_c.py
    :caption: :download:`Solution <assignments/comprehension_dict_c.py>`
    :end-before: # Solution
