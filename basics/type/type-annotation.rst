Type Annotation
===============

.. epigraph::

    Types are not required, and never will be.
    -- Guido van Rossum, Python initiator, core developer, former BDFL

.. epigraph::

    It should be emphasized that Python will remain a dynamically typed language,
    and the authors have no desire to ever make type hints mandatory, even by convention.
    -- Python Software Foundation


Rationale
---------
* Introduced in Python 3.5
* Since Python 3.5: :pep:`484` -- Type Hints
* Since Python 3.6: :pep:`526` -- Syntax for Variable Annotations
* Since Python 3.8: :pep:`544` -- Protocols: Structural subtyping (static duck typing)
* Also known as: "type annotations", "type hints", "gradual typing"
* Good IDE will give you hints
* Types are used extensively in system libraries
* More and more books and documentations use types
* To type check use: ``mypy``, ``pyre-check``, ``pytypes``
* More information in `cicd-tools`
* https://www.infoq.com/presentations/dynamic-static-typing/
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505


Int
---
>>> data: int = 0
>>> data: int = 1
>>> data: int = -1


Float
-----
>>> data: float = 0.0
>>> data: float = 1.23
>>> data: float = -1.23


Str
---
>>> data: str = ''
>>> data: str = 'Jan Twardowski'


Bool
----
>>> data: bool = True
>>> data: bool = False


Union
-----
>>> from typing import Union
>>>
>>> number: Union[int, float] = 1337
>>> number: Union[int, float] = 1.337

Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

>>> number: int|float = 1337        # doctest: +SKIP
>>> number: int|float = 1.337       # doctest: +SKIP
>>> number: int|None = 1337         # doctest: +SKIP
>>> number: int|None = None         # doctest: +SKIP

Result of this expression would then be valid in ``isinstance()`` and ``issubclass()``

>>> isinstance(1337, int|float)     # doctest: +SKIP
>>> isinstance(1337, int|None)      # doctest: +SKIP


Optional
--------
>>> from typing import Optional
>>>
>>> data: Optional[int] = 1337
>>> data: Optional[int] = None

>>> from typing import Optional
>>>
>>> firstname: str = 'Melissa'
>>> lastname: str = 'Lewis'
>>> age: Optional[float] = None

Since Python 3.10: :pep:`645` -- Allow writing optional types as x?

>>> age: int? = 1337                # doctest: +SKIP
>>> age: int? = None                # doctest: +SKIP

Result of this expression would then be valid in ``isinstance()`` and ``issubclass()``

>>> isinstance(1337, int?)          # doctest: +SKIP


Aliases
-------
>>> from typing import Union
>>>
>>> Number = Union[float, int]
>>> age: Number = 10
>>> age: Number = 10.5

Since Python 3.10 :pep:`613` -- TypeAlias Annotation

    PEP 484 introduced the concept of type aliases, only requiring them
    to be top-level unannotated assignments. This simplicity sometimes made
    it difficult for type checkers to distinguish between type aliases and
    ordinary assignments, especially when forward references or invalid types
    were involved. Compare:

>>> Number = 'Cache[str]'  # a type alias                 # doctest: +SKIP
>>> LOG_PREFIX = 'LOG[DEBUG]'  # a module constant          # doctest: +SKIP

    Now the typing module has a special annotation TypeAlias to declare
    type aliases more explicitly:

>>> StrCache: TypeAlias = 'Cache[str]'  # a type alias      # doctest: +SKIP
>>> LOG_PREFIX = 'LOG[DEBUG]'  # a module constant          # doctest: +SKIP

Since Python 3.10:

    >>> from typing import TypeAlias
    >>>
    >>>
    >>> Timestamp: TypeAlias = float

Before Python 3.10:

    >>> Timestamp = float

Final
-----
Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing

>>> from typing import Final
>>>
>>> m: Final[int] = 1
>>> km: Final[int] = 1000 * m

>>> from typing import Final
>>>
>>> second: Final[int] = 1
>>> minute: Final[int] = 60 * second
>>> hour: Final[int] = 60 * minute
>>> day: Final[int] = 24 * hour


Types are not Enforced
----------------------
* This code will run without any problems
* Although ``mypy`` or ``pyre-check`` will throw error

>>> name: int = 'Jan Twardowski'
>>> age: float = 30
>>> is_adult: int = True
