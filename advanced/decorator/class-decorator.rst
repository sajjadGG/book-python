Decorator Class
===============


Rationale
---------
* ``MyDecorator`` is a decorator name
* ``myfunction`` is a function name


Syntax
------
* ``cls`` is a reference to class which is being decorated (``MyClass`` in this case)
* ``Wrapper`` is a closure class
* ``Wrapper`` name is a convention, but you can name it anyhow
* ``Wrapper`` can inherit from ``MyClass``
* Decorator must return reference to ``Wrapper``

>>> class MyDecorator:
...     def __init__(self, func):
...         self._func = func
...
...     def __call__(self, *args, **kwargs):
...         return self._func(*args, **kwargs)
>>>
>>>
>>> @MyDecorator
... def myfunction():
...     ...
>>>
>>>
>>> myfunction()


Example
-------
>>> class Run:
...     def __init__(self, func):
...         self._func = func
...
...     def __call__(self, *args, **kwargs):
...         return self._func(*args, **kwargs)
>>>
>>>
>>> @Run
... def hello(name):
...     return f'My name... {name}'
>>>
>>>
>>> hello('José Jiménez')
'My name... José Jiménez'


Use Case - 0x01
---------------
* Login Check

>>> class User:
...     def __init__(self):
...         self.is_authenticated = False
...
...     def login(self, username, password):
...         self.is_authenticated = True
>>>
>>>
>>> class LoginCheck:
...     def __init__(self, func):
...         self._func = func
...
...     def __call__(self, *args, **kwargs):
...         if user.is_authenticated:
...             return self._func(*args, **kwargs)
...         else:
...             print('Permission Denied')
>>>
>>>
>>> @LoginCheck
... def edit_profile():
...     print('Editing profile...')
>>>
>>>
>>> user = User()
>>>
>>> edit_profile()
Permission Denied
>>>
>>> user.login('admin', 'MyVoiceIsMyPassword')
>>> edit_profile()
Editing profile...


Use Case - 0x02
---------------
* Cache Args

>>> class Cache(dict):
...     def __init__(self, func):
...         self._func = func
...
...     def __call__(self, *args):
...         return self[args]
...
...     def __missing__(self, key):
...         self[key] = self._func(*key)
...         return self[key]
>>>
>>>
>>> @Cache
... def myfunction(a, b):
...     return a * b
>>>
>>>
>>> myfunction(2, 4)  # Computed
8
>>> myfunction('hi', 3)  # Computed
'hihihi'
>>> myfunction('ha', 3)  # Computed
'hahaha'
>>>
>>> myfunction('ha', 3)  # Fetched from cache
'hahaha'
>>> myfunction('hi', 3)  # Fetched from cache
'hihihi'
>>> myfunction(2, 4)  # Fetched from cache
8
>>> myfunction(4, 2)  # Computed
8
>>>
>>> myfunction  # doctest: +NORMALIZE_WHITESPACE
{(2, 4): 8,
 ('hi', 3): 'hihihi',
 ('ha', 3): 'hahaha',
 (4, 2): 8}


Use Case - 0x03
---------------
* Cache Kwargs

>>> class Cache(dict):
...     _func: callable
...     _args: tuple
...     _kwargs: dict
...
...     def __init__(self, func):
...         self._func = func
...
...     def __call__(self, *args, **kwargs):
...         self._args = args
...         self._kwargs = kwargs
...         key = hash(args + tuple(kwargs.values()))
...         return self[key]
...
...     def __missing__(self, key):
...         self[key] = self._func(*self._args, **self._kwargs)
...         return self[key]
>>>
>>>
>>> @Cache
... def myfunction(a, b):
...     return a * b
>>>
>>>
>>> myfunction(1, 2)
2
>>> myfunction(2, 1)
2
>>> myfunction(6, 1)
6
>>> myfunction(6, 7)
42
>>> myfunction(9, 7)
63
>>>
>>> myfunction  # doctest: +SKIP
{-3550055125485641917: 2,
 6794810172467074373: 2,
 8062003079928221385: 6,
 1461316589696902609: 42,
 -4120545409808486724: 63}


Assignments
-----------
.. literalinclude:: assignments/decorator_cls_a.py
    :caption: :download:`Solution <assignments/decorator_cls_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_cls_b.py
    :caption: :download:`Solution <assignments/decorator_cls_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_cls_c.py
    :caption: :download:`Solution <assignments/decorator_cls_c.py>`
    :end-before: # Solution
