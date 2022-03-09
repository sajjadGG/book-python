OOP Metaclass
=============


.. epigraph::

    Metaclasses are deeper magic than 99% of users should ever worry about.
    If you wonder whether you need them, you don't.
    The people who actually need them know with certainty that they need
    them, and don't need an explanation about why.

    -- Tim Peters


Rationale
---------
* Object is an instance of a class
* Class is an instance of a Metaclass

.. figure:: img/oop-metaclass-inheritance.png

    Object is an instance of a Class.
    Class is an instance of a Metaclass.
    Metaclass is an instance of a type.
    Type is an instance of a type.


When a class definition is executed, the following steps occur:

    #. MRO entries are resolved;
    #. the appropriate metaclass is determined;
    #. the class namespace is prepared;
    #. the class body is executed;
    #. the class object is created.

When using the default metaclass type, or any metaclass that ultimately calls ``type.__new__``, the following additional customisation steps are invoked after creating the class object:

    #. ``type.__new__`` collects all of the descriptors in the class namespace that define a ``__set_name__()`` method;
    #. all of these ``__set_name__`` methods are called with the class being defined and the assigned name of that particular descriptor;
    #. the ``__init_subclass__()`` hook is called on the immediate parent of the new class in its method resolution order. [#pydocclassobject]_


Syntax
------
>>> class MyMeta(type):
...     pass
>>>
>>> class MyClass(metaclass=MyMeta):
...     pass
>>>
>>> class MySubclass(MyClass):
...     pass
>>>
>>>
>>> myinstance = MySubclass()
>>>
>>>
>>> type(MyMeta)
<class 'type'>
>>>
>>> type(MyClass)
<class 'MyMeta'>
>>>
>>> type(MySubclass)
<class 'MyMeta'>
>>>
>>> type(myinstance)
<class 'MySubclass'>


Metaclasses
-----------
* Is a callable which returns a class
* Instances are created by calling the class
* Classes are created by calling the metaclass (when it executes the ``class`` statement)
* Combined with the normal ``__init__`` and ``__new__`` methods
* Class defines how an object behaves
* Metaclass defines how a class behaves

>>> class MyClass:
...     pass
>>>
>>> class MyClass(object):
...     pass

>>> class MyMeta(type):
...     pass
>>>
>>> class MyClass(metaclass=MyMeta):
...     pass


>>> class MyMeta(type):
...     def __new__(mcs, classname, bases, attrs):
...         return type(classname, bases, attrs)
>>>
>>>
>>> class MyClass(metaclass=MyMeta):
...     pass


Metaclass as a function
-----------------------
* Function are classes

>>> def add(a, b):
...     return a + b
>>>
>>> type(add)
<class 'function'>

>>> def mymeta(classname, bases, attrs):
...     return type(classname, bases, attrs)
>>>
>>>
>>> class MyClass(metaclass=mymeta):
...     pass


Usage
-----
* Metaclasses allow you to do 'extra things' when creating a class
* Allow customization of class instantiation
* Most commonly used as a class-factory
* Registering the new class with some registry
* Replace the class with something else entirely
* Inject logger instance
* Injecting static fields
* Ensure subclass implementation
* Metaclasses run when Python defines class (even if no instance is created)

