ContextManager
--------------
* ``contextlib.AbstractContextManager``
* ``contextlib.AbstractAsyncContextManager``


Async
-----
* ``collections.abc.Awaitable``
* ``collections.abc.Coroutine``
* ``collections.abc.AsyncIterable``
* ``collections.abc.AsyncIterator``
* ``collections.abc.AsyncGenerator``


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



Overload
--------
* Since Python 3.8: :pep:`589` -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys
* The ``@overload`` decorator allows describing functions and methods that support multiple different combinations of argument types.
* A series of @overload-decorated definitions must be followed by exactly one non-@overload-decorated definition (for the same function/method)
* The @overload-decorated definitions are for the benefit of the type checker only, since they will be overwritten by the non-@overload-decorated definition

>>> @overload
>>> def process(response: None) -> None:
...     ...
>>>
>>> @overload
>>> def process(response: int) -> tuple[int, str]:
...     ...
>>>
>>> @overload
>>> def process(response: bytes) -> str:
...     ...
>>>
>>> def process(response):
...     <actual implementation>


Type Checking
=============


``MyPy``
--------
* http://mypy-lang.org/
* https://github.com/python/mypy

.. code-block:: console

    $ pip install mypy
    $ mypy FILE

``setup.cfg``

.. code-block:: ini

    [mypy]
    strict_optional = True


``PyType``
----------
* https://github.com/google/pytype

.. code-block:: console

    $ pip install pytype
    $ pytype -V 3.7 FILE


``pyre-check``
--------------

Annotating Existing Code
========================


``PyAnnotate``
--------------
* http://mypy-lang.blogspot.com/2017/11/dropbox-releases-pyannotate-auto.html

The -w flag means "go ahead, update the file":

.. code-block:: console

    $ pip install pyannotate
    $ pyannotate -w FILE


``monkeytype``
--------------
* https://instagram-engineering.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881

.. code-block:: console

    $ pip install monkeytype
    $ monkeytype run runtests.py
    $ monkeytype stub some.module
    $ monkeytype apply some.module


Type Vars
=========
>>> from typing import TypeVar, Iterable, Tuple
>>>
>>> T = TypeVar('T', int, float, complex)
>>> Vector = Iterable[tuple[T, T]]
>>>
>>> def product(v: Vector[T]) -> T:
...     return sum(x*y for x, y in v)
>>>
>>> def dilate(v: Vector[T], scale: T) -> Vector[T]:
...     return ((x * scale, y * scale) for x, y in v)
>>>
>>> vec = []  # type: Vector[float]

