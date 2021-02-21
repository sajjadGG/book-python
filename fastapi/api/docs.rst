Documentation
=============


Rationale
---------
>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/')
... def index():
...     return {'data': 'blog list'}
>>>
>>>
>>> @app.get('/blog/unpublished')
... def unpublished():
...     return {'data': 'all unpublished blogs'}
>>>
>>>
>>> @app.get('/blog/{id}')
... def show(id: int):
...     return {'data': id}
>>>
>>>
>>> @app.get('/blog/{id}/comments')
... def show(id: int):
...     return {'data': 'comments'}

.. code-block:: console

    $ uvicorn main:app --reload

Open browser to:

    * Swagger: http://localhost:8000/docs
    * ReDoc: http://localhost:8000/recdoc