The potential uses for metaclasses are boundless. Some ideas that have been explored include enum, logging, interface checking, automatic delegation, automatic property creation, proxies, frameworks, and automatic resource locking/synchronization. [#pydocclassobject]_

>>> class MyMeta(type):
...     def __new__(mcs, classname, bases, attrs):
...         print(locals())
...         return type(classname, bases, attrs)
>>>
>>>
>>> class MyClass(metaclass=MyMeta):
...     myattr = 1
...
...     def mymethod(self):
...         pass  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
{'mcs': <class 'MyMeta'>,
 'classname': 'MyClass',
 'bases': (),
 'attrs': {'__module__': 'builtins',
           '__qualname__': 'MyClass',
           'myattr': 1,
           'mymethod': <function MyClass.mymethod at 0x...>}}


Keyword Arguments
-----------------
>>> class MyMeta(type):
...     def __new__(mcs, classname, bases, attrs, myvar):
...         if myvar:
...             ...
...         return type(classname, bases, attrs)
>>>
>>>
>>> class MyClass(metaclass=MyMeta, myvar=True):
...     pass


Methods
-------
* ``__prepare__(metacls, name, bases, **kwargs) -> dict`` - on class namespace initialization
* ``__new__(mcs, classname, bases, attrs) -> cls`` - before class creation
* ``__init__(self, name, bases, attrs) -> None`` - after class creation
* ``__call__(self, *args, **kwargs)`` - allows custom behavior when the class is called

Once the appropriate metaclass has been identified, then the class
namespace is prepared. If the metaclass has a ``__prepare__`` attribute,
it is called as ``namespace = metaclass.__prepare__(name, bases, **kwds)``
(where the additional keyword arguments, if any, come from the class
definition). The ``__prepare__`` method should be implemented as a
``classmethod()``. The namespace returned by ``__prepare__`` is passed in
to ``__new__``, but when the final class object is created the namespace
is copied into a new ``dict``. If the metaclass has no ``__prepare__``
attribute, then the class namespace is initialised as an empty ordered
mapping. [#pydocsprepare]_

>>> from typing import Any
>>>
>>>
>>> class MyMeta(type):
...     @classmethod
...     def __prepare__(metacls, name, bases) -> dict:
...         pass
...
...     def __new__(mcs, classname, bases, attrs) -> Any:
...         pass
...
...     def __init__(self, *args, **kwargs) -> None:
...         pass
...
...     def __call__(self, *args, **kwargs) -> Any:
...         pass


Use Case - Logging
------------------
>>> import logging
>>>
>>>
>>> class Logger(type):
...     def __init__(cls, *args, **kwargs):
...         cls._logger = logging.getLogger(cls.__name__)
>>>
>>>
>>> class Astronaut(metaclass=Logger):
...     pass
>>>
>>>
>>> class Cosmonaut(metaclass=Logger):
...     pass
>>>
>>>
>>>
>>> print(Astronaut._logger)
<Logger Astronaut (DEBUG)>
>>>
>>> print(Cosmonaut._logger)
<Logger Cosmonaut (DEBUG)>


Type Metaclass
--------------
>>> type(1)
<class 'int'>
>>> type(int)
<class 'type'>
>>> type(type)
<class 'type'>

>>> type(float)
<class 'type'>
>>> type(bool)
<class 'type'>
>>> type(str)
<class 'type'>
>>> type(bytes)
<class 'type'>
>>> type(list)
<class 'type'>
>>> type(tuple)
<class 'type'>
>>> type(set)
<class 'type'>
>>> type(frozenset)
<class 'type'>
>>> type(dict)
<class 'type'>

>>> type(object)
<class 'type'>
>>> type(type)
<class 'type'>

.. figure:: img/oop-metaclass-diagram.png

    Object is an instance of a Class.
    Class is an instance of a Metaclass.
    Metaclass is an instance of a type.
    Type is an instance of a type.

>>> class MyClass:
...     pass
>>>
>>>
>>> my = MyClass()
>>>
>>> MyClass.__class__.__bases__
(<class 'object'>,)
>>>
>>> my.__class__.__bases__
(<class 'object'>,)

>>> class MyClass(object):
...     pass
>>>
>>>
>>> my = MyClass()
>>>
>>> MyClass.__class__.__bases__
(<class 'object'>,)
>>>
>>> my.__class__.__bases__
(<class 'object'>,)

>>> class MyMeta(type):
...     pass
>>>
>>> class MyClass(metaclass=MyMeta):
...     pass
>>>
>>>
>>> my = MyClass()
>>>
>>> MyClass.__class__.__bases__
(<class 'type'>,)
>>>
>>> my.__class__.__bases__
(<class 'object'>,)

>>> class MyMeta(type):
...     def __new__(mcs, classname, bases, attrs):
...         return type(classname, bases, attrs)
>>>
>>>
>>> class MyClass(metaclass=MyMeta):
...     pass


Method Resolution Order
-----------------------
>>> class Astronaut:
...     pass
>>>
>>>
>>> astro = Astronaut()
>>>
>>> isinstance(astro, Astronaut)
True
>>>
>>> isinstance(astro, object)
True
>>>
>>> Astronaut.__mro__
(<class 'Astronaut'>, <class 'object'>)

>>> class AstroMeta(type):
...     pass
>>>
>>>
>>> class Astronaut(metaclass=AstroMeta):
...     pass
>>>
>>>
>>> astro = Astronaut()
>>>
>>> isinstance(astro, Astronaut)
True
>>>
>>> isinstance(astro, object)
True
>>>
>>> isinstance(astro, AstroMeta)
False
>>>
>>> isinstance(Astronaut, AstroMeta)
True
>>>
>>> Astronaut.__mro__
(<class 'Astronaut'>, <class 'object'>)


Example
-------
>>> import logging
>>>
>>>
>>> def new(cls):
...     obj = object.__new__(cls)
...     obj._logger = logging.getLogger(cls.__name__)
...     return obj
>>>
>>>
>>> class Astronaut:
...     pass
>>>
>>>
>>> Astronaut.__new__ = new
>>>
>>> mark = Astronaut()
>>> melissa = Astronaut()
>>>
>>> print(mark._logger)
<Logger Astronaut (DEBUG)>
>>>
>>> print(melissa._logger)
<Logger Astronaut (DEBUG)>

>>> import logging
>>>
>>>
>>> def new(cls):
...     obj = object.__new__(cls)
...     obj._logger = logging.getLogger(cls.__name__)
...     return obj
>>>
>>> str.__new__ = new
Traceback (most recent call last):
TypeError: can't set attributes of built-in/extension type 'str'

>>> import logging
>>>
>>>
>>> def new(cls):
...     obj = object.__new__(cls)
...     obj._logger = logging.getLogger(cls.__name__)
...     return obj
>>>
>>> type.__new__ = new
Traceback (most recent call last):
TypeError: can't set attributes of built-in/extension type 'type'


Use Case - Logger
-----------------
Injecting logger instance:

>>> import logging
>>>
>>>
>>> class Logger(type):
...     def __init__(cls, *args, **kwargs):
...         cls._logger = logging.getLogger(cls.__name__)
>>>
>>> class Astronaut(metaclass=Logger):
...     pass
>>>
>>> class Cosmonaut(metaclass=Logger):
...     pass
>>>
>>>
>>> print(Astronaut._logger)
<Logger Astronaut (DEBUG)>
>>>
>>> print(Cosmonaut._logger)
<Logger Cosmonaut (DEBUG)>


Use Case - Abstract Class
-------------------------
Abstract Base Class:

>>> from abc import ABCMeta, abstractmethod
>>>
>>>
>>> class Astronaut(metaclass=ABCMeta):
...     @abstractmethod
...     def say_hello(self):
...         pass
>>>
>>>
>>> astro = Astronaut()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Astronaut with abstract methods say_hello


Use Case - Event Listener
-------------------------
>>> class EventListener(type):
...     listeners: dict[str, list[callable]] = {}
...
...     @classmethod
...     def register(cls, *clsnames):
...         def wrapper(func):
...             for clsname in clsnames:
...                 if clsname not in cls.listeners:
...                     cls.listeners[clsname] = []
...                 cls.listeners[clsname] += [func]
...         return wrapper
...
...     def __new__(mcs, classname, bases, attrs):
...         for listener in mcs.listeners.get(classname, []):
...             listener.__call__(classname, bases, attrs)
...         return type(classname, bases, attrs)
>>>
>>>
>>> @EventListener.register('Astronaut')
... def hello_class(clsname, bases, attrs):
...     print(f'Hello new class {clsname}')
>>>
>>>
>>> @EventListener.register('Astronaut', 'Person')
... def print_name(clsname, bases, attrs):
...     print('New class created')
...     print('Classname:', clsname)
...     print('Bases:', bases)
...     print('Attrs:', attrs)
>>>
>>>
>>> class Person(metaclass=EventListener):
...     pass
New class created
Classname: Person
Bases: ()
Attrs: {'__module__': 'builtins', '__qualname__': 'Person'}
>>>
>>>
>>> class Astronaut(Person, metaclass=EventListener):
...     pass
Hello new class Astronaut
New class created
Classname: Astronaut
Bases: (<class 'Person'>,)
Attrs: {'__module__': 'builtins', '__qualname__': 'Astronaut'}


Use Case - Singleton
--------------------
>>> class Singleton(type):
...     _instances = {}
...     def __call__(cls, *args, **kwargs):
...         if cls not in cls._instances:
...             cls._instances[cls] = super().__call__(*args, **kwargs)
...         return cls._instances[cls]
>>>
>>>
>>> class MyClass(metaclass=Singleton):
...     pass


Use Case - Final
----------------
>>> class Final(type):
...     def __new__(mcs, classname, base, attrs):
...         for cls in base:
...             if isinstance(cls, Final):
...                 raise TypeError(f'{cls.__name__} is final and cannot inherit from it')
...         return type.__new__(mcs, classname, base, attrs)
>>>
>>>
>>> class MyClass(metaclass=Final):
...     pass
>>>
>>> class SomeOtherClass(MyClass):
...    pass
Traceback (most recent call last):
TypeError: MyClass is final and cannot inherit from it


Use Case Django
---------------
Access static fields of a class, before creating instance:

>>> # doctest: +SKIP
... from django.db import models
...
... # class Model(metaclass=...)
... #     ...
...
...
... class Person(models.Model):
...     firstname = models.CharField(max_length=255)
...     lastname = models.CharField(max_length=255)


Metaclass replacements
----------------------
* Effectively accomplish the same thing

Inheritance and ``__init__()`` method:

>>> import logging
>>>
>>>
>>> class Logger:
...     def __init__(self):
...         self._logger = logging.getLogger(self.__class__.__name__)
>>>
>>> class Astronaut(Logger):
...     pass
>>>
>>>
>>> astro = Astronaut()
>>> print(astro._logger)
<Logger Astronaut (DEBUG)>

Inheritance and ``__new__()`` method:

>>> import logging
>>>
>>>
>>> class Logger:
...     def __new__(cls, *args, **kwargs):
...         obj = super().__new__(cls)
...         obj._logger = logging.getLogger(obj.__class__.__name__)
...         return obj
>>>
>>> class Astronaut(Logger):
...     pass
>>>
>>>
>>> astro = Astronaut()
>>> print(astro._logger)
<Logger Astronaut (DEBUG)>

Inheritance for abstract base class validation:

>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class Astronaut(ABC):
...     @abstractmethod
...     def say_hello(self):
...         pass
>>>
>>>
>>> astro = Astronaut()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Astronaut with abstract methods hello

Class Decorator:

>>> import logging
>>>
>>>
>>> def add_logger(cls):
...     class Wrapper(cls):
...         _logger = logging.getLogger(cls.__name__)
...     return Wrapper
>>>
>>>
>>> @add_logger
... class Astronaut:
...     pass
>>>
>>>
>>> print(Astronaut._logger)
<Logger Astronaut (DEBUG)>


References
----------
.. [#pydocsprepare] https://docs.python.org/3/reference/datamodel.html#preparing-the-class-namespace
.. [#pydocclassobject] https://docs.python.org/3/reference/datamodel.html#creating-the-class-object


.. todo:: Assignments
