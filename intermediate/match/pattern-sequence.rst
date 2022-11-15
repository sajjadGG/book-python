Match Pattern Sequence
======================

A `sequence pattern` looks like ``[a, *rest, b]`` and is similar to a
list unpacking. An important difference is that the elements nested
within it can be any kind of patterns, not just names or sequences. It
matches only sequences of appropriate length, as long as all the
sub-patterns also match. It makes all the bindings of its sub-patterns.


Use Case - 0x03
---------------
* HTTP Request

.. testsetup::

    >>> def handle_get(uri): ...
    >>> def handle_post(uri): ...
    >>> def handle_put(uri): ...
    >>> def handle_delete(uri): ...

>>> request = 'GET /index.html HTTP/2.0'
>>>
>>> match request.split():
...     case ['GET', path, version]:     handle_get(path)
...     case ['POST', path, version]:    handle_post(path)
...     case ['PUT', path, version]:     handle_put(path)
...     case ['DELETE', path, version]:  handle_delete(path)
