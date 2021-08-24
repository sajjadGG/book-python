OOP Slots
=========


Rationale
---------
* Faster attribute access
* Space savings in memory (overhead of dict for every object)
* Prevents from adding new attributes
* The space savings is from:
* Store value references in slots instead of ``__dict__``
* Denying ``__dict__`` and ``__weakref__`` creation if parent classes deny them and you declare ``__slots__``

Example
-------
>>> class Astronaut:
...     __slots__ = ()
>>>
>>>
>>> astro = Astronaut()
>>>
>>> astro.fullname = 'Mark Watney'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'fullname'

>>> class Astronaut:
...     __slots__ = ('fullname',)
>>>
>>>
>>> astro = Astronaut()
>>>
>>> astro.fullname = 'Mark Watney'
>>> astro.mission = 'Ares3'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'mission'

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>>
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>> astro.mission = 'Ares3'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'mission'


``__slots__`` and ``__dict__``
------------------------------
* Using ``__slots__`` will prevent from creating ``__dict__``

>>> class Astronaut:
...     __slots__ = ('fullname',)
>>>
>>>
>>> astro = Astronaut()
>>> astro.fullname = 'Mark Watney'
>>>
>>> print(astro.__slots__)
('fullname',)
>>>
>>> print(astro.__dict__)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '__dict__'

>>> class Astronaut:
...     __slots__ = ('__dict__', 'fullname')
>>>
>>>
>>> astro = Astronaut()
>>> astro.fullname = 'Mark Watney'   # will use __slots__
>>> astro.mission = 'Ares3'          # will use __dict__
>>>
>>> print(astro.__slots__)
('__dict__', 'fullname')
>>>
>>> print(astro.__dict__)
{'mission': 'Ares3'}


Slots and Methods
-----------------
>>> class Astronaut:
...     __slots__ = ('fullname',)
...
...     def say_hello(self):
...         print(f'My name... {self.fullname}')
>>>
>>>
>>> astro = Astronaut()
>>> astro.fullname = 'Mark Watney'
>>> astro.say_hello()
My name... Mark Watney


Slots and Init
--------------
>>> class Astronaut:
...     __slots__ = ('fullname',)
...
...     def __init__(self, fullname)
...         self.fullname = fullname
>>>
>>>
>>> astro = Astronaut('Mark Watney')
>>> print(astro.fullname)
Mark Watney

>>> class Astronaut:
...     __slots__ = ('fullname',)
...
...     def __init__(self, fullname, mission):
...         self.fullname = fullname
...         self.mission = mission
>>>
>>>
>>> astro = Astronaut('Mark Watney', 'Ares 3')
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'mission'


Inheritance
-----------
* Slots do not inherit, unless they are specified in subclass
* Slots are added on inheritance
* If class does not specify slots, the ``__dict__`` will be added

>>> class Person:
...     __slots__ = ('fullname',)
>>>
>>> class Astronaut(Person):
...     pass
>>>
>>>
>>> astro = Astronaut()
>>> astro.fullname = 'Mark Watney'
>>> astro.mission = 'Ares3'
>>>
>>> print(astro.mission)
Ares3

>>> class Person:
...     __slots__ = ('fullname',)
>>>
>>> class Astronaut(Person):
...     __slots__ = ('fullname', 'mission')
>>>
>>>
>>> astro = Astronaut()
>>> astro.fullname = 'Mark Watney'
>>> astro.mission = 'Ares3'
>>> astro.agency = 'NASA'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'agency'

>>> class Person:
...     __slots__ = ('fullname',)
>>>
>>> class Astronaut(Person):
...     __slots__ = ('mission',)
>>>
>>>
>>> astro = Astronaut()
>>> astro.fullname = 'Mark Watney'
>>> astro.mission = 'Ares 3'
>>> astro.agency = 'NASA'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'agency'


Use Case - Getattr
------------------
>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>>
>>> print(astro.firstname)
Mark
>>>
>>> print(astro.lastname)
Watney
>>>
>>> print(astro.__slots__)
('firstname', 'lastname')
>>>
>>> print(astro.__dict__)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '__dict__'
>>>
>>> result = {attr: getattr(astro, attr)
>>>           for attr in astro.__slots__}
>>>
>>> print(result)
{'firstname': 'Mark', 'lastname': 'Watney'}


