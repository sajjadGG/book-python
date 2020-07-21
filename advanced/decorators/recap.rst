****************
Decorators Recap
****************


Function Decorators with Function Wrappers
==========================================
.. code-block:: python

    def mydeco(func):
        def wrapper(*args, **kwargs):
            ...
        return wrapper

    def mydeco(method):
        def wrapper(*args, **kwargs):
            ...
        return wrapper

    def mydeco(cls):
        def wrapper(*args, **kwargs):
            ...
        return wrapper


Function Decorators with Class Wrappers
=======================================
.. code-block:: python

    def mydeco(func):
        class Wrapper:
            ...
        return Wrapper

    def mydeco(method):
        class Wrapper:
            ...
        return Wrapper

    def mydeco(cls):
        class Wrapper(cls):
            ...
        return Wrapper


Class Decorators
================
.. code-block:: python

    class MyDeco:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args, **kwargs):
            ...

    class MyDeco:
        def __init__(self, method):
            self._method = method

        def __call__(self, *args, **kwargs):
            ...

    class MyDeco:
        def __init__(self, cls):
            self._cls = cls

        def __call__(self, *args, **kwargs):
            ...

