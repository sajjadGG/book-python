Documentation
=============


Rationale
---------
>>> from fastapi import FastAPI
>>>
>>>
>>> api = FastAPI()
>>>
>>>
>>> @api.get('/')
... def index():
...     return {'data': 'blog list'}
>>>
>>>
>>> @api.get('/blog/unpublished')
... def unpublished():
...     return {'data': 'all unpublished blogs'}
>>>
>>>
>>> @api.get('/blog/{id}')
... def show(id: int):
...     return {'data': id}
>>>
>>>
>>> @api.get('/blog/{id}/comments')
... def show(id: int):
...     return {'data': 'comments'}

.. code-block:: console

    $ uvicorn main:api

Open browser to:

    * Swagger: http://localhost:8000/docs
    * ReDoc: http://localhost:8000/recdoc
