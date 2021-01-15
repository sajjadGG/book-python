Adapter
=======


Rationale
---------
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

.. figure:: ../_img/designpatterns-adapter-usecase.png

    Please mind, that on Picture there is a ``Caramel`` filter but in code ``BlackAndWhite3rdPartyFilter``

Inheritance:

    .. literalinclude:: ../_src/designpatterns-adapter-inheritance.py
        :language: python

Composition:

    .. literalinclude:: ../_src/designpatterns-adapter-composition.py
        :language: python


Assignments
-----------
.. todo:: Create assignments
