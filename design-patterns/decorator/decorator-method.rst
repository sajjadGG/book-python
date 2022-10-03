Decorator Method
================
* ``MyClass`` is a class containing decorator
* ``mydecorator`` is a decorator name
* ``myfunction`` is a function name
* ``func`` is a reference to function which is being decorated

Definition:

>>> class MyClass:
...     @staticmethod
...     def mydecorator(func):
...         def wrapper(*args, **kwargs):
...             return func(*args, **kwargs)
...         return wrapper

Usage:

>>> @MyClass.mydecorator
... def say_hello():
...     return 'hello'
>>>
>>>
>>> say_hello()
'hello'


Use Case - 0x01
---------------
* FastAPI URL Routing

>>> # doctest: +SKIP
... from fastapi import FastAPI
...
... app = FastAPI()
...
...
... @app.get('/')
... async def index():
...     return {'message': 'Hello World'}
...
...
... @app.get('/user/{pk}')
... async def user(pk: int):
...     return {'pk': pk}
...
...
... @app.get('/search')
... async def items(q: str | None = None):
...     return {'q': q}
