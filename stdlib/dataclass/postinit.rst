Dataclass Postinit
==================


Rationale
---------
* Dataclasses generate ``__init__()``
* Overloading ``__init__()`` manually will destroy it
* For init time validation there is ``__post_init__()``
* It is run after all parameters are set in the class
* Hence you have to take care about negative cases (errors)


Initial Validation in Classes
-----------------------------
>>> class Kelvin:
...     def __init__(self, value):
...         if value < 0.0:
...             raise ValueError('Temperature must be greater than 0')
...         else:
...             self.value = value
>>>
>>>
>>> t = Kelvin(-1)
Traceback (most recent call last):
ValueError: Temperature must be greater than 0


Initial Validation in Dataclasses
---------------------------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Kelvin:
...     value: float = 0.0
...
...     def __post_init__(self):
...         if self.value < 0.0:
...             raise ValueError('Temperature must be greater than 0')
>>>
>>>
>>> t = Kelvin(-1)
Traceback (most recent call last):
ValueError: Temperature must be greater than 0

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     publicname: str = field(init=False)
...
...     def __post_init__(self):
...         self.publicname = f'{self.firstname} {self.lastname[0]}.'


InitVar
-------
* Init-only fields are added as parameters to the generated ``__init__`` method, and are passed to the optional ``__post_init__`` method
* They are not otherwise used by Data Classes

>>> # doctest: +SKIP
... from dataclasses import dataclass, InitVar
...
...
... @dataclass
... class Astronaut:
...     fullname: InitVar[str] = None
...     _firstname: str = None
...     _lastname: str = None
...
...     def __post_init__(self, fullname: str):
...         fullname = fullname.split()
...         self._firstname = fullname[0]
...         self._lastname = fullname[1]
...
...
... astro = Astronaut('Mark Watney')
...
... print(astro._firstname)
Mark
... print(astro._lastname)
Watney
