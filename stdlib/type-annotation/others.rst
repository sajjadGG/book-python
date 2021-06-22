Others
======


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


Type Checking - MyPy
--------------------
* http://mypy-lang.org/
* https://github.com/python/mypy

.. code-block:: console

    $ pip install mypy
    $ mypy FILE

``setup.cfg``

.. code-block:: ini

    [mypy]
    strict_optional = True


Type Checking - PyType
----------------------
* https://github.com/google/pytype

.. code-block:: console

    $ pip install pytype
    $ pytype -V 3.7 FILE


Type Checking - pyre-check
--------------------------


Annotating Existing - PyAnnotate
--------------------------------
* http://mypy-lang.blogspot.com/2017/11/dropbox-releases-pyannotate-auto.html

The -w flag means "go ahead, update the file":

.. code-block:: console

    $ pip install pyannotate
    $ pyannotate -w FILE


Annotating Existing - monkeytype
--------------------------------
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
>>>
>>> T = TypeVar('T', int, float, complex)
>>> Vector = Iterable[tuple[T, T]]
>>>
>>>
>>> def product(data: Vector[T]) -> T:
...     return sum(x*y for x,y in data)
>>>
>>>
>>> def dilate(data: Vector[T], scale: T) -> Vector[T]:
...     return ((x*scale, y*scale) for x,y in data)

