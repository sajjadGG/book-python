Protocol Descriptor
===================


Rationale
---------
* Add managed attributes to objects
* Outsource functionality into specialized classes
* Descriptors: ``classmethod``, ``staticmethod``, ``property``, functions in general
* ``__del__(self)`` is reserved when object is being deleted by garbage collector (destructor)
* ``__set_name()`` After class creation, Python default metaclass will call it with parent and classname


Protocol
--------
* ``__get__(self, parent, *args) -> self``
* ``__set__(self, parent, value) -> None``
* ``__delete__(self, parent) -> None``
* ``__set_name__(self)``

.. epigraph::

    If any of those methods are defined for an object, it is said to be a descriptor.

    -- Raymond Hettinger


>>> class Descriptor:
...     def __get__(self, parent, *args):
...         return ...
...
...     def __set__(self, parent, value):
...         ...
...
...     def __delete__(self, parent):
...         ...
...
...     def __set_name__(self, parent, classname):
...         ...


Property vs Reflection vs Descriptor
------------------------------------
Property:

>>> class Temperature:
...     kelvin = property()
...     _value: float
...
...     @kelvin.setter
...     def myattribute(self, value):
...         if value < 0:
...             raise ValueError
...         else:
...             self._value = value

Reflection:

>>> class Temperature:
...     kelvin: float
...
...     def __setattr__(self, attrname, value):
...         if attrname == 'kelvin' and value < 0:
...             raise ValueError
...         else:
...             super().__setattr__(attrname, value)

Descriptor:

>>> class Kelvin:
...     def __set__(self, parent, value):
...         if value < 0:
...             raise ValueError
...         else:
...             parent._value = value
>>>
>>>
>>> class Temperature:
...     kelvin = Kelvin()
...     _value: float


Example
-------
>>> class MyField:
...     def __get__(self, parent, *args):
...         print('Getter')
...
...     def __set__(self, parent, value):
...         print('Setter')
...
...     def __delete__(self, parent):
...         print('Deleter')
>>>
>>>
>>> class MyClass:
...     value = MyField()
>>>
>>>
>>> my = MyClass()
>>>
>>> my.value = 'something'
Setter
>>>
>>> my.value
Getter
>>>
>>> del my.value
Deleter


Use Case - 0x01
---------------
* Kelvin Temperature Validator

>>> class KelvinValidator:
...     def __set__(self, parent, value):
...         if value < 0.0:
...             raise ValueError('Cannot set negative Kelvin')
...         parent._value = value
>>>
>>>
>>> class Temperature:
...     kelvin = KelvinValidator()
...
...     def __init__(self):
...         self._value = None
>>>
>>>
>>> t = Temperature()
>>> t.kelvin = -1
Traceback (most recent call last):
ValueError: Cannot set negative Kelvin


Use Case - 0x02
---------------
* Temperature Conversion

>>> class Kelvin:
...     def __get__(self, parent, *args):
...         return round(parent._value, 2)
...
...     def __set__(self, parent, value):
...         parent._value = value
>>>
>>>
>>> class Celsius:
...     def __get__(self, parent, *args):
...         value = parent._value - 273.15
...         return round(value, 2)
...
...     def __set__(self, parent, value):
...         parent._value = value + 273.15
>>>
>>>
>>> class Fahrenheit:
...     def __get__(self, parent, *args):
...         value = (parent._value - 273.15) * 9 / 5 + 32
...         return round(value, 2)
...
...     def __set__(self, parent, fahrenheit):
...         parent._value = (fahrenheit - 32) * 5 / 9 + 273.15
>>>
>>>
>>> class Temperature:
...     kelvin = Kelvin()
...     celsius = Celsius()
...     fahrenheit = Fahrenheit()
...
...     def __init__(self):
...         self._value = 0.0
>>>
>>>
>>> t = Temperature()
>>>
>>> t.kelvin = 273.15
>>> print(t.kelvin)
273.15
>>> print(t.celsius)
0.0
>>> print(t.fahrenheit)
32.0
>>>
>>> t.fahrenheit = 100
>>> print(t.kelvin)
310.93
>>> print(t.celsius)
37.78
>>> print(t.fahrenheit)
100.0
>>>
>>> t.celsius = 100
>>> print(t.kelvin)
373.15
>>> print(t.celsius)
100.0
>>> print(t.fahrenheit)
212.0

Use Case - 0x03
---------------
* Value Range Descriptor

>>> class Value:
...     MIN: int
...     MAX: int
...     name: str
...     value: float
...
...     def __init__(self, min, max):
...         self.MIN = min
...         self.MAX = max
...
...     def __set__(self, instance, value):
...         if self.MIN <= value < self.MAX:
...             self.value = value
...         else:
...             raise ValueError(f'{self.name} ({value}) is not in range({self.MIN}, {self.MAX})')
...
...     def __get__(self, instance, owner):
...         return self.value
...
...     def __delete__(self, instance):
...         raise PermissionError
...
...     def __set_name__(self, owner, name):
...         self.name = name
>>>
>>>
>>> class KelvinTemperature:
...     kelvin = Value(min=0, max=99999)
...     celsius = Value(min=-273.15, max=99999)
>>>
>>>
>>> t = KelvinTemperature()
>>>
>>> t.kelvin = 10
>>> t.kelvin = -1
Traceback (most recent call last):
ValueError: kelvin (-1) is not in range(0, 99999)
>>>
>>> t.celsius = -273
>>> t.celsius = -274
Traceback (most recent call last):
ValueError: celsius (-274) is not in range(-273.15, 99999)
>>>
>>> print(t.kelvin)
10
>>> print(t.celsius)
-273

