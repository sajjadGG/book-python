.. _Type Annotation:

***************
Type Annotation
***************

* https://www.python.org/dev/peps/pep-0484/

PEP 3107 introduced syntax for function annotations, but the semantics were deliberately left undefined. There has now been enough 3rd party usage for static type analysis that the community would benefit from a standard vocabulary and baseline tools within the standard library.

While these annotations are available at runtime through the usual ``__annotations__`` attribute, no type checking happens at runtime . Instead, the proposal assumes the existence of a separate off-line type checker which users can run over their source code voluntarily. Essentially, such a type checker acts as a very powerful linter. (While it would of course be possible for individual users to employ a similar checker at run time for Design By Contract enforcement or JIT optimization, those tools are not yet as mature.)

The type system supports unions, generic types, and a special type named Any which is consistent with (i.e. assignable to and from) all types. This latter feature is taken from the idea of gradual typing. Gradual typing and the full type system are explained in PEP 483.

.. warning:: It should also be emphasized that Python will remain a dynamically typed language, and the authors have no desire to ever make type hints mandatory, even by convention.


Korzystanie z typów
===================

Typy proste
-----------

.. code-block:: python

    def sumuj(a: int, b: float) -> float:
        return a + b


    sumuj(1, 2.5)


Dict, List, Set
---------------
.. code-block:: python

    from typing import Dict, List, Set

    # A dictionary where the keys are strings and the values are ints
    name_counts: Dict[str, int] = {
        "Adam": 10,
        "Guido": 12
    }

    # Set of integers
    my_set: Set[int] = {1, 2, 3}

    # A list of integers
    numbers: List[int] = [1, 2, 3, 4, 5, 6]

    # A list that holds dicts that each hold a string key / int value
    list_of_dicts: List[Dict[str, int]] = [
        {"key1": 1},
        {"key2": 2}
    ]

Tuple
-----
.. code-block:: python

    from typing import Tuple

    my_data: Tuple[str, int, float] = ("Adam", 10, 5.7)

Type aliases
------------
.. code-block:: python

    from typing import List, Tuple

    LatLngVector = List[Tuple[float, float]]

    points: LatLngVector = [
        (25.91375, -60.15503),
        (-11.01983, -166.48477),
        (-11.01983, -166.48477)
    ]


Iterable
--------
.. code-block:: python

    from typing import Iterator

    def fib(n: int) -> Iterator[int]:
        a, b = 0, 1
        while a < n:
            yield a
            a, b = b, a + b

Final
-----
* Since Python 3.8
* :pep:`591`
* https://www.python.org/dev/peps/pep-0591/

.. code-block:: python

    from typing import final

    @final
    class Base:
        ...

    class Derived(Base):  # Error: Cannot inherit from final class "Base"
        ...

.. code-block:: python

    from typing import final

    class Base:
        @final
        def foo(self) -> None:
            ...

    class Derived(Base):
        def foo(self) -> None:  # Error: Cannot override final attribute "foo"
                                # (previously declared in base class "Base")
            ...

.. code-block:: python

    from typing import Any, overload

    class Base:
        @overload
        def method(self) -> None:
            ...

        @overload
        def method(self, arg: int) -> int:
            ...

        @final
        def method(self, x=None):
            ...

.. code-block:: python

    ID: Final[float] = 1

.. code-block:: python

    ID: Final = 1

.. code-block:: python

    from typing import Final

    class Window:
        BORDER_WIDTH: Final = 2.5

    class ListView(Window):
        BORDER_WIDTH = 3  # Error: can't override a final attribute

.. code-block:: python

    class ImmutablePoint:
        x: Final[int]
        y: Final[int]  # Error: final attribute without an initializer

        def __init__(self) -> None:
            self.x = 1  # Good

.. code-block:: python

    from typing import Final

    RATE: Final = 3000

    class Base:
        DEFAULT_ID: Final = 0

    RATE = 300  # Error: can't assign to final attribute
    Base.DEFAULT_ID = 1  # Error: can't override a final attribute

Literal
-------
* Since Python 3.8
* https://www.python.org/dev/peps/pep-0586/

.. code-block:: python

    from typing import Literal

    def accepts_only_four(x: Literal[4]) -> None:
        pass

    accepts_only_four(4)   # OK
    accepts_only_four(19)  # Rejected


