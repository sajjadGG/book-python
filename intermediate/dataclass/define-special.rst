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
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: Final[int] = 30
...     AGE_MAX: Final[int] = 50


KWargs Only
-----------
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
