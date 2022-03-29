FastAPI GET
===========
* Resources
* Query Parameters


No Parameters
-------------
* Does define resource (required)
* ``/hello``

>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello')
... def hello():
...     return {'data': 'hello'}

.. code-block:: console

    $ curl http://localhost:8000/hello
    {"data":"hello"}


Single Path - One
-----------------
* Does define resource (required)
* ``/hello/{firstname}``

>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello/{firstname}')
... def hello(firstname: str):
...     return {'data': firstname}

.. code-block:: console

    $ curl http://localhost:8000/hello/Mark
    {"data":"Mark"}


Path Parameter - Many
---------------------
* Does define resource (required)
* ``/hello/{firstname}-{lastname}``

>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello/{firstname}-{lastname}')
... def hello(firstname: str, lastname: str):
...     return {'data': f'{firstname} {lastname}'}

.. code-block:: console

    $ curl http://localhost:8000/hello/Mark-Watney
    {"data":"Mark Watney"}


Query Parameter
---------------
* Does not require a name in URL resource, but requires a parameter
* ``/hello``

>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello')
... def hello(firstname: str):
...     return {'data': firstname}

.. code-block:: console

    $ curl http://localhost:8000/hello?firstname=Mark
    {"data":"Mark"}


Multiple Parameters
-------------------
* Does not require a name in URL resource, but requires a parameter
* ``/hello``

>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello')
... def hello(firstname: str, lastname: str):
...     return {'data': f'{firstname} {lastname}'}

.. code-block:: console

    $ curl http://localhost:8000/hello?firstname=Mark&lastname=Watney
    {"data":"Mark Watney"}


Default Values
--------------
>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello')
... def hello(firstname: str, lastname: str, age: int = 40):
...     return {'data': f'{firstname} {lastname} is {age} years old'}

.. code-block:: console

    $ curl http://localhost:8000/hello/?firstname=Mark&lastname=Watney
    {"data":"Mark Watney is 40 years old"}

.. code-block:: console

    $ curl http://localhost:8000/hello/?firstname=Mark&lastname=Watney&age=69
    {"data":"Mark Watney is 69 years old"}


Optional
--------
>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello/')
... def hello(firstname: str, lastname: str, age: int | None = None):
...     return {'data': f'{firstname} {lastname} is {age} years old'}

.. code-block:: console

    $ curl http://localhost:8000/hello/?firstname=Mark&lastname=Watney
    {"data":"Mark Watney is None years old"}

.. code-block:: console

    $ curl http://localhost:8000/hello/?firstname=Mark&lastname=Watney&age=69
    {"data":"Mark Watney is 69 years old"}
