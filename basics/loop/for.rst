Loop For
========

.. testsetup::

    def spawn_thread():
        pass


Syntax
------
* ``ITERABLE`` must implement ``iterator`` interface
* More information in `Protocol Iterator`

For loop syntax:

.. code-block:: python

    for <variable> in <iterable>:
        <do something>

>>> for digit in [1, 2, 3]:
...     pass


Convention
----------
* The longer the loop scope, the longer the variable name should be
* Avoid one letters if scope is longer than one line
* Prefer locally meaningful name over generic names
* Generic names:

    * ``obj`` - generic name (in Python everything is an object)
    * ``element`` - generic name
    * ``item`` - generic name
    * ``x`` - ok for oneliners, bad for more than one line
    * ``e`` - ok for oneliners, bad for more than one line
    * ``l`` - bad
    * ``o`` - bad
    * ``d`` - bad (for digit)

* Locally meaningful name:

    * ``letter``
    * ``feature``
    * ``digit``
    * ``person``
    * ``color``
    * ``username``
    * etc.

* Special meaning (by convention):

    * ``i`` - for loop counter
    * ``_`` - if value is not used

>>> for digit in [1, 2, 3]:
...     print(digit)
1
2
3

>>> for x in [1, 2, 3]:
...     print(x)
1
2
3

>>> for i in range(0,3):
...     print(i)
0
1
2

>>> for _ in range(3):
...     spawn_thread()


Iterating Sequences
-------------------
* Iterating works for builtin sequences:

    * ``str``
    * ``bytes``
    * ``list``
    * ``tuple``
    * ``set``
    * ``frozenset``
    * ``dict``

>>> for letter in 'setosa':
...     print(letter)
s
e
t
o
s
a

>>> DATA = [5.1, 3.5, 1.4, 0.2, 'setosa']
>>>
>>> for value in DATA:
...     print(value)
5.1
3.5
1.4
0.2
setosa


Range
-----
* ``range(start, stop, step)``
* ``start`` is inclusive, default: ``0``
* ``stop`` is exclusive, required
* ``step`` default: ``1``

>>> range(0, 5)
range(0, 5)

>>> list(range(5))
[0, 1, 2, 3, 4]

>>> list(range(0, 5))
[0, 1, 2, 3, 4]

>>> list(range(0, 5, 1))
[0, 1, 2, 3, 4]

>>> list(range(0, 5, 2))
[0, 2, 4]

Loops with ``range``:

>>> for i in range(0, 3):
...     print(i)
0
1
2

Loops with ``range``:

>>> for number in range(4, 11, 2):
...     print(number)
4
6
8
10


Nested Loops
------------
>>> for row in [1, 2, 3]:  # doctest: +NORMALIZE_WHITESPACE
...     print()
...
...     for column in ['A', 'B', 'C']:
...         print(f'{column}{row}', end=' ')
A1 B1 C1
A2 B2 C2
A3 B3 C3


Assignments
-----------
.. literalinclude:: assignments/loop_for_a.py
    :caption: :download:`Solution <assignments/loop_for_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_b.py
    :caption: :download:`Solution <assignments/loop_for_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_c.py
    :caption: :download:`Solution <assignments/loop_for_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_d.py
    :caption: :download:`Solution <assignments/loop_for_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_e.py
    :caption: :download:`Solution <assignments/loop_for_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_f.py
    :caption: :download:`Solution <assignments/loop_for_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_g.py
    :caption: :download:`Solution <assignments/loop_for_g.py>`
    :end-before: # Solution
