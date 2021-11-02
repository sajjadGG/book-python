Comprehension About
===================


Recap
-----
>>> result = []
>>>
>>> for x in range(0,5):
...     result.append(x)
>>>
>>> print(result)
[0, 1, 2, 3, 4]


Syntax
------
.. code-block:: python

    result = [<RETURN> for <VARIABLE> in <ITERABLE>]


Example
-------
>>> result = [x for x in range(0,5)]
>>>
>>> print(result)
[0, 1, 2, 3, 4]


Convention
----------
* Use shorter variable names
* ``x`` is common name

>>> result = [pow(x,2) for x in range(0,5)]

>>> result = [pow(x,2)
...           for x in range(0,5)]


Assignments
-----------
.. literalinclude:: assignments/comprehension_about_a.py
    :caption: :download:`Solution <assignments/comprehension_about_a.py>`
    :end-before: # Solution
