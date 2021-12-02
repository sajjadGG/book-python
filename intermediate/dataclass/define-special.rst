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
...     agency: Literal['NASA', 'ESA', 'Roscosmos']


Union Fields
------------
>>> from dataclasses import dataclass
>>> from typing import Union
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: Union[int,float]

Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass  # doctest: +SKIP
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int | float


Optional Fields
---------------
>>> from dataclasses import dataclass
>>> from typing import Optional
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: Optional[str] = None

Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

>>> from dataclasses import dataclass
>>> from typing import Optional
>>>
>>>
>>> @dataclass  # doctest: +SKIP
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


Assignments
-----------
.. todo:: Create assignments
