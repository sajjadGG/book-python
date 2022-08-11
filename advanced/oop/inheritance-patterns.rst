OOP Inheritance Patterns
========================
* no inheritance
* single inheritance
* multilevel inheritance
* multiple inheritance (mixin classes)

.. glossary::

    single inheritance
        One class inherits from one other class. Has one parent.

    multilevel inheritance
        One class inherits from other class, and yet another class inherits
        from it. This creates hierarchical structure.

    multiple inheritance
    mixin classes
        One class derives from several other classes at once.


No Inheritance
--------------
>>> class Parent:
...     pass
>>>
>>>
>>> class Child:
...     pass


Single Inheritance
------------------
>>> class Parent:
...     pass
>>>
>>>
>>> class Child(Parent):
...     pass


Multilevel Inheritance
----------------------
>>> class Grandparent:
...     pass
>>>
>>>
>>> class Parent(Grandparent):
...     pass
>>>
>>>
>>> class Child(Parent):
...     pass


Multiple Inheritance
--------------------
* ``Mother`` and ``Father`` are Mixin Classes

>>> class Mother:
...     pass
>>>
>>>
>>> class Father:
...     pass
>>>
>>>
>>> class Child(Mother, Father):
...     pass


Composition
-----------
Static version:

>>> class Mother:
...     pass
>>>
>>> class Father:
...     pass
>>>
>>> class Child:
...     mother = Mother
...     father = Father

Dynamic version:

>>> class Mother:
...     pass
>>>
>>> class Father:
...     pass
>>>
>>>
>>> class Child:
...     mother: Mother
...     father: Father
...
...     def __init__(self, mother=Mother(), father=Father()):
...         self.mother = mother
...         self.father = father


Aggregation
-----------
Static version:

>>> class Mother:
...     pass
>>>
>>> class Father:
...     pass
>>>
>>> class Child:
...     parents = [Father, Mother]

Dynamic version:

>>> class Mother:
...     pass
>>>
>>> class Father:
...     pass
>>>
>>>
>>> class Child:
...     parents: list[Mother|Father]
...
...     def __init__(self, mother=Mother(), father=Father()):
...         self.parents = []
...         self.parents.append(mother)
...         self.parents.append(father)

Why?
----
>>> class Mother:
...     pass
>>>
>>> class Father:
...     pass
>>>
>>>
>>> class Child:
...     mother: Mother
...     father: Father
...
...     def __init__(self, mother=Mother(), father=Father()):
...         self.mother = mother
...         self.father = father

>>> class StepFather:
...     pass
>>>
>>> me = Child(father=StepFather())


Use Case - 0x01
---------------
>>> class Mother:
...     def say_hello(self):
...         pass
>>>
>>> class Father:
...     def say_hello(self):
...         pass
>>>
>>>
>>> class Child:
...     father: Father
...     mother: Mother
...
...     def __init__(self, mother: Mother = Mother(), father: Father = Father()):
...         self.mother = mother
...         self.father = father
...
...     def father_say_hello(self):
...         self.father.say_hello()
...
...     def mother_say_hello(self):
...         self.mother.say_hello()


Use Case - 0x02
---------------
>>> from json import JSONEncoder, JSONDecoder
>>>
>>>
>>> class User:
...     json_encoder: JSONEncoder
...     json_decoder: JSONDecoder
...
...     def __init__(self,
...                  json_encoder: JSONEncoder = JSONEncoder(),
...                  json_decoder: JSONDecoder = JSONDecoder(),
...                  ) -> None:
...         self.json_encoder = json_encoder
...         self.json_decoder = json_decoder
...
...     def json_encode(self, data):
...         self.json_encoder.encode(data)
...
...     def json_decoder(self, data):
...         self.json_decoder.decode(data)


Use Case - 0x03
---------------
>>> from datetime import date
>>> import json

>>> DATA = {'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> json.dumps(DATA)
'{"firstname": "Mark", "lastname": "Watney"}'

>>> DATA = {'firstname': 'Mark', 'lastname': 'Watney', 'birthday': date(1969, 7, 21)}
>>>
>>> json.dumps(DATA)
Traceback (most recent call last):
TypeError: Object of type date is not JSON serializable

>>> class Encoder(json.JSONEncoder):
...     def default(self, x):
...         if isinstance(x, date):
...             return x.isoformat()
...
>>>
>>> DATA = {'firstname': 'Mark', 'lastname': 'Watney', 'birthday': date(1969, 7, 21)}
>>>
>>> json.dumps(DATA, cls=Encoder)
'{"firstname": "Mark", "lastname": "Watney", "birthday": "1969-07-21"}'


Further Reading
---------------
* https://github.com/django/django/blob/main/django/views/generic/base.py
* https://github.com/pandas-dev/pandas/blob/main/pandas/core/frame.py
* https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/linear_model/_base.py#L533

Assignments
-----------
.. literalinclude:: assignments/oop_inheritance_patterns_a.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_inheritance_patterns_b.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_inheritance_patterns_c.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_inheritance_patterns_d.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_d.py>`
    :end-before: # Solution
