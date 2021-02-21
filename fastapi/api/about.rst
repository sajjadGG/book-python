About
=====


Rationale
---------
* `Path`
* `Operation`
* `Path Operation Function`
* `Path Operation Decorator`
* Routing
* Order of `Path Operation Functions` matters

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
* get
* post
* put
* delete
* head


Path
----
* ``'/'``


Path Operation Decorator
------------------------
* ``@app.get('/')``


Path Operation Function
-----------------------
>>> def hello():
...     return {'message': 'hello world'}
