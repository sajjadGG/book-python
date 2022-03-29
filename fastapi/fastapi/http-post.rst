FastAPI POST
============
* HTTP Request and Response
* POST Method
* Request Body
* Pydantic models


Example
-------
>>> from pydantic import BaseModel as Schema
>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> class User(Schema):
...     firstname: str
...     lastname: str
...     age: int | None = None
>>>
>>>
>>> @app.post('/user')
... def user_selection(user: User):
...     return {'data': f'{user.firstname} {user.lastname} age: {user.age}'}

.. code-block:: console

    $ curl -X POST http://127.0.0.1:8000/user -d '{"firstname":"Mark", "lastname": "Watney"}'
    {"data":"Mark Watney age: None"}

Check documentation http://127.0.0.1:8000/docs
