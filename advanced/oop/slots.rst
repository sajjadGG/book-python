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
>>> astro.role = 'Botanist'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'role'

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>>
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>> astro.role = 'Botanist'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'role'


Get Value
---------
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
>>> print(astro.lastname)
Watney


Slots and Methods
-----------------
>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
...
...     def say_hello(self):
...         print(f'My name... {self.firstname} {self.lastname}')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>>
>>> astro.say_hello()
My name... Mark Watney


Slots and Init
--------------
>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> print(astro.firstname)
Mark
>>> print(astro.lastname)
Watney

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
...
...     def __init__(self, firstname, lastname, role):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.role = role
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney', 'Botanist')
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'role'


Get Vars
--------
* Using ``__slots__`` will prevent from creating ``__dict__``

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>>
>>> vars(astro)
Traceback (most recent call last):
TypeError: vars() argument must have __dict__ attribute
>>>
>>> print(astro.__dict__)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '__dict__'

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>>
>>> print(astro.__slots__)
('firstname', 'lastname')
>>>
>>> {x: getattr(astro, x) for x in astro.__slots__}
{'firstname': 'Mark', 'lastname': 'Watney'}

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> vars(Astronaut)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': 'builtins',
              '__slots__': ('firstname', 'lastname'),
              'firstname': <member 'firstname' of 'Astronaut' objects>,
              'lastname': <member 'lastname' of 'Astronaut' objects>,
              '__doc__': None})
>>>
>>> Astronaut.firstname
<member 'firstname' of 'Astronaut' objects>
>>>
>>> type(Astronaut.firstname)
<class 'member_descriptor'>


Slots and Dict
--------------
* Using ``__slots__`` will prevent from creating ``__dict__``
* Adding ``__dict__`` to ``__slots__`` will combine both worlds

>>> class Astronaut:
...     __slots__ = ('__dict__', 'firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'   # will use __slots__
>>> astro.lastname = 'Watney'  # will use __slots__
>>> astro.role = 'Botanist'    # will use __dict__
>>> astro.mission = 'Ares3'    # will use __dict__
>>>
>>> print(astro.__slots__)
('__dict__', 'firstname', 'lastname')
>>>
>>> vars(astro)
{'role': 'Botanist', 'mission': 'Ares3'}
>>>
>>> {x:getattr(astro, x) for x in astro.__slots__ if x != '__dict__'} | vars(astro)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'role': 'Botanist',
 'mission': 'Ares3'}


Inheritance
-----------
* Slots do not inherit, unless they are specified in subclass
* Slots are added on inheritance
* If class does not specify slots, the ``__dict__`` will be added

>>> class Person:
...     __slots__ = ('firstname', 'lastname')
>>>
>>> class Astronaut(Person):
...     pass
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>> astro.role = 'Botanist'
>>>
>>> print(astro.firstname)
Mark
>>> print(astro.lastname)
Watney
>>> print(astro.role)
Botanist
>>>
>>>
>>> vars(astro)
{'role': 'Botanist'}
>>>
>>> vars(Astronaut)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': 'builtins',
              '__dict__': <attribute '__dict__' of 'Astronaut' objects>,
              '__weakref__': <attribute '__weakref__' of 'Astronaut' objects>,
              '__doc__': None})

>>> class Person:
...     __slots__ = ('firstname', 'lastname')
>>>
>>> class Astronaut(Person):
...     __slots__ = ()
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>> astro.role = 'Botanist'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'role'
>>>
>>>
>>> vars(astro)
Traceback (most recent call last):
TypeError: vars() argument must have __dict__ attribute
>>>
>>> vars(Astronaut)
mappingproxy({'__module__': 'builtins', '__slots__': (), '__doc__': None})


>>> class Person:
...     __slots__ = ('firstname', 'lastname')
>>>
>>> class Astronaut(Person):
...     __slots__ = ('role',)
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>> astro.role = 'Botanist'
>>> astro.agency = 'NASA'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'agency'
>>>
>>>
>>> vars(astro)
Traceback (most recent call last):
TypeError: vars() argument must have __dict__ attribute
>>>
>>> vars(Person)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': 'builtins',
              '__slots__': ('firstname', 'lastname'),
              'firstname': <member 'firstname' of 'Person' objects>,
              'lastname': <member 'lastname' of 'Person' objects>,
              '__doc__': None})
>>>
>>> vars(Astronaut)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': 'builtins',
              '__slots__': ('role',),
              'role': <member 'role' of 'Astronaut' objects>,
              '__doc__': None})


Change Slots
------------
>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>>
>>> astro.__slots__
('firstname', 'lastname')
>>>
>>> astro.__slots__ = ('myslot1', 'myslot2')
Traceback (most recent call last):
AttributeError: 'Astronaut' object attribute '__slots__' is read-only

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>>
>>> Astronaut.__slots__ = ('myslot1', 'myslot2')
>>> Astronaut.__slots__
('myslot1', 'myslot2')
>>>
>>> vars(Astronaut)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': 'builtins',
              '__slots__': ('myslot1', 'myslot2'),
              'firstname': <member 'firstname' of 'Astronaut' objects>,
              'lastname': <member 'lastname' of 'Astronaut' objects>,
              '__doc__': None})

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>>
>>> Astronaut.__slots__ = ('myslot1', 'myslot2')
>>> Astronaut.__slots__
('myslot1', 'myslot2')
>>>
>>>
>>> Astronaut.firstname
<member 'firstname' of 'Astronaut' objects>
>>>
>>> Astronaut.lastname
<member 'lastname' of 'Astronaut' objects>
>>>
>>> Astronaut.myslot1
Traceback (most recent call last):
AttributeError: type object 'Astronaut' has no attribute 'myslot1'
>>>
>>> Astronaut.myslot2
Traceback (most recent call last):
AttributeError: type object 'Astronaut' has no attribute 'myslot2'
>>>
>>> astro.firstname
'Mark'
>>>
>>> astro.lastname
'Watney'
>>>
>>> astro.myslot1
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'myslot1'
>>>
>>> astro.myslot2
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'myslot2'


Use Case - 0x01
---------------
* Deep Size
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
>>> # doctest: +SKIP
... if __name__ == 'builtins':
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
DEBUG:deepsizeof:Size: 48, Type: <class 'Astronaut'>, Repr: <Astronaut object at 0x10790b940>
DEBUG:deepsizeof:Size: 53, Type: <class 'str'>, Repr: 'Mark'
DEBUG:deepsizeof:Size: 55, Type: <class 'str'>, Repr: 'Watney'
DEBUG:deepsizeof:Size: 48, Type: <class 'Cosmonaut'>, Repr: <Cosmonaut object at 0x10790b9d0>
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
