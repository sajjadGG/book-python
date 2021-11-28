OOP Classes and Instances
=========================


Rationale
---------
* Object Oriented Paradigm
* Model world as objects that interacts with each other

.. glossary::

    class
        Templates for objects.


Classes
-------
* Classes are templates for objects
* ``PascalCase`` name convention

Classes should have capitalized name:

>>> class Astronaut:
...     pass

Multi-word class names should use ``PascalCase``:

>>> class SeniorAstronaut:
...     pass


Good Practices
--------------
* Never print in a class
* All classes in one file - when classes are short
* One class per file - when classes are long

You can mix classes and functions in one file:

>>> def say_hello():
...     pass
>>>
>>>
>>> class Astronaut:
...     pass


Use Case - 0x01
---------------
>>> class AstronautEngineer:
...     pass
>>>
>>>
>>> class AstronautScientist:
...     pass
>>>
>>>
>>> class AstronautPilot:
...     pass


Assignments
-----------
.. literalinclude:: assignments/oop_class_define_a.py
    :caption: :download:`Solution <assignments/oop_class_define_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_class_define_b.py
    :caption: :download:`Solution <assignments/oop_class_define_b.py>`
    :end-before: # Solution
