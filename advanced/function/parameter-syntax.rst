****************
Parameter Syntax
****************


.. code-block:: python

    def echo(a, b, c=3):
         print(a, b, c)

    echo(1, 2)              # 1 2 3
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required positional argument: 'b'
    echo(1, 2, 3)           # 1 2 3
    echo(1, 2, c=3)         # 1 2 3
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # 1 2 3


Keyword-only parameters
=======================
* All arguments after ``*`` is keyword only

.. code-block:: python

    def echo(a, *, b, c=3):
        print(a, b, c)

    echo(1, 2)              # TypeError: echo() takes 1 positional argument but 2 were given
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required keyword-only argument: 'b'
    echo(1, 2, 3)           # TypeError: echo() takes 1 positional argument but 3 were given
    echo(1, 2, c=3)         # TypeError: echo() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # 1 2 3


Positional-only parameters
==========================
* Since Python 3.8 there will be ``/`` to indicate positional only arguments

.. code-block:: python

    def echo(a, /, b, c=3):
        print(a, b, c)

    echo(1, 2)              # 1 2 3
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required positional argument: 'b'
    echo(1, 2, 3)           # 1 2 3
    echo(1, 2, c=3)         # 1 2 3
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # TypeError: echo() got some positional-only arguments passed as keyword arguments: 'a'


Positional and Keyword parameters
=================================
.. code-block:: python

    def echo(a, /, b, *, c=3):
        print(a, b, c)

    echo(1, 2)              # 1 2 3
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required positional argument: 'b'
    echo(1, 2, 3)           # TypeError: echo() takes 2 positional arguments but 3 were given
    echo(1, 2, c=3)         # 1 2 3
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # TypeError: echo() got some positional-only arguments passed as keyword arguments: 'a'

Example
=======
.. code-block:: python

    def pow(x, y, z=None, /):
        ...

.. code-block:: python

    def quantiles(dist, /, *, n=4, method='exclusive')
        ...

.. code-block:: python

     def add(a, b, /, **kwargs):
        ...

