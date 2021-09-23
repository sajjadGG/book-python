FuncProg First-class Functions
==============================


Rationale
---------
* Function can be assigned to variable
* Function can be stored in data structures such as hash tables, lists, ...
* Function can be returned
* Function can be user as a parameter


Assigning Functions
-------------------
* Function can be assigned to variable

>>> def say_hello():
...     return 'hello world'
>>>
>>>
>>> result = say_hello
>>> result()
'hello world'


Storing Functions
-----------------
* Function can be stored in data structures such as hash tables, lists, ...

>>> def square(x):
...     return x ** 2
>>>
>>> def cube(x):
...     return x ** 3
>>>
>>>
>>> operations = (cube, square)

>>> def square(x):
...     return x ** 2
>>>
>>> def cube(x):
...     return x ** 3
>>>
>>>
>>> operations = {
...     'cube': cube,
...     'square': square,
...     'root': lambda x: x ** (1/2)
... }


Returning Functions
-------------------
* Function can be returned

>>> def lower():
...     return 'Hello world'
>>>
>>>
>>> def higher():
...     return lower
>>>
>>>
>>> result = higher()     # <function lower()>
>>> result()              # 'Hello world'
'Hello world'


Parameter Functions
-------------------
* Function can be user as a parameter

>>> def http_request(url, on_success, on_error):
...     try:
...         result = ...
...     except Exception as error:
...         return on_error(error)
...     else:
...         return on_success(result)
>>>
>>>
>>> http_request(
...     url = 'https://python.astrotech.io',
...     on_success = lambda result: print(result),
...     on_error = lambda error: print(error))
Ellipsis

Use Case
--------
>>> def map(func, data):
...     ...

>>> def filter(func, data):
...     ...

>>> def reduce(func, data):
...     ...
