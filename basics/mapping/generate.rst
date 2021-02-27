Mapping Generate
================


Pair
----
    >>> pair = [
    ...    ('commander', 'Melissa Lewis')]
    >>>
    >>> dict(pair)
    {'commander': 'Melissa Lewis'}


List of Pairs
-------------
    >>> pairs = [
    ...    ('commander', 'Melissa Lewis'),
    ...    ('botanist', 'Mark Watney'),
    ...    ('chemist', 'Alex Vogel')]
    >>>
    >>> dict(pairs)  # doctest: +NORMALIZE_WHITESPACE
    {'commander': 'Melissa Lewis',
      'botanist': 'Mark Watney',
      'chemist': 'Alex Vogel'}


Enumerate
---------
    >>> crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']
    >>> astronaut = enumerate(crew)
    >>>
    >>> next(astronaut)
    (0, 'Melissa Lewis')
    >>> next(astronaut)
    (1, 'Mark Watney')
    >>> next(astronaut)
    (2, 'Alex Vogel')
    >>> next(astronaut)
    Traceback (most recent call last):
    StopIteration

    >>> crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']
    >>>
    >>> list(enumerate(crew))  # doctest: +NORMALIZE_WHITESPACE
    [(0, 'Melissa Lewis'),
     (1, 'Mark Watney'),
     (2, 'Alex Vogel')]
    >>> dict(enumerate(crew))  # doctest: +NORMALIZE_WHITESPACE
    {0: 'Melissa Lewis',
     1: 'Mark Watney',
     2: 'Alex Vogel'}


Zip
---
* ``zip`` is a generator
* ``zip`` will create a list of pairs (like ``dict.items()``)

    >>> roles = ['commander', 'botanist', 'chemist']
    >>> crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']
    >>>
    >>> astronaut = zip(roles, crew)
    >>> next(astronaut)
    ('commander', 'Melissa Lewis')
    >>> next(astronaut)
    ('botanist', 'Mark Watney')
    >>> next(astronaut)
    ('chemist', 'Alex Vogel')
    >>> next(astronaut)
    Traceback (most recent call last):
    StopIteration

    >>> roles = ['commander', 'botanist', 'chemist']
    >>> crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']
    >>>
    >>> list(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
    [('commander', 'Melissa Lewis'),
     ('botanist', 'Mark Watney'),
     ('chemist', 'Alex Vogel')]
    >>>
    >>> dict(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
    {'commander': 'Melissa Lewis',
     'botanist': 'Mark Watney',
     'chemist': 'Alex Vogel'}

    >>> roles = ['commander', 'botanist', 'chemist']
    >>> crew = [('Melissa', 'Lewis'), ('Mark', 'Watney'), ('Alex', 'Vogel')]
    >>>
    >>> astronauts = zip(roles, crew)
    >>> next(astronauts)
    ('commander', ('Melissa', 'Lewis'))
    >>> next(astronauts)
    ('botanist', ('Mark', 'Watney'))
    >>> next(astronauts)
    ('chemist', ('Alex', 'Vogel'))
    >>> next(astronauts)
    Traceback (most recent call last):
    StopIteration

    >>> roles = ['commander', 'botanist', 'chemist']
    >>> crew = [('Melissa', 'Lewis'), ('Mark', 'Watney'), ('Alex', 'Vogel')]
    >>>
    >>> list(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
    [('commander', ('Melissa', 'Lewis')),
     ('botanist', ('Mark', 'Watney')),
     ('chemist', ('Alex', 'Vogel'))]
    >>> dict(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
    {'commander': ('Melissa', 'Lewis'),
     'botanist': ('Mark', 'Watney'),
     'chemist': ('Alex', 'Vogel')}


Assignments
-----------
.. literalinclude:: assignments/mapping_generate_a.py
    :caption: :download:`Solution <assignments/mapping_generate_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_generate_b.py
    :caption: :download:`Solution <assignments/mapping_generate_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_generate_c.py
    :caption: :download:`Solution <assignments/mapping_generate_c.py>`
    :end-before: # Solution
