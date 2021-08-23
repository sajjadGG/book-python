FuncProg Higher-Order
=====================


Rationale
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
