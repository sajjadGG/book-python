POST
====


Rationale
---------
* HTTP Request and Response
* POST Method
* Request Body
* Pydantic models


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
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [68005] using watchgod
    INFO:     Started server process [68007]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

    $ curl -X POST http://localhost:8000/astronaut/ -d '{"firstname":"Mark", "lastname": "Watney"}'
    {"data":"Mark Watney is active: True"}

Check documentation http://localhost:8000/docs
