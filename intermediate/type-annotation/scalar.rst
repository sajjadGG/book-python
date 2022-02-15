Type Annotation Scalar
======================

.. epigraph::

    Types are not required, and never will be.
    -- Guido van Rossum, Python initiator, core developer, former BDFL

.. epigraph::

    It should be emphasized that Python will remain a dynamically typed
    language, and the authors have no desire to ever make type hints
    mandatory, even by convention.
    -- Python Software Foundation


Rationale
---------
* Also known as: "type annotations", "type hints", "gradual typing"
* Types are not required, and never will be
* Good IDE will give you hints
* Types are used extensively in system libraries
* More and more books and documentations use types
* Introduced in Python 3.5
* Since Python 3.5: :pep:`484` -- Type Hints
* Since Python 3.6: :pep:`526` -- Syntax for Variable Annotations
* Since Python 3.8: :pep:`544` -- Protocols: Structural subtyping (static duck typing)
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y
* To type check use: ``mypy``, ``pyre-check``, ``pytypes``


Int
---
.. highlights::
    * Used to inform static type checker that the variable should be int

>>> data: int = 0
>>> data: int = 1
>>> data: int = -1


Float
-----
* Used to inform static type checker that the variable should be float

>>> data: float = 0.0
>>> data: float = 1.23
>>> data: float = -1.23


Str
---
* Used to inform static type checker that the variable should be str

>>> data: str = ''
>>> data: str = 'Mark Watney'


Bool
----
* Used to inform static type checker that the variable should be bool

>>> data: bool = True
>>> data: bool = False


None
----
* Used to inform static type checker that the variable should be None

>>> data: None = None


Union
-----
* Used to inform static type checker that the variable should either X or Y
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y
* ``int | str == str | int``

>>> data: int | float = 1337
>>> data: int | float = 1.337

Result of this expression would then be valid in ``isinstance()`` and
``issubclass()``:

>>> isinstance(1337, int|float)
True


Optional
--------
* Used to inform static type checker that the variable should be X or None
* ``int | None == None | int``

>>> number: int | None = 1337
>>> number: int | None = None

Result of this expression would then be valid in ``isinstance()`` and
``issubclass()``:

>>> isinstance(1337, int|None)
True


Aliases
-------
* Used to make types more readable

>>> number = int | float
>>>
>>> age: number = 10
>>> age: number = 10.5


Final
-----
* Used to inform static type checker the value should not change
* Used to define constants
* Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing

>>> from typing import Final
>>>
>>>
>>> m: Final[int] = 1
>>> km: Final[int] = 1000 * m

>>> from typing import Final
>>>
>>>
>>> second: Final[int] = 1
>>> minute: Final[int] = 60 * second
>>> hour: Final[int] = 60 * minute
>>> day: Final[int] = 24 * hour


Errors
------
* Types are not Enforced
* This code will run without any problems
* Types are not required, and never will be
* Although ``mypy`` or ``pyre-check`` will throw error

>>> name: int = 'Mark Watney'


Future
------
* Since Python 3.11: :pep:`645` -- Allow writing optional types as x?

>>> age: int? = 1337                # doctest: +SKIP
>>> age: int? = None                # doctest: +SKIP


Use Case - 0x01
---------------
>>> firstname: str = 'Melissa'
>>> lastname: str = 'Lewis'
>>> age: int | None = None


Further Reading
---------------
* More information in `cicd-tools`
* https://www.infoq.com/presentations/dynamic-static-typing/
* https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
