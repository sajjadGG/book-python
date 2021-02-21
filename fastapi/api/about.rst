About
=====


Rationale
---------
* Path
* Operation
* Path Operation Function
* Path Operation Decorator
* Routing

>>> from fastapi import FastAPI
>>>
>>>
>>> api = FastAPI()
>>>
>>> @api.get('/')
... def index():
...     return {'message': 'hello world'}
>>>
>>>
>>> @api.get('/hello/{name}')
... def hello(name: str):
...     return {'hello': name}


Operation
---------
* ``api.get()``
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
* ``@api.get('/')``


Path Operation Function
-----------------------
... def index():
...     return {'message': 'hello world'}
