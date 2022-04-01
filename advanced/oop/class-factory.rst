OOP Class Factory
=================


Class Definition
----------------
>>> class MyClass:
...     pass

>>> MyClass = type('MyClass', (), {})


Static Attributes
-----------------
>>> class MyClass:
...     myattr = 1

>>> MyClass = type('MyClass', (), {'myattr': 1})


Static Methods
--------------
>>> class MyClass:
...     def mymethod():  # noqa
...         pass

>>> def mymethod():
...     pass
>>>
>>> MyClass = type('MyClass', (), {'mymethod': mymethod})


Dynamic Methods
---------------
>>> class MyClass:
...     def mymethod(self):
...         pass

>>> def mymethod(self):
...     pass
>>>
>>> MyClass = type('MyClass', (), {'mymethod': mymethod})


Init Method
-----------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def hello(self):
...         print('hello')
...

>>> def __init__(self, firstname, lastname):
...     self.firstname = firstname
...     self.lastname = lastname
>>>
>>> def hello(self):
...     print('hello')
>>>
>>> Astronaut = type('Astronaut', (), {
...     'hello': hello,
...     '__init__': __init__,
... })


Class Inheritance
-----------------
>>> class Parent:
...     pass
>>>
>>>
>>> class MyClass(Parent):
...     pass

>>> MyClass = type('MyClass', (Parent,), {})


Recap
-----
>>> class Parent:
...     pass
>>>
>>>
>>> class MyClass(Parent):
...     myattr = 1
...
...     def mymethod(self):
...         pass

>>> MyClass = type('MyClass', (Parent,), {'myattr': 1, 'mymethod': mymethod})


Dynamic Class Creation
----------------------
>>> Taikonaut()
Traceback (most recent call last):
NameError: name 'Taikonaut' is not defined
>>>
>>>
>>> for classname in ['Astronaut', 'Cosmonaut', 'Taikonaut']:
...     globals()[classname] = type(classname, (), {})
>>>
>>>
>>> Taikonaut
<class '__main__.Taikonaut'>
>>> Taikonaut()  # doctest: +ELLIPSIS
<__main__.Taikonaut object at 0x...>


Use Case - 0x01
---------------
* Init

>>> Astronaut = type('Astronaut', (), {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
...     'hello': lambda: print('hello')})
>>>
>>> Astronaut.hello()
hello
>>>
>>> vars(Astronaut)  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
mappingproxy({'firstname': 'Mark',
              'lastname': 'Watney',
              'hello': <function <lambda> at 0x...>,
              '__module__': '__main__',
              '__dict__': <attribute '__dict__' of 'Astronaut' objects>,
              '__weakref__': <attribute '__weakref__' of 'Astronaut' objects>,
              '__doc__': None})


Use Case - 0x02
---------------
* Dynamic Classes 1

>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa'),
...         (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...         (7.6, 3.0, 6.6, 2.1, 'virginica')]
>>>
>>>
>>> class Iris:
...     def __init__(self, **kwargs):
...         self.__dict__ = kwargs
...
...     def __repr__(self):
...         clsname = self.__class__.__name__
...         values = tuple(vars(self).values())
...         return f'{clsname}{values}'
>>>
>>>
>>> header, *data = DATA
>>> header = [x.lower().replace(' ', '_') for x in header]
>>>
>>> result = []
>>>
>>> for *features,species in data:
...     features = dict(zip(header, features))
...     clsname = species.capitalize()
...     if clsname not in globals():
...         globals()[clsname] = type(clsname, (Iris,), {})
...     cls = globals()[clsname]
...     iris = cls(**features)
...     result.append(iris)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
[Virginica(5.8, 2.7, 5.1, 1.9),
 Setosa(5.1, 3.5, 1.4, 0.2),
 Versicolor(5.7, 2.8, 4.1, 1.3),
 Virginica(6.3, 2.9, 5.6, 1.8),
 Versicolor(6.4, 3.2, 4.5, 1.5),
 Setosa(4.7, 3.2, 1.3, 0.2),
 Versicolor(7.0, 3.2, 4.7, 1.4),
 Virginica(7.6, 3.0, 6.6, 2.1)]
