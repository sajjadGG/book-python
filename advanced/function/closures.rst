********
Closures
********


Nested Function
===============
* Function inside the function
* nested functions can access the variables of the enclosing scope

.. code-block:: python

    def outer(message):

        def inner():
            print(message)

        return inner


What is closure?
================
* technique by which the data is attached to some code even after end of those other original functions is called as closures
* Closures can avoid use of global variables and provides some form of data hiding
* When the interpreter detects the dependency of inner nested function on the outer function, it stores or makes sure that the variables in which inner function depends on are available even if the outer function goes away
* Method of binding data to a function without actually passing them as parameters is called closure
* It is a function object obj that remembers values in enclosing scopes even if they are not present in memory
* Closures provide some sort of data hiding as they are used as callback functions
* This helps us to reduce the use of global variables
* Useful for replacing hard-coded constants
* Closures prove to be efficient way when we have few functions in our code

.. code-block:: python

    def outer(message):

        def inner():
            print(message)

        return inner


    todo = outer('hello')
    todo()
    # hello

    del outer
    todo()
    # hello

.. code-block:: python

    def f(x):
        def g(y):
            return x + y
        return g


Examples
========
.. code-block:: python
    :caption: Functions has access to the outer scope

    data = [1, 2, 3]

    def outer():
        print('inner', data)

    outer()
    # inner [1, 2, 3]

    print('outer', data)
    # outer [1, 2, 3]

.. code-block:: python
    :caption: Variables in functions can shadow outer scope. Outer scope is restored, when function returns

    data = [1,2,3]

    def outer():
        data = ['a', 'b', 'c']
        print('inner', data)

    outer()
    # inner ['a', 'b', 'c']

    print('outer', data)
    # outer [1, 2, 3]

.. code-block:: python
    :caption: Functions can modify outer scope

    data = [1,2,3]

    def outer():
        global data
        data = ['a', 'b', 'c']
        print('inner', data)

    outer()
    # inner ['a', 'b', 'c']

    print('outer', data)
    # outer ['a', 'b', 'c']

.. code-block:: python
    :caption: ``inner`` function (closure) has access to its outer scope, that is ``outer`` function.

    def outer():
        data = ['a', 'b', 'c']

        def inner():
            print('inner', data)

        inner()
        print('outer', data)

    outer()
    # inner ['a', 'b', 'c']
    # outer ['a', 'b', 'c']

.. code-block:: python

    def outer():
        data = ['a', 'b', 'c']

        def inner():
            print('inner', data)

        return inner


    my_ptr = outer()

    print(my_ptr)
    # <function outer.<locals>.inner at 0x11bfb8560>

    my_ptr()
    # inner ['a', 'b', 'c']

.. code-block:: python

    def outer():
        data = ['a', 'b', 'c']

        def inner():
            print('inner', data)

        return inner


    my_ptr = outer()

    print(my_ptr)
    # <function outer.<locals>.inner at 0x10617c8b0>

    del outer

    print(my_ptr)
    # <function outer.<locals>.inner at 0x10617c940>

    my_ptr()
    # inner ['a', 'b', 'c']
