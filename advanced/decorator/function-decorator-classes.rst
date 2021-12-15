Decorator Function with Cls
===========================


Rationale
---------
* ``mydecorator`` is a decorator name
* ``MyClass`` is a class name

Syntax:

>>> @mydecorator  # doctest: +SKIP
... class MyClass:
...     ...

Is equivalent to:

>>> MyClass = mydecorator(MyClass)  # doctest: +SKIP


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


Use Case - 0x01
---------------
* Logger

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


Use Case - 0x02
---------------
* Since

>>> from datetime import datetime
>>>
>>>
>>> def since(cls):
...     class Wrapper(cls):
...         _instance_created = datetime.now()
...     return Wrapper
>>>
>>>
>>> @since
... class Astronaut:
...     pass
>>>
>>>
>>> print(Astronaut._instance_created)  #   # doctest: +SKIP
datetime.datetime(1969, 7, 21, 2, 56, 15)


Use Case - 0x03
---------------
* Singleton Func

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
...         print(f'Connecting...')
>>>
>>>
>>> a = DatabaseConnection()  # Will create instance
>>> a.connect()  # doctest: +ELLIPSIS
Connecting...
>>>
>>> b = DatabaseConnection()  # Will reuse instance
>>> b.connect()  # doctest: +ELLIPSIS
Connecting...


Use Case - 0x04
---------------
* Singleton Cls

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
...         print(f'Connecting...')
>>>
>>>
>>> a = DatabaseConnection()  # Will create instance
>>> a.connect()  # doctest: +ELLIPSIS
Connecting...
>>>
>>> b = DatabaseConnection()  # Will reuse instance
>>> b.connect()  # doctest: +ELLIPSIS
Connecting...


Assignments
-----------
.. todo:: Create assignments

