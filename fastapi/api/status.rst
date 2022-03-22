Status
======
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
>>> @app.get('/astronaut/{id}', status_code=status.HTTP_200_OK)
... def details(id: int):
...     return {'data': id}


201 - Created
-------------
>>> from typing import Optional
>>> from pydantic import BaseModel
>>> from fastapi import FastAPI, status
>>> app = FastAPI()
>>>
>>>
>>> class Astronaut(BaseModel):
...     firstname: str
...     lastname: str
...     active: Optional[bool] = True
>>>
>>>
>>> @app.post('/astronaut/', status_code=status.HTTP_201_CREATED)
... def post(astronaut: Astronaut):
...     # Creating Astronaut in database
...     return {'data': astronaut}


202 - Accepted
--------------
>>> from typing import Optional
>>> from pydantic import BaseModel
>>> from fastapi import FastAPI, status
>>> app = FastAPI()
>>>
>>>
>>> class Astronaut(BaseModel):
...     firstname: str
...     lastname: str
...     active: Optional[bool] = True
>>>
>>>
>>> @app.put('/astronaut/{id}', status_code=status.HTTP_202_ACCEPTED)
... def put(id: int, astronaut: Astronaut):
...     # Update Astronaut in database
...     return astronaut


204 - No Content
----------------
>>> from fastapi import FastAPI, status
>>> app = FastAPI()
>>>
>>>
>>> @app.delete('/astronaut/{id}', status_code=status.HTTP_204_NO_CONTENT)
... def delete(id: int):
...     # Delete Astronaut in database
...     return None


404 - Not Found
---------------
>>> from fastapi import FastAPI, status, Response
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/astronaut/{id}', status_code=status.HTTP_200_OK)
... def get(id: int):
...     if id <= 0:
...         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog with that id does not exists')
...     else:
...         return ...
