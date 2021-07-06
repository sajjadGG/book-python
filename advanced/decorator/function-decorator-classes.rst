Decorator Function with Cls
===========================


Rationale
---------
* ``mydecorator`` is a decorator name
* ``MyClass`` is a class name

Syntax:

>>> @mydecorator
... class MyClass:
...     ...

Is equivalent to:

>>> MyClass = mydecorator(MyClass)


Syntax
------
* ``mydecorator`` is a decorator name
* ``MyClass`` is a class name

>>> def decorator(cls):
...     class Wrapper(cls):
...         def __new__(cls, *args, **kwargs):
...             ...
...     return Wrapper
>>>
>>>
>>> def decorator(cls):
...     def wrapper(*args, **kwargs):
...         instance = cls.__new__(cls, *args, **kwargs)
...         return instance
...     return wrapper
>>>
>>>
>>> @decorator
... class MyClass:
...     ...
>>>
>>>
>>> my = MyClass()


Example
-------
>>> def run(cls):
...     def wrapper(*args, **kwargs):
...         instance = cls.__new__(cls, *args, **kwargs)
...         return instance
...     return wrapper
>>>
>>>
>>> @run
... class Astronaut:
...     def hello(self, name):
...         return f'My name... {name}'
>>>
>>>
>>> astro = Astronaut()
>>> astro.hello('José Jiménez')
'My name... José Jiménez'


Use Case - Logger
-----------------
>>> import logging
>>>
>>>
>>> def logger(cls):
...     class Wrapper(cls):
...         logger = logging.getLogger(cls.__name__)
...     return Wrapper
>>>
>>>
>>> @logger
... class Astronaut:
...     pass
>>>
>>>
>>> print(Astronaut.logger)
<Logger Astronaut (WARNING)>


Use Case - Since
----------------
>>> from time import time
>>>
>>>
>>> def since(cls):
...     class Wrapper(cls):
...         _instance_created = time()
...     return Wrapper
>>>
>>>
>>> @since
... class Astronaut:
...     pass
>>>
>>>
>>> print(Astronaut._instance_created)
1607187641.3407109


Use Case - Singleton Func
-------------------------
>>> def singleton(cls):
...     def wrapper(*args, **kwargs):
...         if not hasattr(cls, '_instance'):
...             instance = object.__new__(cls, *args, **kwargs)
...             setattr(cls, '_instance', instance)
...         return getattr(cls, '_instance')
...     return wrapper
>>>
>>>
>>> @singleton
... class DatabaseConnection:
...     def connect(self):
...         print(f'Connecting... using {self._instance}')
>>>
>>>
>>> a = DatabaseConnection()  # Creating instance
>>> a.connect()  # doctest: +ELLIPSIS
Connecting... using <__main__.DatabaseConnection object at 0x...>
>>>
>>> b = DatabaseConnection()  # Reusing instance
>>> b.connect()  # doctest: +ELLIPSIS
Connecting... using <__main__.DatabaseConnection object at 0x...>


Use Case - Singleton Cls
------------------------
>>> def singleton(cls):
...     class Wrapper(cls):
...         def __new__(cls, *args, **kwargs):
...             if not hasattr(cls, '_instance'):
...                 instance = object.__new__(cls, *args, **kwargs)
...                 setattr(cls, '_instance', instance)
...             return getattr(cls, '_instance')
...     return Wrapper
>>>
>>>
>>> @singleton
... class DatabaseConnection:
...     def connect(self):
...         print(f'Connecting... using {self._instance}')
>>>
>>>
>>> a = DatabaseConnection()  # Creating instance
>>> a.connect()  # doctest: +ELLIPSIS
Connecting... using <__main__.DatabaseConnection object at 0x...>
>>>
>>> b = DatabaseConnection()  # Reusing instance
>>> b.connect()  # doctest: +ELLIPSIS
Connecting... using <__main__.DatabaseConnection object at 0x...>


Assignments
-----------
.. todo:: Create assignments