.. code-block:: python

    @overload
    def open(path: str,
             mode: Literal["r", "w", "a", "x", "r+", "w+", "a+", "x+"],
             ) -> IO[str]: ...

    @overload
    def open(path: str,
             mode: Literal["rb", "wb", "ab", "xb", "r+b", "w+b", "a+b", "x+b"],
             ) -> IO[bytes]: ...

TypedDict
---------
* Since Python 3.8
* https://www.python.org/dev/peps/pep-0589/

.. code-block:: python

    from typing import TypedDict

    class Movie(TypedDict):
        name: str
        year: int

.. code-block:: python

    movie: Movie = {
        'name': 'Blade Runner',
        'year': 1982
    }

.. code-block:: python

    def record_movie(movie: Movie) -> None:
        ...

    record_movie({'name': 'Blade Runner', 'year': 1982})

.. code-block:: python
    :caption: The code below should be rejected, since 'title' is not a valid key, and the 'name' key is missing

    movie2: Movie = {
        'title': 'Blade Runner',
        'year': 1982
    }

.. code-block:: python

    m = Movie(name='Blade Runner', year=1982)

.. code-block:: python

    class BookBasedMovie(Movie):
        based_on: str

.. code-block:: python

    class X(TypedDict):
        x: int

    class Y(TypedDict):
        y: str

    class XYZ(X, Y):
        z: bool

.. code-block:: python

    m: Movie = dict(
        name='Alien',
        year=1979,
        director='Ridley Scott')  # error: Unexpected key 'director'

Union
-----
.. code-block:: python

    from typing import Union

    def search_for(needle: str, haystack: str) -> Union[int, None]:
        offset = haystack.find(needle)
        if offset == -1:
            return None
        else:
            return offset

Since accepting a small, limited set of expected types for a single argument is common, there is a new special factory called Union . Example:

.. code-block:: python

    from typing import Union

    def handle_employees(e: Union[Employee, Sequence[Employee]]) -> None:
        if isinstance(e, Employee):
            e = [e]
        pass

A type factored by Union[T1, T2, ...] is a supertype of all types T1 , T2 , etc., so that a value that is a member of one of these types is acceptable for an argument annotated by Union[T1, T2, ...] .

.. code-block:: python

    from typing import Union

    AllowedTypes = Union[list, set, tuple]

    def print_elements(collection: AllowedTypes) -> None:
        if not isinstance(collection, AllowedTypes.__args__):
            raise TypeError(f'Collection must be instance of {AllowedTypes.__args__}')

        for element in collection:
            print(element)


Optional
--------
.. code-block:: python

    from typing import Optional

    def search_for(needle: str, haystack: str) -> Optional[int]:
        offset = haystack.find(needle)
        if offset == -1:
            return None
        else:
            return offset


TypeVar, Iterable, Tuple
------------------------

.. code-block:: python

    from typing import TypeVar, Iterable, Tuple

    T = TypeVar('T', int, float, complex)
    Vector = Iterable[Tuple[T, T]]

    def inproduct(v: Vector[T]) -> T:
        return sum(x*y for x, y in v)

    def dilate(v: Vector[T], scale: T) -> Vector[T]:
        return ((x * scale, y * scale) for x, y in v)

    vec = []  # type: Vector[float]

Callable
--------

.. code-block:: python

    from typing import Callable

    def feeder(get_next_item: Callable[[], str]) -> None:
        pass

    def async_query(on_success: Callable[[int], None],
                    on_error: Callable[[int, Exception], None]) -> None:
        pass


The NoReturn type
-----------------
The typing module provides a special type NoReturn to annotate functions that never return normally. For example, a function that unconditionally raises an exception:

.. code-block:: python

    from typing import NoReturn

    def stop() -> NoReturn:
        raise RuntimeError('no way')

Introspekcja
============
.. code-block:: python

    def annotated(x: int, y: str) -> bool:
        return x < y

    print(annotated.__annotations__)
    # {'y': <class 'str'>, 'return': <class 'bool'>, 'x': <class 'int'>}


Sprawdzanie typów
=================

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


Dodawanie typów do istniejącego kodu
====================================

``PyAnnotate``
--------------
* http://mypy-lang.blogspot.com/2017/11/dropbox-releases-pyannotate-auto.html

.. code-block:: console

    $ pip install pyannotate

    # (the -w flag means “go ahead, update the file”)
    $ pyannotate -w FILE

``monkeytype``
--------------
* https://instagram-engineering.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881

.. code-block:: console

    $ pip install monkeytype
    $ monkeytype run runtests.py
    $ monkeytype stub some.module
    $ monkeytype apply some.module

