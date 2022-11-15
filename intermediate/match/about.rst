Match About
===========
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial
* Significantly faster for sequences and mappings [#Shaw2022]_
* Since Python 3.11: For sequences if faster around 80% [#Shaw2022]_
* Since Python 3.11: For mappings if faster around 80% [#Shaw2022]_


Problem
-------
>>> choice = 'r'
>>>
>>> if choice == 'r':
...     color = 'red'
... elif choice == 'g':
...     color = 'green'
... elif choice == 'b':
...     color = 'blue'
... else:
...     color = None


Pattern Matching
----------------
New ``match`` syntax allows to be ``PEP-8`` compliant while having
clear syntax without condition repetitions:

>>> choice = 'r'
>>>
>>> match choice:
...     case 'r': color = 'red'
...     case 'g': color = 'green'
...     case 'b': color = 'blue'
...     case _:   color = None


Syntax
------
>>> # doctest: +SKIP
... match <object>:
...     case <option>: <action>
...     case <option>: <action>
...     case <option>: <action>
...     case _: <default action>


Patterns
--------
* literal pattern
* capture pattern
* wildcard pattern
* constant value pattern
* sequence pattern
* mapping pattern
* class pattern
* OR pattern
* walrus pattern

Patterns don't just have to be literals. The patterns can also:

* Use variable names that are set if a ``case`` matches
* Match sequences using list or tuple syntax (like Python's existing ``iterable unpacking`` feature)
* Match mappings using ``dict`` syntax
* Use ``*`` to match the rest of a list
* Use ``**`` to match other keys in a dict
* Match objects and their attributes using class syntax
* Include "or" patterns with ``|``
* Capture sub-patterns with ``as``
* Include an ``if`` "guard" clause



Recap
-----
* ``x`` - assign ``x = subject``
* ``'x'`` - test ``subject == 'x'``
* ``x.y`` - test ``subject == x.y``
* ``x()`` - test ``isinstance(subject, x)``
* ``{'x': 'y'}`` - test ``isinstance(subject, Mapping) and subject.get('x') == 'y'``
* ``['x']`` - test ``isinstance(subject, Sequence) and len(subject) == 1 and subject[0] == 'x'``
* Source: [#Hettinger2021]_


Further Reading
---------------
* https://peps.python.org/pep-0622/
* https://peps.python.org/pep-0636/


References
----------
.. [#Shaw2022] Anthony Shaw. Write faster Python! Common performance anti patterns. Year: 2022. Retrieved: 2022-06-09. URL: https://youtu.be/YY7yJHo0M5I?t=1555

.. [#Hettinger2021] Raymond Hettinger. Year: 2021. Retrieved: 2021-03-07. URL: https://twitter.com/raymondh/status/1361780586570948609?s=20

.. todo:: Assignments
