Install
=======


Install
-------
.. code-block:: console

    $ pip install fastapi
    $ pip install 'uvicorn[standard]'


First App
---------
Create file `main.py` with content:

>>> from fastapi import FastAPI
>>>
>>>
>>> api = FastAPI()
>>>
>>> @api.get('/')
... def index():
...     return {'message': 'hello world'}

Run app

.. code-block:: console

    $ uvicorn main:api --reload
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [63402] using statreload
    INFO:     Started server process [63404]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

* ``uvicorn`` - lightning-fast ASGI server implementation, using ``uvloop`` and ``httptools``
* ``main`` - name of the module to run (filename without ``.py`` extension)
* ``api`` - name of the ``FastAPI`` class instance (inside of the ``main.py`` file)
* ``--reload`` - reload webserver each time when ``main.py`` changes

Open browser at ``http://localhost:8000/``


Further Reading
---------------
* https://www.uvicorn.org
