Type Annotation Function
========================


Rationale
---------
* Before Python 3.9 you need ``from typing import List, Set, Tuple, Dict``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections


Return
------
>>> def say_hello() -> str:
...     return 'My name... José Jiménez'


Parameters
----------
>>> def add_numbers(a: int, b: int) -> int:
...     return a + b


Union
-----
Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

>>> # doctest: +SKIP
... def add_numbers(a: int | float, b: int | float) -> int | float:
...     return a + b

>>> number = int | float
>>>
>>> def add_numbers(a: number, b: number) -> number:
...     return a + b


Optional
--------
Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

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

Since Python 3.11: :pep:`645` -- Allow writing optional types as x?

>>> # doctest: +SKIP
... def find(text: str, what: str) -> int?:
...     position = text.find(what)
...     if position == -1:
...         return None
...     else:
...         return position
...
...
... find('Python', 'x')
... find('Python', 'o')
4


Exception
---------
>>> def stop() -> Exception:
...     raise RuntimeError

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


Literal
-------
* Since Python 3.8: :pep:`586` -- Literal Types

>>> from typing import Literal
>>>
>>>
>>> def open(filename: str, mode: Literal['r','w','a']) -> None:
...     pass
>>>
>>> open('data.csv', mode='w')  # mypy: OK
>>> open('data.csv', mode='r')  # mypy: OK
>>> open('data.csv', mode='a')  # mypy: OK
>>> open('data.csv', mode='x')  # mypy: ERROR


Callable
--------
>>> from typing import Callable
>>>
>>>
>>> def feeder(get_next_item: Callable[[], str]) -> None:
...     pass

>>> from typing import Callable
>>>
>>>
>>> def async_query(on_success: Callable[[int], None],
...                 on_error: Callable[[int, Exception], None]) -> None:
...     pass

Since Python 3.11 :pep:`677` -- Callable Type Syntax

>>> # doctest: +SKIP
... from typing import Awaitable, Callable, Concatenate, ParamSpec, TypeVarTuple
...
... P = ParamSpec("P")
... Ts = TypeVarTuple('Ts')
...
... f0: () -> bool
... f0: Callable[[], bool]
...
... f1: (int, str) -> bool
... f1: Callable[[int, str], bool]
...
... f2: (...) -> bool
... f2: Callable[..., bool]
...
... f3: async (str) -> str
... f3: Callable[[str], Awaitable[str]]
...
... f4: (**P) -> bool
... f4: Callable[P, bool]
...
... f5: (int, **P) -> bool
... f5: Callable[Concatenate[int, P], bool]
...
... f6: (*Ts) -> bool
... f6: Callable[[*Ts], bool]
...
... f7: (int, *Ts, str) -> bool
... f7: Callable[[int, *Ts, str], bool]


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

Since Python 3.11: :pep:`563` -- Postponed Evaluation of Annotations

>>> def add(a: int, b: int) -> int:
...     return a + b
>>>
>>> # doctest: +SKIP
... add.__annotations__
{'a': 'int', 'b': 'int', 'return': 'int'}


Errors
------
* Python will execute without even warning
* Your IDE and ``mypy`` et. al. will yield errors

>>> def add_numbers(a: int, b: int) -> int:
...     return a + b
>>>
>>>
>>> add_numbers('Mark', 'Watney')
'MarkWatney'


Good Engineering Practices
--------------------------
>>> def add_numbers(a: int | float,
...                 b: int | float
...                 ) -> int | float:
...     return a + b
>>>
>>>
>>> add_numbers(1, 2)       # mypy: OK
3
>>> add_numbers(1, 2.5)     # mypy: OK
3.5
>>> add_numbers(1.5, 2.5)   # mypy: OK
4.0


Before Python 3.10
------------------
>>> from typing import Union
>>>
>>>
>>> def add_numbers(a: Union[int,float], b: Union[int,float]) -> Union[int,float]:
...     return a + b

>>> from typing import Optional
>>>
>>>
>>> def find(text: str, what: str) -> Optional[int]:
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


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`
