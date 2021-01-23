Conditional Expressions
=======================


Conjunction
-----------
    >>> firstname = 'Mark'
    >>> lastname = 'Watney'
    >>>
    >>> if firstname == 'Mark' and lastname == 'Watney':
    ...     print('Hello Space Pirate')
    ... else:
    ...     print('Sorry, astronauts only')
    Hello Space Pirate


Disjunction
-----------
    >>> name = 'Watney'
    >>>
    >>> if name == 'Watney' or name == 'Twardowski':
    ...     print('Hello astronaut')
    ... else:
    ...     print('Sorry, astronauts only')
    Hello astronaut


Boolean Algebra
---------------
* Use parenthesis for explicit order

    >>> firstname = 'José'
    >>> lastname = 'Jiménez'
    >>>
    >>> if (firstname == 'Mark' and lastname == 'Watney') \
    ...         or (firstname == 'Jan' and lastname == 'Twardowski') \
    ...         or (firstname == 'Melissa' and lastname == 'Lewis'):
    ...
    ...     print('Hello astronaut')
    ... else:
    ...     print('Sorry, astronauts only')
    Sorry, astronauts only

Complex conditions:

    >>> # doctest: +SKIP
    ... for line in file:
    ...    if line and (not line.startswith('#') or not line.isspace()):
    ...        ...

    >>> # doctest: +SKIP
    ... for line in file:
    ...   if len(line) == 0:
    ...       continue
    ...
    ...   if line.startswith('#'):
    ...       continue
    ...
    ...   if line.isspace():
    ...       continue
    ...


Contains
--------
    >>> text = 'Monty Python'
    >>>
    >>> if 'Python' in text:
    ...     print('Yes')
    ... else:
    ...     print('No')
    Yes

    >>> crew = ['Lewis', 'Watney', 'Twardowski']
    >>>
    >>> if 'Jiménez' in crew:
    ...     print('Yes')
    ... else:
    ...     print('No')
    No

    >>> crew = {'Lewis', 'Watney', 'Twardowski'}
    >>>
    >>> if 'Jiménez' in crew:
    ...     print('Yes')
    ... else:
    ...     print('No')
    No


Identity
--------
    >>> name = None
    >>>
    >>> if name is None:
    ...    print('Name is empty')
    Name is empty


Negation
--------
* ``not`` negates (logically inverts) condition

    >>> name = None
    >>>
    >>> if not name:
    ...    print('Name is empty')
    Name is empty

    >>> crew = {'Lewis', 'Watney', 'Twardowski'}
    >>>
    >>> if 'Ivanovich' not in crew:
    ...    print('You are not assigned to the crew')
    You are not assigned to the crew

    >>> name = None
    >>>
    >>> if name is not None:
    ...    print(name)


Assignments
-----------
.. literalinclude:: assignments/controlflow_conditional_expression.py
    :caption: :download:`Solution <assignments/controlflow_conditional_expression.py>`
    :end-before: # Solution
