OOP Stringify Objects
=====================


Rationale
---------
* ``str(obj)`` -> ``obj.__str__()``
* ``repr(obj)`` -> ``obj.__repr__()``
* ``format(obj, name)`` -> ``obj.__format__(name)``
* ``print(obj)`` -> ``str(obj)`` -> ``obj.__str__()``

>>> import datetime
>>> date = datetime.datetime(1961, 4, 12, 6, 7)
>>>
>>> str(date)
'1961-04-12 06:07:00'
>>> repr(date)
'datetime.datetime(1961, 4, 12, 6, 7)'
>>> format(date, '%Y-%m-%d')
'1961-04-12'
>>> print(date)
1961-04-12 06:07:00


String
------
* Calling function ``str(obj)`` calls ``obj.__str__()``
* Calling function ``print(obj)`` calls ``str(obj)``, which calls ``obj.__str__()``
* Method ``obj.__str__()`` must return ``str``
* for end-user

>>> class Astronaut:
...     pass
>>>
>>> astro = Astronaut()
>>> str(astro)  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'

Object without ``__str__()`` method overloaded prints their memory address:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> astro = Astronaut('José Jiménez')
>>>
>>> print(astro)  # doctest: +ELLIPSIS
<Astronaut object at 0x...>
>>> str(astro)  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'
>>> astro.__str__()  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'

Objects can verbose print if ``__str__()`` method is present:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
...
...     def __str__(self):
...         return f'My name... {self.name}'
>>>
>>>
>>> astro = Astronaut('José Jiménez')
>>>
>>> print(astro)
My name... José Jiménez
>>> str(astro)
'My name... José Jiménez'
>>> astro.__str__()
'My name... José Jiménez'


Representation
--------------
* Calling function ``repr(obj)`` calls ``obj.__repr__()``
* Method ``obj.__repr__()`` must return ``str``
* for developers
* object representation
* copy-paste for creating object with the same values
* useful for debugging
* printing ``list`` will call ``__repr__()`` method on each element

>>> class Astronaut:
...     pass
>>>
>>> astro = Astronaut()
>>> repr(astro)  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'

Using ``__repr__()`` on a class:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
...
...     def __repr__(self):
...         return f'Astronaut(name="{self.name}")'
>>>
>>>
>>> astro = Astronaut('José Jiménez')
>>>
>>> repr(astro)
'Astronaut(name="José Jiménez")'
>>> astro
Astronaut(name="José Jiménez")

Printing ``list`` will call ``__repr__()`` method on each element:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
>>>
>>> crew = [Astronaut('Jan Twardowski'),
...         Astronaut('Mark Watney'),
...         Astronaut('Melissa Lewis')]
>>>
>>> print(crew)  # doctest: +ELLIPSIS
[<Astronaut object at 0x...>, <Astronaut object at 0x...>, <Astronaut object at 0x...>]

Printing ``list`` will call ``__repr__()`` method on each element:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
...
...     def __repr__(self):
...         return f'{self.name}'
>>>
>>> crew = [Astronaut('Jan Twardowski'),
...         Astronaut('Mark Watney'),
...         Astronaut('Melissa Lewis')]
>>>
>>> print(crew)
[Jan Twardowski, Mark Watney, Melissa Lewis]


Format
------
* Calling function ``format(obj, fmt)`` calls ``obj.__format__(fmt)``
* Method ``obj.__format__()`` must return ``str``
* Used for advanced formatting

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
...
...     def __format__(self, mood):
...         if mood == 'happy':
...             return f"Yuppi, we're going to space!"
...         elif mood == 'scared':
...             return f"I hope we don't crash"
>>>
>>>
>>> jose = Astronaut('José Jiménez')
>>>
>>> print(f'{jose:happy}')
Yuppi, we're going to space!
>>> print(f'{jose:scared}')
I hope we don't crash

