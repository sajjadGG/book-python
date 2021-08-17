FuncProg Callable
=================


Rationale
---------
>>> def hello():
...     return 'Hello World'
>>>
>>>
>>> callable(hello)
True
>>>
>>> type(hello)
<class 'function'>
>>>
>>> hello  # doctest: +ELLIPSIS
<function hello at 0x...>
>>>
>>> hello()
'Hello World'


Calling Call Method
-------------------
* ``__call__()`` method makes object callable

.. code-block:: python

    def hello():
        print('My name... José Jiménez')


    type(hello)
    # <class 'function'>

    callable(hello)
    # True

    hello()
    # My name... José Jiménez

    hello.__call__()
    # My name... José Jiménez


Overloading Call Method
-----------------------
.. code-block:: python

    data = str('Mark Watney')

    data()
    # Traceback (most recent call last):
    # TypeError: 'str' object is not callable

    callable(data)
    # False

.. code-block:: python

    class str(str):
        def __call__(self):
            print('Calling str')


    data = str('Mark Watney')

    data()
    # Calling str

    callable(data)
    # True


Callbacks
---------
Callback Design Pattern:

.. code-block:: python

    from http import HTTPStatus
    import requests


    def http_request(url, on_success=lambda: ..., on_error=lambda: ...):
        result = requests.get(url)
        if result.status_code == HTTPStatus.OK:
            return on_success(result)
        else:
            return on_error(result)


    http_request(
        url='http://python.astrotech.io/',
        on_success=lambda result: print(result),
        on_error=lambda error: print(error))

    # <Response [200]>


Type Annotation
---------------
.. code-block:: python

    def add(a: int, b: int) -> int:
        return a + b


    total: Callable = add
    total: Callable[[int, int], int] = add

.. code-block:: python

    from typing import Callable


    def lower() -> str:
        return 'hello'


    def higher() -> Callable:
        return lower

.. code-block:: python

    from typing import Callable


    def http_request(url: str,
                     on_success: Callable = lambda: ...,
                     on_error: Callable = lambda: ...) -> None:
        ...


.. code-block:: python

    from typing import Callable


    def request(url: str,
                on_success: Callable[[int,int], int],
                on_error: Callable) -> callable:
        ...

    def handle_success(x: int, y: int) -> int:
        ...

    request('https://...',
            on_success=handle_success,
            on_error=lambda: ...)


.. code-block:: python

    from typing import Callable, Iterator, Iterable


    def zip(a: Iterable, b: Iterable) -> Iterator:
        ...

    def enumerate(data: Iterable) -> Iterator[int, Any]:
        ...

    def map(func: Callable, data: Iterable) -> Iterator:
        ...

    def filter(func: Callable, data: Iterable) -> Iterator:
        ...


Use Case
--------
.. code-block:: python

    import datetime


    now = datetime.datetime.now

    print(now)
    # <built-in method now of type object at 0x107695638>

    print(now())
    # 1969-07-21 02:56:25

    now()
    # datetime.datetime(1969, 7, 21, 2, 56, 25)

    now.__call__()
    # datetime.datetime(1969, 7, 21, 2, 56, 25)

.. code-block:: python

    import datetime
    from time import sleep


    now = datetime.datetime.now

    print(now())          # 1969-07-21 02:56:15
    sleep(10)
    print(now())          # 1969-07-21 02:56:25


Assignments
-----------
.. literalinclude:: assignments/funcprog_callable_a.py
    :caption: :download:`Solution <assignments/funcprog_callable_a.py>`
    :end-before: # Solution