>>>
>>> vars(result[0])  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.8,
 'sepal_width': 2.7,
 'petal_length': 5.1,
 'petal_width': 1.9}


Use Case - 0x03
---------------
* Dynamic Classes 2

>>> from dataclasses import dataclass
>>> from itertools import zip_longest
>>>
>>>
>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 'setosa'),
...         (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...         (7.6, 3.0,  'virginica')]
>>>
>>>
>>> @dataclass(init=False)
... class Iris:
...     def __init__(self, **kwargs):
...         self.__dict__ = kwargs
>>>
>>>
>>> result = []
>>> header, *data = DATA
>>> header = [x.lower().replace(' ', '_') for x in header]
>>>
>>> for *features,species in data:
...     features = dict(zip_longest(header, features, fillvalue=None))
...     clsname = species.capitalize()
...     if clsname not in globals():
...         globals()[clsname] = type(clsname, (Iris,), {})
...     cls = globals()[clsname]
...     iris = cls(**features)
...     result.append(iris)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
[Virginica(5.8, 2.7, None, None, None),
 Setosa(5.1, 3.5, 1.4, 0.2, None),
 Versicolor(5.7, None, None, None, None),
 Virginica(6.3, 2.9, 5.6, 1.8, None),
 Versicolor(6.4, 3.2, 4.5, 1.5, None),
 Setosa(4.7, 3.2, 1.3, None, None),
 Versicolor(7.0, 3.2, 4.7, 1.4, None),
 Virginica(7.6, 3.0, None, None, None)]
>>>
>>> vars(result[0])  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.8,
 'sepal_width': 2.7,
 'petal_length': None,
 'petal_width': None,
 'species': None}


Use Case - 0x03
---------------
* Factory

>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> class Iris:
...     def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...
...     def __repr__(self):
...         name = self.__class__.__name__
...         values = tuple(self.__dict__.values())
...         return f'{name}{values}'
>>>
>>>
>>> class Setosa(Iris):
...     pass
>>>
>>> class Virginica(Iris):
...     pass
>>>
>>> class Versicolor(Iris):
...     pass
>>>
>>>
>>> def factory(species: str):
...     if species == 'setosa':
...         return Setosa
...     if species == 'virginica':
...         return Virginica
...     if species == 'versicolor':
...         return Versicolor
>>>
>>>
>>> result = []
>>>
>>> for *features, species in DATA[1:]:
...     iris = factory(species)
...     i = iris(*features)
...     result.append(i)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
[Virginica(5.8, 2.7, 5.1, 1.9),
 Setosa(5.1, 3.5, 1.4, 0.2),
 Versicolor(5.7, 2.8, 4.1, 1.3),
 Virginica(6.3, 2.9, 5.6, 1.8),
 Versicolor(6.4, 3.2, 4.5, 1.5),
 Setosa(4.7, 3.2, 1.3, 0.2)]


Use Case - 0x04
---------------
* Dynamic factory

>>> from dataclasses import dataclass
>>>
>>>
>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
>>>
>>> class Setosa(Iris):
...     pass
>>>
>>> class Virginica(Iris):
...     pass
>>>
>>> class Versicolor(Iris):
...     pass
>>>
>>>
>>> def factory(species: str):
...     species = species.capitalize()
...     classes = globals()
...     return classes[species]
>>>
>>>
>>> result = [
...     factory(species)(*features)
...     for *features, species in DATA[1:]
... ]
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
[Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
 Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
 Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
 Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
 Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
 Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2)]


Assignments
-----------
.. literalinclude:: assignments/oop_class_factory_a.py
    :caption: :download:`Solution <assignments/oop_class_factory_a.py>`
    :end-before: # Solution
