OOP Class Instance
==================
* Instances are also known as Objects
* Two newlines between class and code
* ``snake_case`` names

.. glossary::

    instance
    object
        Object created from class.



Class vs Instance
-----------------
.. figure:: img/oop-classes-class.jpg

    Class. Source: [#class]_

.. figure:: img/oop-classes-instances.jpg

    Instances. Source: [#instances]_


Instances
---------
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
>>> lewis = Astronaut()
>>> martinez = Astronaut()

Two classes and two instances:

>>> class Astronaut:
...     pass
>>>
>>> class Cosmonaut:
...     pass
>>>
>>>
>>> watney = Astronaut()
>>> twardowski = Cosmonaut()

Two classes and four instances (two instances of an ``Astronaut`` class,
and two of a ``Cosmonaut`` class):

>>> class SeniorAstronaut:
...     pass
>>>
>>> class SeniorCosmonaut:
...     pass
>>>
>>>
>>> mark_watney = SeniorAstronaut()
>>> melissa_lewis = SeniorAstronaut()
>>> pan_twardowski = SeniorCosmonaut()

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
>>> rick_martinez = AstronautPilot()
>>> alex_vogel = AstronautEngineer()


Use Case - 0x01
---------------
>>> a = int()
>>> b = float()
>>> c = bool()
>>> d = str()
>>> e = list()
>>> f = tuple()
>>> g = set()
>>> h = dict()


References
----------
.. [#class] http://makieta.pl/12344-thickbox_default/faller-130803-blok-z-wielkiej-plyty-skala-h0.jpg
.. [#instances] https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Os_Rusa_Poznań_RB1.jpg/1200px-Os_Rusa_Poznań_RB1.jpg


Assignments
-----------
.. literalinclude:: assignments/oop_class_instance_a.py
    :caption: :download:`Solution <assignments/oop_class_instance_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_class_instance_b.py
    :caption: :download:`Solution <assignments/oop_class_instance_b.py>`
    :end-before: # Solution
