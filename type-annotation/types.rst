.. _Type Annotation:

***************
Type Annotation
***************


What are Type Annotations?
==========================
* Also known as Type Hinting
* Introduced in Python 3.5 with :pep:`484`
* Accessed by ``__annotations__`` attribute
* No type checking happens at runtime
* Use separate off-line type checker which users can run over their source code voluntarily
* Supports unions, generic types, and a special type named
* ``Any`` is consistent with (i.e. assignable to and from) all types
* This latter feature is taken from the idea of gradual typing.
* Gradual typing and the full type system are explained in :pep:`483`

.. warning:: It should also be emphasized that Python will remain a dynamically typed language, and the authors have no desire to ever make type hints mandatory, even by convention.


Data types
==========
.. code-block:: python

    name: str = 'Jan Twardowski'
    leet: int = 1337
    pi: float = 3.14

.. code-block:: python

    def add(a: int, b: float) -> float:
        return a + b


    add(1, 2.5)


Sequences
=========

List
----
.. code-block:: python

    from typing import List


    my_list: list = ['a', 2, 3.3]

    my_list: List[int] = [1, 2, 3]
    my_list: List[float] = [1.1, 2.2, 3.3]
    my_list: List[str] = ['a', 'b', 'c']

Set
---
.. code-block:: python

    from typing import Set


    my_set: set = {'a', 2, 3.3}

    my_set: Set[int] = {1, 2, 3}
    my_set: Set[float] = {1.1, 2.2, 3.3}
    my_set: Set[str] = {'a', 'b', 'c'}

Tuple
-----
.. code-block:: python

    from typing import Tuple


    my_tuple: tuple = 'a', 2, 3.3
    my_tuple: tuple = ('a', 2, 3.3)

    my_tuple: Tuple[int, int, int] = (1, 2, 3)
    my_tuple: Tuple[float, float, float] = (1.1, 2.2, 3.3)
    my_tuple: Tuple[str, str, str] = ('a', 'b', 'c')

    my_tuple: Tuple[str, int, float] = ('a', 2, 3.3)

Dict
----
.. code-block:: python

    from typing import Dict


    my_dict: dict = {
        'a': 1,
        2: 'b',
        3.3: 'c',
    }

    my_dict: Dict[str, int] = {
        'a': 1,
        'b': 2,
        'c': 3,
    }


Nested sequences
================

List of dict
------------
.. code-block:: python

    list_of_dicts: List[dict] = [
        {'a': 1},
        {2: 'b'},
        {3.3: 'c'}
    ]

    list_of_dicts: List[Dict[str, int]] = [
        {'a': 1},
        {'b': 2},
        {'c': 3},
    ]

List of tuples
--------------
.. code-block:: python

    my_data: List[tuple] = [
        (1, 2, 3),
        (1.1, 2.2, 3.3),
        ('a', 'b', 'c'),
        ('a', 2, 3.3),
    ]

    my_data: List[Tuple[int, int, int]] = [
        (1, 2, 3),
        (1, 2, 3),
        (1, 2, 3),
    ]


Union
=====
.. code-block:: python

    from typing import Union


    def round(number: Union[int, float]) -> int:
        return int(number)

.. code-block:: python

    from typing import Union


    def handle_employees(e: Union[Employee, Sequence[Employee]]) -> None:
        if isinstance(e, Employee):
            e = [e]

.. code-block:: python

    from typing import Union


    AllowedTypes = Union[list, set, tuple]

    def my_print(args: AllowedTypes) -> None:
        if not isinstance(args, AllowedTypes.__args__):
            raise TypeError(f'Collection must be instance of {AllowedTypes.__args__}')

        for element in collection:
            print(element)

Any
===
.. code-block:: python

    from typing import Optional


    def my_print(value: Any) -> None:
        print(value)


Optional
========
.. code-block:: python

    from typing import Optional


    def non_zero(number: int) -> Optional[int]:
        if not number:
            return None
        else:
            return number


The NoReturn type
=================
.. code-block:: python

    from typing import NoReturn


    def stop() -> NoReturn:
        raise RuntimeError


Type aliases
============
.. code-block:: python

    from typing import List, Tuple


    GeographicCoordinate = Tuple[float, float]

    locations: List[GeographicCoordinate] = [
        (25.91375, -60.15503),
        (-11.01983, -166.48477),
        (-11.01983, -166.48477)
    ]


Iterable
========
.. code-block:: python

    from typing import Iterator


    def fib(n: int) -> Iterator[int]:
        a, b = 0, 1
        while a < n:
            yield a
            a, b = b, a + b

Final
=====
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
=======
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
=========
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


TypeVar, Iterable, Tuple
========================
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
========
.. code-block:: python

    from typing import Callable

    def feeder(get_next_item: Callable[[], str]) -> None:
        pass

    def async_query(on_success: Callable[[int], None],
                    on_error: Callable[[int, Exception], None]) -> None:
        pass
