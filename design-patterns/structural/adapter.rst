Adapter
=======
* EN: Adapter
* PL: Adapter
* Type: class and object


Pattern
-------
* Convert an interface of an object to a different form
* Like power socket adapter for US and EU
* Refactoring of a large application
* Working with legacy code / database
* Niekompatybilne API dwóch systemów
* Wymagające różnych sposobów uwierzytelniania (OAuth2, BasicAuth)
* Tłumaczenie pomiędzy różnymi formatami danych (SOAP/XML, REST/JSON)
* Iteracyjne przepisywanie legacy systemu na nowy, ale tak, aby móc wciąż korzystać ze starego


.. figure:: img/designpatterns-adapter-pattern.png

.. literalinclude:: uml/designpatterns-adapter-pattern.md
    :language: md


Problem
-------
* ``BlackAndWhite3rdPartyFilter`` is from external library
* Does not conform to ``Filter`` interface
* Do not have ``apply()`` method
* Need manual call of ``init()`` at initialization
* Need manual call of ``render()``

.. figure:: img/designpatterns-adapter-problem.png

.. literalinclude:: uml/designpatterns-adapter-problem.md
    :language: md

.. literalinclude:: src/designpatterns-adapter-problem.py
    :language: python


Solution
--------
* Inheritance is simpler
* Composition is more flexible
* Favor Composition over Inheritance

.. figure:: img/designpatterns-adapter-solution.png

    Please mind, that on Picture there is a ``Caramel`` filter but in code ``BlackAndWhite3rdPartyFilter``

.. literalinclude:: uml/designpatterns-adapter-solution.md
    :language: md

.. literalinclude:: src/designpatterns-adapter-solution.py
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


Assignments
-----------
.. todo:: Assignments
