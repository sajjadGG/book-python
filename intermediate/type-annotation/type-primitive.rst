Type Annotation Primitives
==========================
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

.. epigraph::

    Types are not required, and never will be.
    -- Guido van Rossum, Python initiator, core developer, former BDFL

.. epigraph::

    It should be emphasized that Python will remain a dynamically typed
    language, and the authors have no desire to ever make type hints
    mandatory, even by convention.
    -- Python Software Foundation

.. figure:: img/typeannotation-timeline.png

    Timeline of changes to type annotations from Python 3.0 to now [#Briggs2021]_


Int
---
* Used to inform static type checker that the variable should be int

Declaration:

>>> data: int

Example:

>>> data: int
>>>
>>> data = 1        # ok
>>> data = -1       # ok
>>> data = 'hello'  # error

Definition:

>>> data: int = 1
>>> data: int = -1


Float
-----
* Used to inform static type checker that the variable should be float

Declaration:

>>> data: float

Example:

>>> data: float
>>>
>>> data = 1.0        # ok
>>> data = -1.0       # ok
>>> data = 'hello'    # error

Definition:

>>> data: float = 0.0
>>> data: float = 1.23
>>> data: float = -1.23


Str
---
* Used to inform static type checker that the variable should be str

Declaration:

>>> data: str

Example:

>>> data: str
>>>
>>> data = 'Mark'           # ok
>>> data = 'Watney'         # ok
>>> data = 'Mark Watney'    # ok

Definition:

>>> data: str = ''
>>> data: str = 'hello'


Bool
----
* Used to inform static type checker that the variable should be bool

Declaration:

>>> data: bool

Example:

>>> data: bool
>>>
>>> data = True     # ok
>>> data = False    # ok
>>> data = None     # error

Definition:

>>> data: bool = True
>>> data: bool = False


None
----
* Used to inform static type checker that the variable should be None

Declaration:

>>> data: None

Example:

>>> data: None
>>>
>>> data = True     # error
>>> data = False    # error
>>> data = None     # ok

Definition:

>>> data: None = None


Union
-----
* Used to inform static type checker that the variable should either X or Y
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y
* ``int | str == str | int``

Declaration:

>>> data: int | float

Example:

>>> data: int | float
>>>
>>> data = 1337     # ok
>>> data = 1.337    # ok
>>> data = 'hello'  # error

Definition:

>>> data: int | float = 1337
>>> data: int | float = 1.337

Result of this expression would then be valid in ``isinstance()``
and ``issubclass()``:

>>> isinstance(1337, int|float)
True


Optional
--------
* Used to inform static type checker that the variable should be X or None
* ``int | None == None | int``

Declaration:

>>> data: int | None

Example:

>>> number: int | None
>>>
>>> number = 1337    # ok
>>> number = None    # ok
>>> number = 1.0     # error

Definition:

>>> number: int | None = 1337
>>> number: int | None = None

Result of this expression would then be valid in ``isinstance()``
and ``issubclass()``:

>>> isinstance(1337, int|None)
True


Aliases
-------
* Used to make types more readable

Declaration:

>>> data = int | float

Example:

>>> number = int | float
>>>
>>> age: number = 10      # ok
>>> age: number = 10.5    # ok
>>> age: number = None    # error


Final
-----
* Used to inform static type checker the value should not change
* Used to define constants
* Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing

In Python there is not such thing as constants. All values can be changed
during the runtime. However using ``Final`` we can achieve similar effect.
Static type checker will ensure that the value should not change during
the program.

SetUp:

>>> from typing import Final

Declaration:

>>> data: Final
>>> data: Final[int]
>>> data: Final[float]
>>> data: Final[bool]
>>> data: Final[str]

Definition:

>>> pressure: Final[float] = 1013.25    # ok
>>> pressure = 1024.00                  # error


Literal
-------
* Since Python 3.8: :pep:`586` -- Literal Types
* Literal de-duplicates parameters
* Equality comparisons of Literal objects are not order dependent
* https://docs.python.org/3/library/typing.html#typing.Literal

SetUp:

>>> from typing import Literal

Declaration:

>>> data: Literal['one', 'two', 'three']

Problem:

>>> agency: str
>>>
>>> agency = 'NASA'         # ok
>>> agency = 'ESA'          # ok
>>> agency = 'Not existing' # ok

Solution:

>>> agency: Literal['NASA', 'ESA', 'POLSA']
>>>
>>> agency = 'NASA'          # ok
>>> agency = 'ESA'           # ok
>>> agency = 'Not existing'  # error


Errors
------
* Types are not Enforced
* This code will run without any problems
* Types are not required, and never will be
* Although ``mypy``, ``pyre-check`` or ``pytypes`` will throw error

>>> name: int = 'Mark Watney'


Use Case - 0x01
---------------
>>> firstname: str = 'Mark'
>>> lastname: str = 'Watney'
>>> age: int = 40
>>> agency: Literal['NASA', 'ESA', 'POLSA'] = 'NASA'
>>> height: int | float = 185.5
>>> weight: int | float | None = None
>>> is_person: bool = True
>>> is_astronaut: bool | None = True


Use Case - 0x02
---------------
>>> SECOND: Final[int] = 1
>>> MINUTE: Final[int] = 60 * SECOND
>>> HOUR: Final[int] = 60 * MINUTE
>>> DAY: Final[int] = 24 * HOUR


Further Reading
---------------
* More information in `cicd-tools`
* https://www.infoq.com/presentations/dynamic-static-typing/
* https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505


References
----------
.. [#Briggs2021] Briggs, J. Type Annotations in Python. Year: 2021. Retrieved: 2022-04-08. URL: https://towardsdatascience.com/type-annotations-in-python-d90990b172dc
