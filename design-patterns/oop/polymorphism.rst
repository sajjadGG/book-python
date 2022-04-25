OOP Polymorphism
================


Polymorphism
------------
>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class Language(ABC):
...     @abstractmethod
...     def hello(self): ...
>>>
>>>
>>> class Polish(Language):
...     def hello(self):
...         print('Witaj')
>>>
>>>
>>> class English(Language):
...     def hello(self):
...         print('Hello')
>>>
>>>
>>> class German(Language):
...     def hello(self):
...         print('Guten Tag')
>>>
>>>
>>> language = Polish()
>>> language.hello()
Witaj

Use Case - 0x01
---------------
* Astronauts

>>> from abc import ABCMeta, abstractmethod
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Person(metaclass=ABCMeta):
...     name: str
...
...     @abstractmethod
...     def say_hello(self):
...         pass
>>>
>>>
>>> class Astronaut(Person):
...     def say_hello(self):
...         return f'Hello {self.name}'
>>>
>>> class Cosmonaut(Person):
...     def say_hello(self):
...         return f'Привет {self.name}'
>>>
>>>
>>> def hello(crew: list[Person]) -> None:
...     for member in crew:
...         print(member.say_hello())
>>>
>>>
>>> crew = [Astronaut('Mark Watney'),
...         Cosmonaut('Иван Иванович'),
...         Astronaut('Melissa Lewis'),
...         Cosmonaut('Pan Twardowski')]
>>>
>>> hello(crew)
Hello Mark Watney
Привет Иван Иванович
Hello Melissa Lewis
Привет Pan Twardowski

In Python, due to the duck typing and dynamic nature of the language, the Interface or abstract class is not needed to do polymorphism:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     name: str
...
...     def say_hello(self):
...         return f'Hello {self.name}'
>>>
>>> @dataclass
... class Cosmonaut:
...     name: str
...
...     def say_hello(self):
...         return f'Привет {self.name}'
>>>
>>>
>>> crew = [Astronaut('Mark Watney'),
...         Cosmonaut('Иван Иванович'),
...         Astronaut('Melissa Lewis'),
...         Cosmonaut('Pan Twardowski')]
>>>
>>> for member in crew:
...     print(member.say_hello())
Hello Mark Watney
Привет Иван Иванович
Hello Melissa Lewis
Привет Pan Twardowski


Use Case - 0x02
---------------
* UI Elements

>>> from abc import ABCMeta, abstractmethod
>>>
>>>
>>> class UIElement(metaclass=ABCMeta):
...     def __init__(self, name):
...         self.name = name
...
...     @abstractmethod
...     def render(self):
...         ...
>>>
>>>
>>> class Textarea(UIElement):
...     def render(self):
...         print(f'Rendering {self.name} Textarea')
>>>
>>> class Button(UIElement):
...     def render(self):
...         print(f'Rendering {self.name} Button')
>>>
>>>
>>> def render(elements: list[UIElement]):
...     for element in elements:
...         element.render()
>>>
>>>
>>> render([
...     Textarea('Username'),
...     Textarea('Password'),
...     Button('Submit'),
... ])
Rendering Username Textarea
Rendering Password Textarea
Rendering Submit Button


Use Case - 0x03
---------------
* Static Factory

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


References
----------
.. [#patternmatching] Raymond Hettinger. Retrieved: 2021-03-07. URL: https://twitter.com/raymondh/status/1361780586570948609?s=20


.. todo:: Assignments
