.. _Intermediate Type Annotation Types:

***************
Type Annotation
***************


What are Type Annotations?
==========================
.. versionadded:: Python 3.5
    See :pep:`484`

* Also known as Type Hinting
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



Final
=====
.. versionadded:: Python 3.8
    See :pep:`591`

.. code-block:: python

    from typing import final

    @final
    class Base:
        ...

    class Derived(Base):  # Error: Cannot inherit from final class "Base"
        ...

.. code-block:: python

    from typing import Final


    ID: Final = 1
    ID: Final[float] = 1

.. code-block:: python

    from typing import Final

    class Window:
        BORDER_WIDTH: Final = 2.5

    class ListView(Window):
        BORDER_WIDTH = 3  # Error: can't override a final attribute

.. code-block:: python

    from typing import Final

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


New Features
============
.. versionadded:: Python 3.9
    :pep:`585` Builtin Generic Types

In type annotations you can now use built-in collection types such as list and dict as generic types instead of importing the corresponding capitalized types (e.g. List or Dict) from typing. Some other types in the standard library are also now generic, for example queue.Queue.

.. code-block:: python

    def greet_all(names: list[str]) -> None:
        for name in names:
            print("Hello", name)
