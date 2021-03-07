Polymorphism
============


Switch
------
It all starts with single ``if`` statement

>>> language = 'English'
>>>
>>> if language == 'Polish':
...     result = 'Witaj'
... elif language == 'English':
...     result = 'Hello'
>>>
>>> print(result)
Hello

It quickly grows into multiple ``elif``:

>>> language = 'English'
>>>
>>> if language == 'Polish':
...     result = 'Witaj'
... elif language == 'English':
...     result = 'Hello'
... elif language == 'Russian':
...     result = 'Привет'
... else:
...     result = 'Unknown language'
>>>
>>> print(result)
Hello

In other languages you may find ``switch`` statement:
(note that this is not a valid Python code)

>>> # doctest: +SKIP
...
... switch(language):
...     case 'Polish':
...         result = 'Witaj'
...     case 'English':
...         result = 'Hello'
...     case 'Russian':
...         result = 'Привет'
...     default:
...         result = 'Unknown language'

It's a bit cleaner, but essentially the same.
Problem is that, ``switch`` moves business logic to the execution place:

>>> SWITCH = {'Polish': 'Witaj',
...           'English': 'Hello',
...           'German': 'Guten Tag'}
>>>
>>> language = 'English'
>>>
>>> SWITCH.get(language, 'Unknown language')
'Hello'

>>> def switch(key):
...     return {
...         'Polish': 'Witaj',
...         'English': 'Hello',
...         'Russian': 'Привет',
...     }.get(key, 'Unknown language')
>>>
>>> switch('English')
'Hello'
>>> switch('Russian')
'Привет'


Pattern Matching
----------------
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial
* x ⟼ assign x = subject
* 'x' ⟼ test subject == 'x'
* x.y ⟼ test subject == x.y
* x() ⟼ test isinstance(subject, x)
* {'x': 'y'} ⟼ test isinstance(subject, Mapping) and subject.get('x') == 'y'
* ['x'] ⟼ test isinstance(subject, Sequence) and len(subject) == 1 and subject[0] == 'x'
* Source: [#patternmatching]_

>>> language = 'English'
>>>
>>> # doctest: +SKIP
... match language:
...     case 'Polish':
...         result = 'Witaj'
...     case 'English':
...         result = 'Hello'
...     case 'Russian':
...         result = 'Привет'
...     case _:
...         result = 'Unknown language'

>>> status = 418
>>>
>>> # doctest: +SKIP
... match status:
...     case 400:
...         result = 'Bad request'
...     case 401 | 403 | 405:
...         result = 'Not allowed'
...     case 404:
...         result = 'Not found'
...     case 418:
...         result = "I'm a teapot"
...     case _:
...         result = 'Unexpected status'

>>> request = 'GET /index.html HTTP/2.0'
>>>
>>> # doctest: +SKIP
... match request.split():
...     case ['GET', uri, version]:
...         server.get(uri)
...     case ['POST', uri, version]:
...         server.post(uri)
...     case ['PUT', uri, version]:
...         server.put(uri)
...     case ['DELETE', uri, version]:
...         server.delete(uri)

>>> class Hero:
...     def action():
...         return  ['move', 'left', 20]
>>>
>>> # doctest: +SKIP
... match hero.action():
...     case ['move', ('up'|'down'|'left'|'right') as direction, value]:
...         hero.move(direction, value)
...     case ['make_damage', value]:
...         hero.make_damage(value)
...     case ['take_damage', value]:
...         hero.take_damage(value)

>>> from enum import Enum
>>>
>>> class Key(Enum):
...     ESC = 27
...     ARROW_LEFT = 37
...     ARROW_UP = 38
...     ARROW_RIGHT = 39
...     ARROW_DOWN = 40
>>>
>>> # doctest: +SKIP
... match keyboard.on_key_press():
...     case Key.ESC:
...         game.quit()
...     case Key.ARROW_LEFT:
...         game.move_left()
...     case Key.ARROW_UP:
...         game.move_up()
...     case Key.ARROW_RIGHT:
...         game.move_right()
...     case Key.ARROW_DOWN:
...         game.move_down()
...     case _:
...         raise ValueError(f'Unrecognized key')

>>> from enum import Enum
>>>
>>> class Color(Enum):
...     RED = 0
...     BLUE = 1
...     BLACK = 2
>>>
>>> # doctest: +SKIP
... match color:
...     case Color.RED:
...         print('Soviet')
...     case Color.BLUE:
...         print('Allies')
...     case Color.BLACK:
...         print('Axis')

>>> from enum import Enum
>>>
>>> class SpaceMan(Enum):
...     NASA = 'Astronaut'
...     ESA = 'Astronaut'
...     ROSCOSMOS = 'Cosmonaut'
...     CNSA = 'Taikonaut'
...     ISRO = 'GaganYatri'
>>>
>>> # doctest: +SKIP
... match agency:
...     case SpaceMan.NASA:
...         print('USA')
...     case SpaceMan.ESA:
...         print('Europe')
...     case SpaceMan.ROSCOSMOS:
...         print('Russia')
...     case SpaceMan.CNSA:
...         print('China')
...     case SpaceMan.ISRO:
...         print('India')


Polymorphism
------------
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
...         Cosmonaut('Jan Twardowski')]
>>>
>>> hello(crew)
Hello Mark Watney
Привет Иван Иванович
Hello Melissa Lewis
Привет Jan Twardowski

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
...         Cosmonaut('Jan Twardowski')]
>>>
>>> for member in crew:
...     print(member.say_hello())
Hello Mark Watney
Привет Иван Иванович
Hello Melissa Lewis
Привет Jan Twardowski


Use Cases
---------
UIElement:

>>> from abc import ABCMeta, abstractmethod
>>>
>>>
>>> class UIElement(metaclass=ABCMeta):
...     @abstractmethod
...     def render(self):
...         pass
>>>
>>> class Textarea(UIElement):
...     def render(self):
...         print('Rendering Textarea')
>>>
>>> class Button(UIElement):
...     def render(self):
...         print('Rendering Button')
>>>
>>>
>>> def render(element: UIElement):
...     element.render()
>>>
>>>
>>> render(Textarea())
Rendering Textarea
>>> render(Button())
Rendering Button

Factory:

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

Dynamic factory:

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
.. todo:: Create assignments


References
----------
.. [#patternmatching] Raymond Hettinger. Accessed Date: 2021-03-07. URL: https://twitter.com/raymondh/status/1361780586570948609?s=20
