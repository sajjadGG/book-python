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


Example
=======
.. code-block:: python
    :caption: Functions has access to the outer scope

    data = [1, 2, 3]

    def add():
        print('inside', data)

    add()
    # inside [1, 2, 3]

    print('outside', data)
    # outside [1, 2, 3]

.. code-block:: python
    :caption: Variables in functions can shadow outer scope. Outer scope is restored, when function returns

    data = [1,2,3]

    def add():
        data = ['a', 'b', 'c']
        print('inside', data)

    add()
    # inside ['a', 'b', 'c']

    print('outside', data)
    # outside [1, 2, 3]

.. code-block:: python
    :caption: Functions can modify outer scope

    data = [1,2,3]

    def add():
        global data
        data = ['a', 'b', 'c']
        print('inside', data)

    add()
    # inside ['a', 'b', 'c']

    print('outside', data)
    # outside ['a', 'b', 'c']

.. code-block:: python
    :caption: ``inside`` function (closure) has access to its outer scope, that is ``outside`` function.

    def outside():
        data = ['a', 'b', 'c']

        def inside():
            print('inside', data)

        inside()
        print('outside', data)

    outside()
    # inside ['a', 'b', 'c']
    # outside ['a', 'b', 'c']

.. code-block:: python

    def outside():
        data = ['a', 'b', 'c']

        def inside():
            print('inside', data)

        return inside


    my_ptr = outside()

    print(my_ptr)
    # <function outside.<locals>.inside at 0x11bfb8560>

    my_ptr()
    # inside ['a', 'b', 'c']

.. code-block:: python

    def outside():
        data = ['a', 'b', 'c']

        def inside():
            print('inside', data)

        return bbb


    my_ptr = add()
    del add

    print(my_ptr)
    # <function add.<locals>.bbb at 0x11bfb85f0>

    my_ptr()
    # inside ['a', 'b', 'c']
