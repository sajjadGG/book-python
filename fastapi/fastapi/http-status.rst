FastAPI Status
==============
* 200 - OK (GET)
* 201 - Created (POST)
* 202 - Accepted (PUT)
* 204 - No Content (DELETE)
* 404 - Not Found (GET, POST, PUT, DELETE)
* 500 - Internal Server Error


200 - OK
--------
>>> from fastapi import FastAPI, status, Response
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/user', status_code=status.HTTP_200_OK)
... def user_list():
...     users = ['user1', 'user2', 'user3']
...     return {'detail': users}

.. code-block:: console

    $ curl -I -X GET http://localhost:8000/user |head -n1
    HTTP/1.1 200 OK


201 - Created
-------------
>>> from pydantic import BaseModel as Schema
>>> from fastapi import FastAPI, status
>>> app = FastAPI()
>>>
>>>
>>> class User(Schema):
...     firstname: str
...     lastname: str
...     age: int | None = None
>>>
>>>
>>> @app.post('/user', status_code=status.HTTP_201_CREATED)
... def user_post(user: User):
...     # Creating User in database
...     return {'detail': user}

.. code-block:: console

    $ curl -X GET http://localhost:8000/user -d '{"firstname":"Mark", "lastname": "Watney"}'
    {"data":"Mark Watney age: None"}


202 - Accepted
--------------
>>> from pydantic import BaseModel as Schema
>>> from fastapi import FastAPI, status
>>> app = FastAPI()
>>>
>>>
>>> class User(Schema):
...     firstname: str
...     lastname: str
...     active: bool | None = True
>>>
>>>
>>> @app.put('/user/{id}', status_code=status.HTTP_202_ACCEPTED)
... def user_put(id: int, user: User):
...     # Update User in database
...     return user


204 - No Content
----------------
>>> from fastapi import FastAPI, status
>>> app = FastAPI()
>>>
>>>
>>> @app.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT)
... def user_delete(id: int):
...     # Delete User in database
...     return None


404 - Not Found
---------------
>>> from fastapi import FastAPI, status, Response
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/user/{id}', status_code=status.HTTP_200_OK)
... def user_get(id: int):
...     if id <= 0:
...         raise HTTPException(
...             status_code=status.HTTP_404_NOT_FOUND,
...             detail='Blog with that id does not exist')
...     else:
...         return ...

.. code-block:: console

    $ curl -I -X GET http://localhost:8000/user/0 |head -n1
    HTTP/1.1 404 Not Found
