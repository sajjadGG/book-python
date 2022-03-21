About
=====


Important
---------
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
* ``app.delete()``
* ``app.head()``


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
