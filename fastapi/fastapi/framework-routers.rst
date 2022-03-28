FastAPI Routers
===============
* You don't have to worry about performance when including routers.
* This will take microseconds and will only happen at startup.
* So it won't affect performance.


Define Router
-------------
>>> from fastapi import APIRouter
>>>
>>> router = APIRouter()
>>>
>>>
>>> @router.post("/")
... async def update_admin():
...     return {"message": "Admin getting schwifty"}


Include in Main
---------------
>>> from fastapi import Depends, FastAPI
>>> from .dependencies import get_query_token, get_token_header
>>> from .internal import admin
>>> from .routers import items, users
>>>
>>> app = FastAPI(dependencies=[Depends(get_query_token)])
>>>
>>>
>>> app.include_router(users.router)
>>> app.include_router(items.router)
>>> app.include_router(
...     admin.router,
...     prefix="/admin",
...     tags=["admin"],
...     dependencies=[Depends(get_token_header)],
...     responses={418: {"description": "I'm a teapot"}},
... )
>>>
>>>
>>> @app.get("/")
... async def root():
...     return {"message": "Hello Bigger Applications!"}



Include the same router multiple times with different prefix
------------------------------------------------------------
You can also use .include_router() multiple times with the same router using different prefixes.

This could be useful, for example, to expose the same API under different prefixes, e.g. /api/v1 and /api/latest.

This is an advanced usage that you might not really need, but it's there in case you do.
