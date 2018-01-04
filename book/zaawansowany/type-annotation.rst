***************
Type Annotation
***************

* https://www.python.org/dev/peps/pep-0484/

PEP 3107 introduced syntax for function annotations, but the semantics were deliberately left undefined. There has now been enough 3rd party usage for static type analysis that the community would benefit from a standard vocabulary and baseline tools within the standard library.

While these annotations are available at runtime through the usual __annotations__ attribute, no type checking happens at runtime . Instead, the proposal assumes the existence of a separate off-line type checker which users can run over their source code voluntarily. Essentially, such a type checker acts as a very powerful linter. (While it would of course be possible for individual users to employ a similar checker at run time for Design By Contract enforcement or JIT optimization, those tools are not yet as mature.)

The type system supports unions, generic types, and a special type named Any which is consistent with (i.e. assignable to and from) all types. This latter feature is taken from the idea of gradual typing. Gradual typing and the full type system are explained in PEP 483.

.. warning:: It should also be emphasized that Python will remain a dynamically typed language, and the authors have no desire to ever make type hints mandatory, even by convention.

Typy proste
-----------

.. code-block:: python

    def sumuj(a: int, b: float) -> float:
        return a + b


    sumuj(1, 2.5)

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

Dict, List, Optional
--------------------

.. code-block:: python

    from typing import Dict, List, Optional

    class Node:
        pass

    class SymbolTable(Dict[str, List[Node]]):
        def push(self, name: str, node: Node) -> None:
            self.setdefault(name, []).append(node)

        def pop(self, name: str) -> Node:
            return self[name].pop()

        def lookup(self, name: str) -> Optional[Node]:
            nodes = self.get(name)
            if nodes:
                return nodes[-1]
            return None


Union types
-----------
Since accepting a small, limited set of expected types for a single argument is common, there is a new special factory called Union . Example:

.. code-block:: python

    from typing import Union

    def handle_employees(e: Union[Employee, Sequence[Employee]]) -> None:
        if isinstance(e, Employee):
            e = [e]
        pass

A type factored by Union[T1, T2, ...] is a supertype of all types T1 , T2 , etc., so that a value that is a member of one of these types is acceptable for an argument annotated by Union[T1, T2, ...] .


The NoReturn type
-----------------

The typing module provides a special type NoReturn to annotate functions that never return normally. For example, a function that unconditionally raises an exception:

.. code-block:: python

    from typing import NoReturn

    def stop() -> NoReturn:
        raise RuntimeError('no way')
