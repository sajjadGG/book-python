Functional Paradigm
===================


Rationale
---------
* Programming paradigm
* Programs are constructed by applying and composing functions
* Functions are treated as first-class citizens
* Functions can be bound to names (including local identifiers), passed as arguments, and returned from other functions, just as any other data type can [#WikipediaFunc]_
* Functional programming avoids side effects, which are used in imperative programming to implement state and I/O
* Pure functional programming completely prevents side-effects and provides referential transparency
* Higher-order functions are rarely used in older imperative programming.
* Imperative program will use a loop to traverse and modify a list, while a functional program, would prefer using a higher-order ``map`` function that takes a function and a list, generating and returning a new list by applying the function to each list item [#Spiewak2008]_
* Restricting side effects, can decrease number of bugs, be easier to debug and test, and be more suited to formal verification [#Hughes1984]_ [#Hudak1989]_
* Functional programming languages are typically less efficient in their use of CPU and memory than imperative languages such as C, Java, Python [#Paulson1996]_
* This is due that some mutable data structures like arrays have a very straightforward implementation using present hardware

.. code-block:: python

    def hello():
        print('My name... José Jiménez')


    type(hello)
    # <class 'function'>

    callable(hello)
    # True







First-class Function
--------------------
* Function can be returned
* Function can be user as a parameter
* Function can be assigned to variable
* Function can be stored in data structures such as hash tables, lists, ...

Function can be returned:

.. code-block:: python

    def lower():
        return 'My name... José Jiménez'


    def higher():
        return lower


    result = higher()     # <function __main__.lower()>
    result()              # 'My name... José Jiménez'

.. code-block:: python

    def lower():
        return 'My name... José Jiménez'

    def higher():
        return lower


    a = higher
    b = higher()

    a
    # <function higher at 0x10a999040>

    a()
    # <function lower at 0x10a802a60>

    a()()
    # 'My name... José Jiménez'

    b
    # <function lower at 0x10a802a60>

    b()
    # 'My name... José Jiménez'

Function can be user as a parameter:

.. code-block:: python

    def http_request(url, on_success, on_error):
        try:
            result = ...
        except Exception as error:
            return on_error(error)
        else:
            return on_success(result)


    http_request(
        url = 'https://python.astrotech.io',
        on_success = lambda result: print(result),
        on_error = lambda error: print(error))

Function can be assigned to variable:

.. code-block:: python

    from datetime import datetime
    from time import sleep


    now = datetime.now

    print(now())          # 1969-07-21 02:56:15
    sleep(10)
    print(now())          # 1969-07-21 02:56:25

Function can be stored in data structures such as hash tables, lists, ...:

.. code-block:: python

    def square(x):
        return x ** 2


    def cube(x):
        return x ** 3


    myfunctions = {
        'cube': cube,
        'square': square,
    }


References
----------
.. [#WikipediaFunc] Functional programming. Retrieved: 2020-10-09. URL: https://en.wikipedia.org/wiki/Functional_programming
.. [#Hudak1989] Hudak, Paul. "Conception, evolution, and application of functional programming languages". ACM Computing Surveys. 21 (3): 359–411. doi:10.1145/72551.72554. S2CID 207637854. 1989.
.. [#Hughes1984] Hughes, John. "Why Functional Programming Matters". Chalmers University of Technology. 1984.
.. [#Spiewak2008] Spiewak, Daniel. "Implementing Persistent Vectors in Scala". Code Commit. 2008.
.. [#Paulson1996] Paulson, Larry C. "ML for the Working Programmer". Cambridge University Press. ISBN: 978-0-521-56543-1. Retrieved: 2013-02-10. 1996.