Note ``__repr__()`` method and how to access Descriptor value.

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class ValueRange:
...     name: str
...     min: float
...     max: float
...     value: float = None
...
...     def __set__(self, parent, value):
...         if value not in range(self.min, self.max):
...             raise ValueError(f'{self.name} is not between {self.min} and {self.max}')
...         self.value = value
>>>
>>>
>>> class Astronaut:
...     name: str
...     age = ValueRange('Age', min=28, max=42)
...     height = ValueRange('Height', min=150, max=200)
...
...     def __init__(self, name, age, height):
...         self.name = name
...         self.height = height
...         self.age = age
...
...     def __repr__(self):
...         name = self.name
...         age = self.age.value
...         height = self.height.value
...         return f'Astronaut({name=}, {age=}, {height=})'
>>>
>>>
>>> Astronaut('Mark Watney', age=38, height=170)
Astronaut(name='Mark Watney', age=38, height=170)
>>>
>>> Astronaut('Melissa Lewis', age=44, height=170)
Traceback (most recent call last):
ValueError: Age is not between 28 and 42
>>>
>>> Astronaut('Rick Martinez', age=38, height=210)
Traceback (most recent call last):
ValueError: Height is not between 150 and 200

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class ValueRange:
...     name: str
...     min: int
...     max: int
...
...     def __set__(self, instance, value):
...         print(f'Setter: {self.name} -> {value}')
>>>
>>>
>>> class Point:
...     x = ValueRange('x', 0, 10)
...     y = ValueRange('y', 0, 10)
...     z = ValueRange('z', 0, 10)
...
...     def __init__(self, x, y, z):
...         self.x = x
...         self.y = y
...         self.z = z
...
...     def __setattr__(self, attrname, value):
...         print(f'Setattr: {attrname} -> {value}')
...         super().__setattr__(attrname, value)
>>>
>>>
>>> p = Point(1,2,3)
Setattr: x -> 1
Setter: x -> 1
Setattr: y -> 2
Setter: y -> 2
Setattr: z -> 3
Setter: z -> 3
>>>
>>> p.notexisting = 1337
Setattr: notexisting -> 1337


Inheritance
-----------
.. code-block:: python

    class Validator:
        attribute_name: str

        def __set_name__(self, parent, attribute_name):
            self.attribute_name = f'_{attribute_name}'

        def __get__(self, parent, parent_type):
            return getattr(parent, self.attribute_name)

        def __delete__(self, parent):
            setattr(parent, self.attribute_name, None)


    class RangeValidator(Validator):
        min: int | float
        max: int | float

        def __init__(self, min: float, max: float):
            self.min = min
            self.max = max

        def __set__(self, parent, newvalue):
            if self.min <= newvalue < self.max:
                setattr(parent, self.attribute_name, newvalue)
            else:
                attr = f'{parent.__class__.__name__}.{self.attribute_name.removeprefix("_")}'
                min = self.min
                max = self.max
                raise ValueError(f'{attr} value: {newvalue} is out of range {min=}, {max=}')


    class Astronaut:
        firstname: str
        lastname: str
        age: int = RangeValidator(min=27, max=50)
        height: float = RangeValidator(min=150, max=200)
        weight: float = RangeValidator(min=50, max=90)
        _firstname: str
        _lastname: str
        _age: int
        _height: float
        _weight: float


    astro = Astronaut()


Use Case - 0x01
---------------
* Timezone Converter Descriptor (pytz)

.. figure:: img/protocol-descriptor-timezone.png

    Comparing datetime works only when all has the same timezone (UTC).
    More information in `Stdlib Datetime Timezone`

Descriptor Timezone Converter:

