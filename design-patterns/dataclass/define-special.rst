Dataclass Define Special
========================


Literal Field
-------------
>>> from dataclasses import dataclass, field
>>> from typing import Literal
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: Literal['NASA', 'ESA', 'POLSA']


Union Fields
------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int | float


Optional Fields
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: str | None = None


Final Fields
------------
* In Python there is no constants

>>> from dataclasses import dataclass
>>> from typing import Final
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: Final[str]
...     lastname: Final[str]
...     age: int


ClassVar Fields
---------------
* ``from typing import ClassVar``
* Defines static field

One of two places where ``dataclass()`` actually inspects the type of a
field is to determine if a field is a class variable as defined in PEP 526.
It does this by checking if the type of the field is ``typing.ClassVar``.
If a field is a ``ClassVar``, it is excluded from consideration as a field
and is ignored by the dataclass mechanisms. Such ``ClassVar`` pseudo-fields
are not returned by the module-level ``fields()`` function.

>>> from typing import ClassVar

>>> @dataclass
... class Astronaut:
...     fullname: str
...     firstname: str
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50


Keyword Arguments Only
----------------------
* Since Python 3.10
* ``from dataclasses import KW_ONLY``

Any fields after a pseudo-field with the type of KW_ONLY are marked as
keyword-only fields. Note that a pseudo-field of type KW_ONLY is otherwise
completely ignored. This includes the name of such a field. By convention, a
name of _ is used for a KW_ONLY field.

>>> from dataclasses import dataclass, KW_ONLY
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     _: KW_ONLY
...     age: int
...     height: float
...     weight: float


.. todo:: Assignments
