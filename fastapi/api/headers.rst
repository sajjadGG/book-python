API Headers
===========
* Request headers
* Response headers

>>> from typing import Optional
>>> from fastapi import FastAPI, Header
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/')
... async def index(user_agent: Optional[str] = Header(None)):
...     return {'User-Agent': user_agent}


Request
-------
* Request headers will be strings

>>> from fastapi import FastAPI, Request
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/')
... def index(request: Request):
...     ua = request.headers['User-Agent']
...     host = request.headers['Host']
...     accept = request.headers['Accept']
...     return {'message': 'ok'}

.. code-block:: console

    $ curl -D- http://127.0.0.1:8000/
    HTTP/1.1 200 OK
    date: Fri, 05 Mar 2021 11:36:38 GMT
    server: uvicorn
    content-length: 16
    content-type: application/json

    {"message":"ok"}


Response
--------
* Response headers values must be string

>>> from fastapi import FastAPI, Response
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/')
... def index(response: Response):
...     response.headers['X-API-VERSION'] = "1.0"
...     return {'message': 'ok'}

.. code-block:: console

    $ curl -D- http://127.0.0.1:8000/
    HTTP/1.1 200 OK
    date: Fri, 05 Mar 2021 11:16:51 GMT
    server: uvicorn
    content-length: 7
    content-type: application/json
    x-api-version: 1.0

    {"message":"ok"}
