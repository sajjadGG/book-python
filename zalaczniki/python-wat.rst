************
Python WAT?!
************

.. code-block:: python

    >>> 999 + 1 is 1000
    False

    >>> 1000 is 1000
    True

    >>> 1 + 1 is 2
    True

    >>> 2.2 * 3.0 == 3.3 * 2.0
    False

.. code-block:: python

    >>> a = ('hello', 'word')
    >>> a = ('hello')
    >>> for x in a:
    ...    print(x)
    h
    e
    l
    l
    o

    >>> a = ('hello', 'word')
    >>> a = ('hello',)
    >>> for x in a:
    ...    print(x)
    hello


    >>> a = 'hello', 'word'
    >>> a = 'hello'
    >>> for x in a:
    ...    print(x)
    h
    e
    l
    l
    o

    >>> a = 'hello', 'word'
    >>> a = 'hello',
    >>> for x in a:
    ...    print(x)
    hello