>>> SECOND = 1
>>> MINUTE = 60 * SECOND
>>> HOUR = 60 * MINUTE
>>> DAY = 24 * HOUR
>>>
>>>
>>> class Duration:
...     def __init__(self, seconds):
...         self.seconds = seconds
...
...     def __format__(self, unit):
...         if unit == 'minutes':
...             result = self.seconds / MINUTE
...         elif unit == 'hours':
...             result = self.seconds / HOUR
...         elif unit == 'days':
...             result = self.seconds / DAY
...         return str(round(result, 2))
>>>
>>> duration = Duration(seconds=3600)
>>>
>>> print(f'Duration was {duration:minutes} min')
Duration was 60.0 min
>>> print(f'Duration was {duration:hours} hour')
Duration was 1.0 hour
>>> print(f'Duration was {duration:days} day')
Duration was 0.04 day

>>> SECOND = 1
>>> MINUTE = 60 * SECOND
>>> HOUR = 60 * MINUTE
>>> DAY = 24 * HOUR
>>>
>>>
>>> class Duration:
...     seconds: int
...
...     def __init__(self, seconds):
...         self.seconds = seconds
...
...     def __format__(self, unit):
...         duration = self.seconds
...         unit = 'seconds' if unit == '' else unit
...
...         if unit in ('s', 'sec', 'second', 'seconds'):
...              duration /= SECOND
...         elif unit in ('m', 'min', 'minute', 'minutes'):
...             duration /= MINUTE
...         elif unit in ('h', 'hour', 'hours'):
...             duration /= HOUR
...         elif unit in ('d', 'day', 'days'):
...             duration /= DAY
...         return f'{duration:.2f} {unit}'
...
>>> duration = Duration(seconds=3600)
>>>
>>> print(f'Duration: {duration:s}')
Duration: 3600.00 s
>>> print(f'Duration: {duration:min}')
Duration: 60.00 min
>>> print(f'Duration: {duration:h}')
Duration: 1.00 h
>>> print(f'Duration: {duration:days}')
Duration: 0.04 days

>>> class Temperature:
...     def __init__(self, kelvin):
...         self.kelvin = kelvin
...
...     def to_fahrenheit(self):
...         return (self.kelvin-273.15) * 1.8 + 32
...
...     def to_celsius(self):
...         return self.kelvin - 273.15
...
...     def __format__(self, unit):
...         if unit == 'kelvin':
...             value = self.kelvin
...         elif unit == 'celsius':
...             value = self.to_celsius()
...         elif unit == 'fahrenheit':
...             value = self.to_fahrenheit()
...         unit = unit[0].upper()
...         return f'{value:.2f} {unit}'
>>>
>>>
>>> temp = Temperature(309.75)
>>>
>>> print(f'Temperature is {temp:kelvin}')
Temperature is 309.75 K
>>> print(f'Temperature is {temp:celsius}')
Temperature is 36.60 C
>>> print(f'Temperature is {temp:fahrenheit}')
Temperature is 97.88 F

>>> class Point:
...     def __init__(self, x, y, z=0):
...         self.x = x
...         self.y = y
...         self.z = z
...
...     def __format__(self, name):
...
...         if name == 'in_2D':
...             result = f"Point(x={self.x}, y={self.y})"
...         elif name == 'in_3D':
...             result = f"Point(x={self.x}, y={self.y}, z={self.z})"
...         elif name == 'as_dict':
...             result = self.__dict__
...         elif name == 'as_tuple':
...             result = tuple(self.__dict__.values())
...         elif name == 'as_json':
...             import json
...             result = json.dumps(self.__dict__)
...         return str(result)
>>>
>>>
>>> point = Point(x=1, y=2)
>>>
>>> print(f'{point:in_2D}')
Point(x=1, y=2)
>>> print(f'{point:in_3D}')
Point(x=1, y=2, z=0)
>>> print(f'{point:as_tuple}')
(1, 2, 0)
>>> print(f'{point:as_dict}')
{'x': 1, 'y': 2, 'z': 0}
>>> print(f'{point:as_json}')
{"x": 1, "y": 2, "z": 0}


Assignments
-----------
.. literalinclude:: assignments/oop_stringify_a.py
    :caption: :download:`Solution <assignments/oop_stringify_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_stringify_b.py
    :caption: :download:`Solution <assignments/oop_stringify_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_stringify_c.py
    :caption: :download:`Solution <assignments/oop_stringify_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_stringify_d.py
    :caption: :download:`Solution <assignments/oop_stringify_d.py>`
    :end-before: # Solution
