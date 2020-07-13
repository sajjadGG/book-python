********
Closures
********


Nested Function
===============
* Function inside the function
* nested functions can access the variables of the enclosing scope

.. code-block:: python

    def run():
        lastname = 'Twardowski'

        def hello():
            print(lastname)

        return hello

    hello()
    # NameError: name 'hello' is not defined

    run()
    # <function __main__.run.<locals>.hello()>

    hello = run()
    hello()
    # Twardowski

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

    firstname = 'Jan'
    lastname = 'Twardowski'

    def hello():
        print(firstname)
        print(lastname)

    hello()
    # Jan
    # Twardowski

.. code-block:: python

    firstname = 'Jan'

    def run():
        lastname = 'Twardowski'

        def hello():
            print(firstname)
            print(lastname)

        return hello


    hello = run()
    hello()
    # Jan
    # Twardowski

.. code-block:: python

    firstname = 'Jan'

    def run():
        lastname = 'Twardowski'

        def hello():
            print(firstname)
            print(lastname)

        return hello


    hello = run()
    del run
    hello()
    # Jan
    # Twardowski

.. code-block:: python

    def f(x):
        def g(y):
            return x + y
        return g