>>> from dataclasses import dataclass
>>> from datetime import datetime
>>> from pytz import timezone
>>>
>>>
>>> class Timezone:
...     def __init__(self, name):
...         self.timezone = timezone(name)
...
...     def __get__(self, parent, *args):
...         return parent.utc.astimezone(self.timezone)
...
...     def __set__(self, parent, new_datetime):
...         local_time = self.timezone.localize(new_datetime)
...         parent.utc = local_time.astimezone(timezone('UTC'))
>>>
>>>
>>> @dataclass
... class Time:
...     utc = datetime.now(tz=timezone('UTC'))
...     warsaw = Timezone('Europe/Warsaw')
...     moscow = Timezone('Europe/Moscow')
...     eastern = Timezone('America/New_York')
...     pacific = Timezone('America/Los_Angeles')
>>>
>>>
>>> t = Time()
>>>
>>> # Launch of a first man to space
>>> t.moscow = datetime(1961, 4, 12, 9, 6, 59)
>>> print(t.utc)
1961-04-12 06:06:59+00:00
>>> print(t.warsaw)
1961-04-12 07:06:59+01:00
>>> print(t.moscow)
1961-04-12 09:06:59+03:00
>>> print(t.eastern)
1961-04-12 01:06:59-05:00
>>> print(t.pacific)
1961-04-11 22:06:59-08:00
>>>
>>> # First man set foot on a Moon
>>> t.warsaw = datetime(1969, 7, 21, 3, 56, 15)
>>> print(t.utc)
1969-07-21 02:56:15+00:00
>>> print(t.warsaw)
1969-07-21 03:56:15+01:00
>>> print(t.moscow)
1969-07-21 05:56:15+03:00
>>> print(t.eastern)
1969-07-20 22:56:15-04:00
>>> print(t.pacific)
1969-07-20 19:56:15-07:00


Use Case - 0x02
---------------
* Timezone Converter Descriptor (zoneinfo)

.. figure:: img/protocol-descriptor-timezone.png

    Comparing datetime works only when all has the same timezone (UTC).
    More information in `Stdlib Datetime Timezone`

>>> from dataclasses import dataclass
>>> from datetime import datetime
>>> from zoneinfo import ZoneInfo
>>>
>>>
>>> class Timezone:
...     def __init__(self, name):
...         self.timezone = ZoneInfo(name)
...
...     def __get__(self, parent, *args):
...         return parent.utc.astimezone(self.timezone)
...
...     def __set__(self, parent, new_datetime):
...         local_time = new_datetime.replace(tzinfo=self.timezone)
...         parent.utc = local_time.astimezone(ZoneInfo('UTC'))
>>>
>>>
>>> @dataclass
... class Time:
...     utc = datetime.now(tz=ZoneInfo('UTC'))
...     warsaw = Timezone('Europe/Warsaw')
...     moscow = Timezone('Europe/Moscow')
...     eastern = Timezone('America/New_York')
...     pacific = Timezone('America/Los_Angeles')
>>>
>>>
>>> t = Time()
>>>
>>>pacificeasternt.utc = datetime(1961, 4, 12, 6, 7)  # Gagarin's launch to space
>>> print(t.utc)
1961-04-12 06:07:00
>>> print(t.moscow)
1961-04-12 09:07:00+03:00
>>> print(t.warsaw)
1961-04-12 07:07:00+01:00
>>> print(t.eastern)
1961-04-12 01:07:00-05:00
>>> print(t.pacific)
1961-04-11 22:07:00-08:00
>>>
>>>
>>> t.warsaw = datetime(1969, 7, 21, 3, 56, 15)  # Armstrong's first Lunar step
>>> print(t.utc)
1969-07-21 02:56:15+00:00
>>> print(t.warsaw)
1969-07-21 03:56:15+01:00
>>> print(t.moscow)
1969-07-21 05:56:15+03:00
>>> print(t.eastern)
1969-07-20 22:56:15-04:00
>>> print(t.pacific)
1969-07-20 19:56:15-07:00

.. todo:: Check if those times are correct


Function Descriptor
-------------------
>>> def hello():
...     pass
>>>
>>>
>>> type(hello)
<class 'function'>
>>> hasattr(hello, '__get__')
True
>>> hasattr(hello, '__set__')
False
>>> hasattr(hello, '__delete__')
False
>>> hasattr(hello, '__set_name__')
False
>>> dir(hello)  # doctest: +NORMALIZE_WHITESPACE
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__',
 '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__',
 '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__',
 '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

>>> class Astronaut:
...     def hello(self):
...         pass
>>>
>>> type(Astronaut.hello)
<class 'function'>
>>> hasattr(Astronaut.hello, '__get__')
True
>>> hasattr(Astronaut.hello, '__set__')
False
>>> hasattr(Astronaut.hello, '__delete__')
False
>>> hasattr(Astronaut.hello, '__set_name__')
False
>>> dir(Astronaut.hello)  # doctest: +NORMALIZE_WHITESPACE
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__',
 '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__',
 '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__',
 '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

>>> class Astronaut:
...     def hello(self):
...         pass
>>>
>>> astro = Astronaut()
>>>
>>> type(astro.hello)
<class 'method'>
>>> hasattr(astro.hello, '__get__')
True
>>> hasattr(astro.hello, '__set__')
False
>>> hasattr(astro.hello, '__delete__')
False
>>> hasattr(astro.hello, '__set_name__')
False
>>> dir(astro.hello)  # doctest: +NORMALIZE_WHITESPACE
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
 '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


Assignments
-----------
.. literalinclude:: assignments/protocol_descriptor_a.py
    :caption: :download:`Solution <assignments/protocol_descriptor_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_descriptor_b.py
    :caption: :download:`Solution <assignments/protocol_descriptor_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_descriptor_c.py
    :caption: :download:`Solution <assignments/protocol_descriptor_c.py>`
    :end-before: # Solution
