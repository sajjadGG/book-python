API Documentation
=================
* Generate Documentation
* What is OpenAPI?
* Swagger vs Redoc


Example
-------
>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/')
... def index():
...     return {'data': 'list all astronauts'}
>>>
>>>
>>> @app.get('/astronauts/active')
... def active():
...     return {'data': 'list all active astronauts'}
>>>
>>>
>>> @app.get('/astronaut/{id}')
... def show_by_id(id: int):
...     return {'data': id}
>>>
>>>
>>> @app.get('/astronaut/{firstname}-{lastname}')
... def show_by_name(firstname: str, lastname: str):
...     return {'data': f'{firstname} {lastname}'}
>>>
>>>
>>> @app.get('/astronaut/{id}/friends')
... def show_friends(id: int):
...     return {'data': 'comments'}

.. code-block:: console

    $ uvicorn main:app --reload
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [68005] using watchgod
    INFO:     Started server process [68007]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

Open browser to:

    * Swagger: http://localhost:8000/docs
    * ReDoc: http://localhost:8000/recdoc
