FuncProg Callable
=================


Rationale
---------
>>> def hello():
...     return 'Hello World'
>>>
>>>
>>> callable(hello)
True
>>>
>>> type(hello)
<class 'function'>
>>>
>>> hello  # doctest: +ELLIPSIS
<function hello at 0x...>
>>>
>>> hello()
'Hello World'


Calling Call Method
-------------------
* ``__call__()`` method makes object callable

>>> def hello():
...     print('My name... José Jiménez')
>>>
>>>
>>> type(hello)
<class 'function'>
>>>
>>> callable(hello)
True
>>>
>>> hello()
My name... José Jiménez
>>>
>>> hello.__call__()
My name... José Jiménez


Overloading Call Method
-----------------------
>>> data = str('Mark Watney')
>>>
>>> data()
Traceback (most recent call last):
TypeError: 'str' object is not callable
>>>
>>> callable(data)
False

>>> class str(str):
...     def __call__(self):
...         print('Calling str')
>>>
>>>
>>> data = str('Mark Watney')
>>>
>>> data()
Calling str
>>>
>>> callable(data)
True


Callbacks
---------
Callback Design Pattern:

>>> def request(url, on_success, on_error):
...     try:
...         result = f'Downloading from {url}'
...     except Exception as error:
...         on_error(error)
...     else:
...         on_success(result)
>>>
>>>
>>> request(
...     url='https://python.astrotech.io',
...     on_success=lambda result: print(result),
...     on_error=lambda error: print(error))

>>> from http import HTTPStatus
>>> import requests
>>>
>>>
>>> def http_request(url, on_success=lambda: ..., on_error=lambda: ...):
...     result = requests.get(url)
...     if result.status_code == HTTPStatus.OK:
...         return on_success(result)
...     else:
...         return on_error(result)
>>>
>>>
>>> http_request(
...     url='http://python.astrotech.io/',
...     on_success=lambda result: print(result),
...     on_error=lambda error: print(error))
<Response [200]>


Type Annotation
---------------
>>> def add(a: int, b: int) -> int:
...     return a + b
>>>
>>>
>>> total: Callable = add
>>> total: Callable[[int, int], int] = add

>>> from typing import Callable
>>>
>>>
>>> def lower() -> str:
...     return 'hello'
>>>
>>>
>>> def higher() -> Callable:
...     return lower

>>> from typing import Callable
>>>
>>>
>>> def http_request(url: str,
...                  on_success: Callable = lambda: ...,
...                  on_error: Callable = lambda: ...) -> None:
...     ...

>>> from typing import Callable
>>>
>>>
>>> def request(url: str,
...             on_success: Callable[[int,int], int],
...             on_error: Callable) -> callable:
...     ...
>>>
>>> def handle_success(x: int, y: int) -> int:
...     ...
>>>
>>> request('https://...',
...         on_success=handle_success,
...         on_error=lambda: ...)

>>> from typing import Callable, Iterator, Iterable
>>>
>>>
>>> def map(func: Callable, data: Iterable) -> Iterator:
...     ...
>>>
>>> def filter(func: Callable, data: Iterable) -> Iterator:
...     ...


Assignments
-----------
.. literalinclude:: assignments/funcprog_callable_a.py
    :caption: :download:`Solution <assignments/funcprog_callable_a.py>`
    :end-before: # Solution
