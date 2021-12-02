Operators Stringify
===================


Rationale
---------
.. csv-table:: String Operator Overload
    :header: "Operator", "Method"

    "``str(obj)``",           "``obj.__str__()``"
    "``repr(obj)``",          "``obj.__repr__()``"
    "``format(obj, name)``",  "``obj.__format__(name)``"
    "``print(obj)``",         "``str(obj)`` -> ``obj.__str__()``"

    "``obj + other``",        "``obj.__add__(other)``"
    "``obj - other``",        "``obj.__sub__(other)``"
    "``obj * other``",        "``obj.__mul__(other)``"
    "``obj % other``",        "``obj.__mod__(other)``"

    "``obj += other``",       "``obj.__iadd__(other)``"
    "``obj -= other``",       "``obj.__isub__(other)``"
    "``obj *= other``",       "``obj.__imul__(other)``"
    "``obj %= other``",       "``obj.__imod__(other)``"


Example
-------
>>> import datetime
>>>
>>>
>>> date = datetime.date(1961, 4, 12)
>>>
>>>
>>> str(date)
'1961-04-12'
>>>
>>> repr(date)
'datetime.date(1961, 4, 12)'
>>>
>>> format(date, '%Y-%m-%d')
'1961-04-12'
>>>
>>> print(date)
1961-04-12


String
------
* Calling function ``str(obj)`` calls ``obj.__str__()``
* Calling function ``print(obj)`` calls ``str(obj)``, which calls ``obj.__str__()``
* Method ``obj.__str__()`` must return ``str``
* for end-user

>>> class Astronaut:
...     pass
>>>
>>>
>>> astro = Astronaut()
>>>
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
>>>
>>> str(astro)  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'
>>>
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
>>>
>>> str(astro)
'My name... José Jiménez'
>>>
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
>>>
>>> astro = Astronaut()
>>>
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
>>>
>>> astro
Astronaut(name="José Jiménez")

Printing ``list`` will call ``__repr__()`` method on each element:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
>>>
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
>>>
>>> print(f'{jose:scared}')
I hope we don't crash


Use Case - 0x01
---------------
* ``%`` (``__mod__``) operator behavior for ``int`` and ``str``:

>>> 13 % 4
1
>>>
>>> '13' % '4'
Traceback (most recent call last):
TypeError: not all arguments converted during string formatting

>>> pi = 3.1514
>>>
>>>
>>> 'String: %s' % pi
'String: 3.1514'
>>>
>>> 'Double: %d' % pi
'Double: 3'
>>>
>>> 'Float: %f' % pi
'Float: 3.151400'

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>>
>>> 'Hello %s' % firstname
'Hello Mark'
>>>
>>> 'Hello %s %s' % (firstname, lastname)
'Hello Mark Watney'
>>>
>>> 'Hello %(fname)s %(lname)s' % {'fname': firstname, 'lname': lastname}
'Hello Mark Watney'

>>> text = 'Hello %s'
>>> text %= 'Mark Watney'
>>>
>>> print(text)
Hello Mark Watney

>>> class Str:
...     def __mod__(self, other):
...         """str substitute"""
...
...         if type(other) is str:
...             ...
...         if type(other) is tuple:
...             ...
...         if type(other) is dict:
...             ...

Note, that using ``%s``, ``%d``, ``%f`` is currently deprecated in favor
of ``f'...'`` string formatting. More information in `Builtin Printing`


Use Case - 0x02
---------------
* Self formatting duration

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
>>>
>>> duration = Duration(seconds=3600)
>>>
>>>
>>> print(f'Duration was {duration:minutes} min')
Duration was 60.0 min
>>>
>>> print(f'Duration was {duration:hours} hour')
Duration was 1.0 hour
>>>
>>> print(f'Duration was {duration:days} day')
Duration was 0.04 day


Use Case - 0x03
---------------
* Duration Many Units

>>> SECOND = 1
>>> MINUTE = 60 * SECOND
>>> HOUR = 60 * MINUTE
>>> DAY = 24 * HOUR
>>> MONTH = 30.436875 * DAY
>>> YEAR = 365.2425 * DAY
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
...         if unit in ('seconds', 'second', 'sec', 's'):
...             duration /= SECOND
...         elif unit in ('minutes', 'minute', 'min', 'm'):
...             duration /= MINUTE
...         elif unit in ('hours', 'hour', 'hr', 'h'):
...             duration /= HOUR
...         elif unit in ('days', 'day', 'd'):
...             duration /= DAY
...         elif unit in ('months', 'month', 'mth'):
...             duration /= MONTH
...         elif unit in ('years', 'year', 'yr', 'y'):
...             duration /= YEAR
...         else:
...             raise ValueError('Invalid unit')
...         return f'{duration:.2f} {unit}'
>>>
>>>
>>> ares3 = Duration(seconds=187368216)
>>>
>>>
>>> print(f'Ares3 mission length was {ares3:seconds}')
Ares3 mission length was 187368216.00 seconds
>>>
>>> print(f'Ares3 mission length was {ares3:min}')
Ares3 mission length was 3122803.60 min
>>>
>>> print(f'Ares3 mission length was {ares3:h}')
Ares3 mission length was 52046.73 h
>>>
>>> print(f'Ares3 mission length was {ares3:days}')
Ares3 mission length was 2168.61 days
>>>
>>> print(f'Ares3 mission length was {ares3:years}')
Ares3 mission length was 5.94 years


Use Case - 0x04
---------------
* Temperature conversion

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
>>> temp = Temperature(kelvin=309.75)
>>>
>>>
>>> print(f'Temperature is {temp:kelvin}')
Temperature is 309.75 K
>>>
>>> print(f'Temperature is {temp:celsius}')
Temperature is 36.60 C
>>>
>>> print(f'Temperature is {temp:fahrenheit}')
Temperature is 97.88 F


Use Case - 0x05
---------------
* Format output

>>> class Point:
...     def __init__(self, x, y, z=0):
...         self.x = x
...         self.y = y
...         self.z = z
...
...     def __format__(self, name):
...
...         if name in ('2D', '2d', '2dimensions'):
...             result = f"Point(x={self.x}, y={self.y})"
...         elif name in ('3D', '3d', '3dimensions'):
...             result = f"Point(x={self.x}, y={self.y}, z={self.z})"
...         elif name == 'as_dict':
...             result = vars(self)
...         elif name == 'as_tuple':
...             result = tuple(vars(self).values())
...         elif name == 'as_json':
...             import json
...             result = json.dumps(vars(self))
...         return str(result)
>>>
>>>
>>> point = Point(x=1, y=2)
>>>
>>>
>>> print(f'{point:2d}')
Point(x=1, y=2)
>>>
>>> print(f'{point:3d}')
Point(x=1, y=2, z=0)
>>>
>>> print(f'{point:as_tuple}')
(1, 2, 0)
>>>
>>> print(f'{point:as_dict}')
{'x': 1, 'y': 2, 'z': 0}
>>>
>>> print(f'{point:as_json}')
{"x": 1, "y": 2, "z": 0}


Assignments
-----------
.. literalinclude:: assignments/operators_string_a.py
    :caption: :download:`Solution <assignments/operators_string_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operators_string_b.py
    :caption: :download:`Solution <assignments/operators_string_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operators_string_c.py
    :caption: :download:`Solution <assignments/operators_string_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operators_string_d.py
    :caption: :download:`Solution <assignments/operators_string_d.py>`
    :end-before: # Solution
