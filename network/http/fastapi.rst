*******
FastAPI
*******


Rationale
=========
* https://fastapi.tiangolo.com


Install
=======
.. code-block:: console

    pip install fastapi uvicorn


Minimal
=======
.. code-block:: python

    from fastapi import FastAPI
    api = FastAPI()


    @api.get('/')
    async def index():
        return {"message": "Hello World"}


Example
=======
.. code-block:: python

    from typing import Optional
    from fastapi import FastAPI
    api = FastAPI()


    @api.get("/")
    async def read_root():
        return {"Hello": "World"}


    @api.get("/items/{item_id}")
    async def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}

User Agent:

.. code-block:: python

    from typing import Optional
    from fastapi import FastAPI, Header
    api = FastAPI()


    @api.get("/")
    async def info(user_agent: Optional[str] = Header(None)):
        return [{"User-Agent": user_agent}]

Pydantic:

.. code-block:: python

    from typing import Optional
    from fastapi import FastAPI
    from pydantic import BaseModel
    api = FastAPI()


    class Item(BaseModel):
        name: str
        price: float
        is_offer: Optional[bool] = None


    @api.get("/")
    def read_root():
        return {"Hello": "World"}


    @api.get("/items/{item_id}")
    def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}


    @api.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}


Run
===
.. code-block:: console

    $ uvicorn main:app --reload
    INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO: Started reloader process [28720]
    INFO: Started server process [28722]
    INFO: Waiting for application startup.
    INFO: Application startup complete.


Usage
=====
*  http://127.0.0.1:8000/items/5?q=somequery

Docs
====
* Swagger http://127.0.0.1:8000/docs
* ReDoc http://127.0.0.1:8000/redoc
