OOP Principles
==============


Rationale
---------
* Encapsulation
* Abstraction
* Inheritance
* Polymorphism


Encapsulation
-------------
* Do not allow to modify attributes directly
* Hide them behind setters and getters
* Prevents objects to get to an invalid state

>>> position_x = 0
>>> position_y = 0
>>>
>>> def position_set(x, y):
...     global position_x
...     global position_y
...     position_x = x
...     position_y = y
>>>
>>> def position_get():
...     return position_x, position_y
>>>
>>> position_set(1, 2)
>>> position_get()
(1, 2)

>>> class Position:
...     x: int = 0
...     y: int = 0
...
...     def set(self, x, y):
...         self.x = x
...         self.y = y
...
...     def get(self):
...         return self.x, self.y
>>>
>>> position = Position()
>>> position.set(1, 2)
>>> position.get()
(1, 2)


Abstraction
-----------
* Reduce complexity by hiding unnecessary details
* User do not need what does it mean to send email, that you have to connect, auth and later disconnect

>>> class MarsMission:
...     def send_astronauts(self, astronauts):
...         self._develop_tools()
...         self._develop_rocket()
...         self._train_crew(astronauts)
...         self._launch_rocket()
...         self._navigate_in_space()
...         self._land()
...         self._first_step_on_mars(astronauts)
...
...     def _develop_tools(self):
...         print('Developing Tools')
...
...     def _develop_rocket(self):
...         print('Developing Rocket')
...
...     def _train_crew(self, astronauts):
...         print('Training Crew')
...
...     def _launch_rocket(self):
...         print('Launch Rocket')
...
...     def _navigate_in_space(self):
...         print('Navigate in space')
...
...     def _land(self):
...         print('Entry, descend and landing')
...
...     def _first_step_on_mars(self, astronauts):
...         print('First step on Mars')
>>>
>>>
>>> mars = MarsMission()
>>> mars.send_astronauts(['Mark Watney', 'Melissa Lewis', ...])
Developing Tools
Developing Rocket
Training Crew
Launch Rocket
Navigate in space
Entry, descend and landing
First step on Mars


Inheritance
-----------
>>> class Person:
...     firstname: str
...     lastname: str
...
...     def say_hello(self):
...         print(f'Hello {self.firstname} {self.lastname}')
>>>
>>>
>>> class Astronaut(Person):
...     pass
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>> astro.say_hello()
Hello Mark Watney


Polymorphism
------------
* Ability of an object to take many forms

>>> class Person:
...     def __init__(self, name):
...         self.name = name
...
...     def say_hello(self):
...         pass
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


Further Reading
---------------
* https://www.youtube.com/watch?v=NU_1StN5Tkk
