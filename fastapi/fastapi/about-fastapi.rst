FastAPI About
=============
* `Path`
* `Operation`
* `Path Operation Function`
* `Path Operation Decorator`
* Routing
* Order of `Path Operation Functions` matters
* `Tags` are identifiers used to group routes. Routes with the same tags are grouped into a section on the API documentation.

>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello')
... def hello():
...     return {'message': 'hello'}
>>>
>>>
>>> @app.get('/ehlo')
... def ehlo():
...     return {'message': 'ehlo'}


Operation
---------
* ``app.get()``
* ``app.post()``
* ``app.put()``
* ``app.patch()``
* ``app.delete()``
* ``app.head()``
* ``app.options()``
* ``app.trace()``


Path
----
* ``/`` - URI


Path Operation Decorator
------------------------
* ``@app.get('/')``


Path Operation Function
-----------------------
>>> def hello():
...     return {'message': 'hello world'}


Use Case - 0x01
---------------
>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello')
... def hello_get():
...     return {'message': 'get'}
>>>
>>> @app.post('/hello')
... def hello_post():
...     return {'message': 'post'}
>>>
>>> @app.put('/hello')
... def hello_put():
...     return {'message': 'put'}
>>>
>>> @app.patch('/hello')
... def hello_patch():
...     return {'message': 'patch'}
>>>
>>> @app.delete('/hello')
... def hello_delete():
...     return {'message': 'delete'}
>>>
>>> @app.head('/hello')
... def hello_head():
...     return {'message': 'head'}
>>>
>>> @app.options('/hello')
... def hello_options():
...     return {'message': 'options'}
>>>
>>> @app.trace('/hello')
... def hello_trace():
...     return {'message': 'trace'}