Use Case - Deep Size
--------------------
* Source: https://code.activestate.com/recipes/577504/

>>> from sys import getsizeof
>>> from itertools import chain
>>> from collections import deque
>>> import logging
>>>
>>>
>>> logging.basicConfig(level='DEBUG')
>>> log = logging.getLogger('deepsizeof')
>>>
>>>
>>> def deepsizeof(o, handlers={}):
...     """
...     Returns the approximate memory footprint an object and all of its contents.
...
...     Automatically finds the contents of the following builtin containers and
...     their subclasses: tuple, list, deque, dict, set and frozenset
...     """
...     dict_handler = lambda d: chain.from_iterable(d.items())
...     all_handlers = {tuple: iter,
...                     list: iter,
...                     deque: iter,
...                     dict: dict_handler,
...                     set: iter,
...                     frozenset: iter}
...     all_handlers.update(handlers)     # user handlers take precedence
...     seen = set()                      # track which object id's have already been seen
...     default_size = getsizeof(0)       # estimate sizeof object without __sizeof__
...
...     def sizeof(o):
...         if id(o) in seen:       # do not double count the same object
...             return 0
...         seen.add(id(o))
...         s = getsizeof(o, default_size)
...
...         log.debug('Size: %s, Type: %s, Repr: %s', s, type(o), repr(o))
...
...         for typ, handler in all_handlers.items():
...             if isinstance(o, typ):
...                 s += sum(map(sizeof, handler(o)))
...                 break
...         else:
...             if not hasattr(o.__class__, '__slots__'):
...                 if hasattr(o, '__dict__'):
...                     # no __slots__ *usually* means a
...                     # __dict__, but some special builtin classes (such
...                     # as `type(None)`) have neither
...                     # else, `o` has no attributes at all, so sys.getsizeof()
...                     # actually returned the correct value
...                     s += sizeof(o.__dict__)
...             else:
...                 s += sum(
...                     sizeof(getattr(o, x))
...                            for x in o.__class__.__slots__
...                            if hasattr(o, x))
...         return s
...     return sizeof(o)
>>>
>>>
>>> if __name__ == '__main__':
...     class Astronaut:
...        __slots__ = ('firstname', 'lastname')
...
...     class Cosmonaut:
...         pass
...
...     a = Astronaut()
...     a.firstname = 'Mark'
...     a.lastname = 'Watney'
...
...     c = Cosmonaut()
...     c.firstname = 'Mark'
...     c.lastname = 'Watney'
...
...     print('Astronaut', deepsizeof(a))
...     print('Cosmonaut', deepsizeof(c))
DEBUG:deepsizeof:Size: 48, Type: <class '__main__.Astronaut'>, Repr: <__main__.Astronaut object at 0x10790b940>
DEBUG:deepsizeof:Size: 53, Type: <class 'str'>, Repr: 'Mark'
DEBUG:deepsizeof:Size: 55, Type: <class 'str'>, Repr: 'Watney'
DEBUG:deepsizeof:Size: 48, Type: <class '__main__.Cosmonaut'>, Repr: <__main__.Cosmonaut object at 0x10790b9d0>
DEBUG:deepsizeof:Size: 104, Type: <class 'dict'>, Repr: {'firstname': 'Mark', 'lastname': 'Watney'}
DEBUG:deepsizeof:Size: 58, Type: <class 'str'>, Repr: 'firstname'
DEBUG:deepsizeof:Size: 53, Type: <class 'str'>, Repr: 'Mark'
DEBUG:deepsizeof:Size: 57, Type: <class 'str'>, Repr: 'lastname'
DEBUG:deepsizeof:Size: 55, Type: <class 'str'>, Repr: 'Watney'
Astronaut 156
Cosmonaut 375


Assignments
-----------
.. literalinclude:: assignments/oop_slots_define.py
    :caption: :download:`Solution <assignments/oop_slots_define.py>`
    :end-before: # Solution
