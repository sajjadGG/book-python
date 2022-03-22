Adapter
=======
* EN: Adapter
* PL: Adapter
* Type: class and object


Use Cases
---------
* Convert an interface of an object to a different form
* Like power socket adapter for US and EU
* Refactoring of a large application
* Working with legacy code / database


Problem
-------
* ``BlackAndWhite3rdPartyFilter`` is from external library
* Does not conform to ``Filter`` interface
* Do not have ``apply()`` method
* Need manual call of ``init()`` at initialization
* Need manual call of ``render()``

.. literalinclude:: ../_src/designpatterns-adapter-problem.py
    :language: python


Design
------


Implementation
--------------
* Inheritance is simpler
* Composition is more flexible
* Favor Composition over Inheritance

.. figure:: img/designpatterns-adapter-usecase.png

    Please mind, that on Picture there is a ``Caramel`` filter but in code ``BlackAndWhite3rdPartyFilter``

Inheritance:

    .. literalinclude:: ../_src/designpatterns-adapter-inheritance.py
        :language: python

Composition:

    .. literalinclude:: ../_src/designpatterns-adapter-composition.py
        :language: python


Use Case - 0x01
---------------
>>> def otherrange(a, b, c):  # function with bad API
...     current = a
...     result = []
...     while current < b:
...         result.append(current)
...         current += c
...     return result
>>>
>>>
>>> def myrange(start, stop, step):  # adapter
...     return otherrange(a=start, b=stop, c=step)
>>>
>>>
>>> myrange(start=10, stop=20, step=2)
[10, 12, 14, 16, 18]


.. todo:: Assignments
