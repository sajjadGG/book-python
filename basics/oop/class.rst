OOP Classes and Instances
=========================


Rationale
---------
* Object Oriented Paradigm
* Model world as objects that interacts with each other

.. glossary::

    class
        Templates for objects.

    instance
    object
        Object created from class.


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


Instances
---------
* Instances are also known as Objects
* Two newlines between class and code
* ``snake_case`` names

One class and one instance:

>>> class Astronaut:
...     pass
>>>
>>>
>>> watney = Astronaut()

One class and three instances:

>>> class Astronaut:
...     pass
>>>
>>>
>>> watney = Astronaut()
>>> twardowski = Astronaut()
>>> jimenez = Astronaut()

Two classes and two instances:

>>> class Astronaut:
...     pass
>>>
>>> class Cosmonaut:
...     pass
>>>
>>>
>>> mark = Astronaut()
>>> ivan = Cosmonaut()

Two classes and four instances (two instances of an ``Astronaut`` class, and two of a ``Cosmonaut`` class):

>>> class SeniorAstronaut:
...     pass
>>>
>>> class SeniorCosmonaut:
...     pass
>>>
>>>
>>> mark_watney = SeniorAstronaut()
>>> melissa_lewis = SeniorAstronaut()
>>> ivan_ivanovich = SeniorCosmonaut()
>>> jan_twardowski = SeniorCosmonaut()


Class vs Instance
-----------------
.. figure:: img/oop-classes-class.jpg

    Class. Source: [#class]_

.. figure:: img/oop-classes-instances.jpg

    Instances. Source: [#instances]_


Convention
----------
* Never print in a class
* One class per file - when classes are long
* All classes in one file - when classes are short
* You can mix classes and functions in one file

Classes and Objects:

>>> class AstronautEngineer:
...     pass
>>>
>>> class AstronautScientist:
...     pass
>>>
>>> class AstronautPilot:
...     pass
>>>
>>>
>>> mark_watney = AstronautScientist()
>>> melissa_lewis = AstronautScientist()
>>> jose_jimenez = AstronautEngineer()
>>> jan_twardowski = AstronautPilot()

>>> def hello():
...     pass
>>>
>>> class Astronaut:
...     pass
>>>
>>>
>>> mark = Astronaut()
>>> jose = Astronaut()


Use Cases
---------
>>> a = int()
>>> b = float()
>>> c = bool()
>>> d = str()
>>> e = list()
>>> f = tuple()
>>> g = set()
>>> h = frozenset()
>>> i = dict()


References
----------
.. [#class] http://makieta.pl/12344-thickbox_default/faller-130803-blok-z-wielkiej-plyty-skala-h0.jpg
.. [#instances] https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Os_Rusa_Poznań_RB1.jpg/1200px-Os_Rusa_Poznań_RB1.jpg


Assignments
-----------
.. literalinclude:: assignments/oop_class_a.py
    :caption: :download:`Solution <assignments/oop_class_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_class_b.py
    :caption: :download:`Solution <assignments/oop_class_b.py>`
    :end-before: # Solution
