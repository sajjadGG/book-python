FuncProg Higher-Order
=====================


Important
---------
* Function can take other function as arguments
* Function can return function


Example
-------
>>> def lower():
...     ...
>>>
>>>
>>> def higher():
...     return lower


Calling
-------
>>> def lower():
...     return 'My name... José Jiménez'
>>>
>>> def higher():
...     return lower
>>>
>>>
>>> a = higher
>>> b = higher()
>>>
>>> a  # doctest: +ELLIPSIS
<function higher at 0x...>
>>>
>>> a()  # doctest: +ELLIPSIS
<function lower at 0x...>
>>>
>>> a()()
'My name... José Jiménez'
>>>
>>> b  # doctest: +ELLIPSIS
<function lower at 0x...>
>>>
>>> b()
'My name... José Jiménez'


Use Case
--------
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
