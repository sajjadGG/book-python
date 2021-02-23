Schema
======

Rationale
---------
* Schema - also known as Model
* Represents data in your system
* Pydantic class


Example
-------
>>> from typing import Optional
>>> from pydantic import BaseModel
>>>
>>>
>>> class Astronaut(BaseModel):
...     firstname: str
...     lastname: str
...     active: Optional[bool] = True
