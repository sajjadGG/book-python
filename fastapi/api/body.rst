Body
====


Rationale
---------
* HTTP Request and Response
* POST Method
* Request Body
* Pydantic models


Models
------
* Represents data in your system
* Pydantic class

>>> from typing import Optional
>>> from pydantic import BaseModel
>>>
>>>
>>> class Astronaut(BaseModel):
...     firstname: str
...     lastname: str
...     active: Optional[bool] = True


POST Method
-----------
>>> from typing import Optional
>>> from pydantic import BaseModel
>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> class Astronaut(BaseModel):
...     firstname: str
...     lastname: str
...     active: Optional[bool] = True
>>>
>>>
>>> @app.post('/astronaut/')
... def astronaut_selection(astronaut: Astronaut):
...     return {'data': f'{astronaut.firstname} {astronaut.lastname} is active: {astronaut.active}'}

.. code-block:: console

    $ uvicorn main:app --reload

    $ curl -X POST http://localhost:8000/astronaut/ -d '{"firstname":"Mark", "lastname": "Watney"}'
    {"data":"Mark Watney is active: True"}

Check documentation http://localhost:8000/docs
