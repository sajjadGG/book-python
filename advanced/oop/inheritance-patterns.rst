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


.. figure:: img/uml-relations-inheritance-simple.png


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


.. figure:: img/uml-relations-inheritance-multilevel.png


Composition
-----------
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
...     def __init__(self):
...         self.mother = Mother()
...         self.father = Father()


Aggregation
-----------
>>> class Parent:
...     pass
>>>
>>> class Mother(Parent):
...     pass
>>>
>>> class Father(Parent):
...     pass
>>>
>>>
>>> class Child:
...     parents: list[Parent]
...
...     def __init__(self):
...         self.parents = []
...         self.parents.append(Mother())
...         self.parents.append(Father())


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
