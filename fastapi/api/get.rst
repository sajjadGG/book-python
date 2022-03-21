GET
===


Important
---------
* Resources
* Query Parameters


Resources
---------
* ``'/hello/{name}'`` - Does define resource (required)

>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello/{name}')
... def hello(name: str):
...     return {'data': name}

.. code-block:: console

    $ uvicorn main:app --reload

    $ curl http://localhost:8000/hello/Mark/
    {"data":"Mark"}


Single Parameter
----------------
* ``'/hello/'`` - Does not require a name in URL resource, but requires a parameter

>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello/')
... def hello(name: str):
...     return {'data': name}

.. code-block:: console

    $ uvicorn main:app --reload
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [68005] using watchgod
    INFO:     Started server process [68007]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

    $ curl http://localhost:8000/hello/?name=Mark
    {"data":"Mark"}


Multiple Parameters
-------------------
>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello/')
... def hello(firstname: str, lastname: str):
...     return {'data': f'{firstname} {lastname}'}

.. code-block:: console

    $ uvicorn main:app --reload
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [68005] using watchgod
    INFO:     Started server process [68007]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

    $ curl http://localhost:8000/hello/?firstname=Mark&lastname=Watney
    {"data":"Mark Watney"}


Default Values
--------------
>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello/')
... def hello(firstname: str, lastname: str, age: int = 69):
...     return {'data': f'{firstname} {lastname} is {age} years old'}

.. code-block:: console

    $ uvicorn main:app --reload
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [68005] using watchgod
    INFO:     Started server process [68007]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

    $ curl http://localhost:8000/hello/?firstname=Mark&lastname=Watney
    {"data":"Mark Watney is 69 years old"}

    $ curl http://localhost:8000/hello/?firstname=Mark&lastname=Watney&age=1337
    {"data":"Mark Watney is 1337 years old"}


Optional
--------
>>> from typing import Optional
>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/hello/')
... def hello(firstname: str, lastname: str, age: Optional[int] = None):
...     return {'data': f'{firstname} {lastname} is {age} years old'}


.. code-block:: console

    $ uvicorn main:app --reload
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [68005] using watchgod
    INFO:     Started server process [68007]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

    $ curl http://localhost:8000/hello/?firstname=Mark&lastname=Watney
    {"data":"Mark Watney is None years old"}

    $ curl http://localhost:8000/hello/?firstname=Mark&lastname=Watney&age=69
    {"data":"Mark Watney is 69 years old"}
