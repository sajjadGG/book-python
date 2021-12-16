Cookies
=======


Rationale
---------
>>> from fastapi import FastAPI, Cookie
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/')
... def index(ads_id: str | None = Cookie(None)):
...     return {'ads_id': ads_id}


Request
-------
>>> from fastapi import FastAPI, Request
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/')
... def index(request: Request):
...     mycookie = request.headers['MYCOOKIE']
...     return {'message': 'ok'}

.. code-block:: console

    $ curl -D- http://127.0.0.1:8000/ --cookie "MYCOOKIE=myvalue"
    HTTP/1.1 200 OK
    date: Fri, 05 Mar 2021 11:36:38 GMT
    server: uvicorn
    content-length: 16
    content-type: application/json

    {"message":"ok"}


Response
--------
* Response cookies values must be string

>>> from fastapi import FastAPI, Response
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/')
... def index(response: Response):
...     response.set_cookie(key='mycookiename', value='mycookievalue')
...     return {'message': 'ok'}

$ curl -D- http://127.0.0.1:8000/
HTTP/1.1 200 OK
date: Fri, 05 Mar 2021 11:22:46 GMT
server: uvicorn
content-length: 16
content-type: application/json
set-cookie: mycookiename=mycookievalue; Path=/; SameSite=lax

{"message":"ok"}
