Type Annotation Callable
========================
* Before Python 3.9 you need ``from typing import List, Set, Tuple, Dict``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections


Return
------
>>> def say_hello() -> str:
...     return 'My name... José Jiménez'


Required Parameters
-------------------
>>> def add(a: int, b: int):
...     return a + b


Optional Parameters
-------------------
>>> def add(a: int = 1, b: int = 1):
...     return a + b


Union
-----
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

>>> # doctest: +SKIP
... def add(a: int | float, b: int | float) -> int | float:
...     return a + b


Alias
-----
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

>>> number = int | float
>>>
>>> def add(a: number, b: number) -> number:
...     return a + b


Optional
--------
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

>>> def say_hello(name: str | None) -> str | None:
...     if name is not None:
...         return f'Hello {name}'


Exception
---------
>>> def on_timeout() -> Exception:
...     raise TimeoutError

>>> def on_timeout() -> TimeoutError:
...     raise TimeoutError


Literal
-------
* Since Python 3.8: :pep:`586` -- Literal Types
* Literal de-duplicates parameters
* Equality comparisons of Literal objects are not order dependent
* https://docs.python.org/3/library/typing.html#typing.Literal

>>> from typing import Literal
>>>
>>>
>>> def open(filename: str, mode: Literal['r','w','a']) -> None:
...     pass

Usage:

>>> open('data.csv', mode='w')  # mypy: OK
>>> open('data.csv', mode='r')  # mypy: OK
>>> open('data.csv', mode='a')  # mypy: OK
>>> open('data.csv', mode='x')  # mypy: ERROR


Callable
--------
* Callable type
* ``Callable[[int, int], float]`` is a function of ``(int, int) -> float``
* There is no syntax to indicate optional or keyword arguments
* https://docs.python.org/3/library/typing.html#typing.Callable

>>> from typing import Callable
>>>
>>>
>>> def run(func: Callable[[int, int], float]):
...     ...


Iterator
--------
>>> from typing import Iterator
>>>
>>>
>>> def fib(n: int) -> Iterator[int]:
...     a, b = 0, 1
...     while a < n:
...         yield a
...         a, b = b, a + b


Annotations
-----------
>>> def add(a: int, b: int) -> int:
...     return a + b
>>>
>>>
>>> add.__annotations__
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


Errors
------
* Python will execute without even warning
* Your IDE and ``mypy`` et. al. will yield errors

>>> def add(a: int, b: int) -> int:
...     return a + b
>>>
>>>
>>> add('Mark', 'Watney')
'MarkWatney'


Good Engineering Practices
--------------------------
>>> def add(a: int | float,
...         b: int | float
...         ) -> int | float:
...     return a + b


Future
------
* Since Python 3.11: :pep:`563` -- Postponed Evaluation of Annotations

Postponed Evaluation of Annotations:

>>> def add(a: int, b: int) -> int:
...     return a + b
>>>
>>> # doctest: +SKIP
... add.__annotations__
{'a': 'int', 'b': 'int', 'return': 'int'}


Use Case - 0x01
---------------
>>> def valid_email(email: str) -> str | Exception:
...     if '@' in email:
...         return email
...     else:
...         raise ValueError('Invalid Email')
>>>
>>>
>>> valid_email('mark.watney@nasa.gov')
'mark.watney@nasa.gov'
>>>
>>> valid_email('mark.watney_at_nasa.gov')
Traceback (most recent call last):
ValueError: Invalid Email


Use Case - 0x02
---------------
>>> def find(text: str, what: str) -> int | None:
...     position = text.find(what)
...     if position == -1:
...         return None
...     else:
...         return position
>>>
>>>
>>> find('Python', 'x')
>>> find('Python', 'o')
4

Use Case - 0x03
---------------
>>> def request(url: str,
...             on_success: Callable[[str], None],
...             on_error: Callable[[str, Exception], None],
...             ) -> None:
...     ...


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`
