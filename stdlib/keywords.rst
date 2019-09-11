********
Keywords
********


``pass``
========
* Avoid error when you don't specify the body of a block

.. code-block:: python
    :caption: Exceptions has all the content needed inherited from ``Exception`` class. You need something to avoid ``IndentationError``

    class MyError(Exception):


    print('hello')
    # IndentationError: expected an indented block

.. code-block:: python

    class MyError(Exception):
        pass


    print('hello')
    # hello


``__file__``
============
.. code-block:: python

    print(__file__)
    # /src/my_file.py

.. code-block:: python

    from os.path import dirname


    print(f'Working directory: {dirname(__file__)}')
    # Working directory: /src

.. code-block:: python

    from os.path import dirname, join


    path = join(dirname(__file__), 'main.py')

    print(f'My file: {path}')
    # My file: /src/main.py

