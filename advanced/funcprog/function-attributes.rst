FuncProg Function Attributes
============================


Rationale
---------
>>> def hello():
...     return 'Hello World'
>>>
>>>
>>> type(hello)
<class 'function'>


Function Annotations
--------------------
>>> def add(a: int, b: int) -> int:
...     return a + b
>>>
>>>
>>> add.__annotations__
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


Setattr, Getattr
----------------
>>> def hello():
...     pass
>>>
>>>
>>> hello.firstname = 'Mark'
>>> hello.lastname = 'Watney'
>>>
>>> print(f'Hello {hello.firstname} {hello.lastname}')
Hello Mark Watney

>>> def hello():
...     return f'Hello {hello.firstname} {hello.lastname}'
>>>
>>>
>>> hello.firstname = 'Mark'
>>> hello.lastname = 'Watney'
>>>
>>> hello()
'Hello Mark Watney'


Function Code
-------------
>>> def add(a, b):
...     return a + b
>>>
>>>
>>> add.__code__.co_varnames
('a', 'b')
>>>
>>> dir(add.__code__)  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
[...,
 'co_argcount',
 'co_cellvars',
 'co_code',
 'co_consts',
 'co_filename',
 'co_firstlineno',
 'co_flags',
 'co_freevars',
 'co_kwonlyargcount',
 'co_lnotab',
 'co_name',
 'co_names',
 'co_nlocals',
 'co_posonlyargcount',
 'co_stacksize',
 'co_varnames',
 'replace']


Use Case 1
----------
>>> def hello():
...     if not hello.disabled:
...         print('My name... José Jiménez')
...     else:
...         raise PermissionError
>>>
>>>
>>> hello.disabled = False
>>> hello()
My name... José Jiménez
>>>
>>> hello.disabled = True
>>> hello()
Traceback (most recent call last):
PermissionError

Use Case 2
----------
>>> def add(a, b):
...     return a + b
>>>
>>>
>>> add(1, 2)
3
>>> add(1, 2)
3
>>> add(1, 2)
3

>>> def add(a, b):
...     if not hasattr(add, '_cache'):
...         setattr(add, '_cache', {})
...     if (a,b) in add._cache:
...         print('Found in cache; fetching...')
...         return add._cache[a,b]
...     else:
...         print('Not in cache; computing and updating cache...')
...         add._cache[a,b] = result = a + b
...         return result
>>>
>>>
>>> add(1, 2)
Not in cache; computing and updating cache...
3
>>> add(1, 2)
Found in cache; fetching...
3
>>> add(1, 2)
Found in cache; fetching...
3
