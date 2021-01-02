Function Definition
===================


Rationale
---------
* Reuse code
* Improves code readability
* Clean-up code
* Allows for easier refactoring


Syntax
------
.. code-block:: python

    def <name>():
        <do something>


Definition
----------
.. code-block:: python

    def say_hello():
        print('My name... José Jiménez')


    say_hello()
    # My name... José Jiménez

    say_hello()
    # My name... José Jiménez

    say_hello()
    # My name... José Jiménez


Convention
----------
* Do not use ``camelCase`` names
* ``CamelCase`` is reserved for class names
* Use ``snake_case`` names # Python - snake ;)
* Add underscore (``_``) at the end of name when name collide
* System functions names starts and ends with 'dunder' - double underscore: ``__``

Do not use ``camelCase``, CamelCase is reserved for class names. Use ``snake_case``:

.. code-block:: python

    def sayHello():
        print('This is camelCase() name')
        print('It is c/c++/Java/JavaScript convention')


    def say_hello():
        print('This is snake_case() name')
        print('It is Pythonic way')

Use better names, rather than comments:

.. code-block:: python

    def cal_var(data, m):
        # Calculate variance
        return sum((Xi-m) ** 2 for Xi in data) / len(data)


    def calculate_variance(data, m):
        return sum((Xi-m) ** 2 for Xi in data) / len(data)

Add underscore (``_``) at the end of name when name collide. Although prefer naming it differently:

.. code-block:: python

    def print_(text):
        # Add underscore (``_``) at the end of name when name collide.
        print(f'<strong>{text}</strong>')


    def print_html(text):
        # Although prefer naming it differently.
        print(f'<strong>{text}</strong>')

System functions names starts and ends with 'dunder' - double underscore: ``__``:

.. code-block:: python

    def __import__(module_name):
        ...


Docstring
---------
* Docstring is a first multiline comment in: File/Module, Class, Method/Function
* Used for generating ``help()`` documentation
* It is accessible in ``__doc__`` property of an object
* Used for ``doctest``
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters
* More information in :ref:`Function Doctest`

Docstring used for documentation:

.. code-block:: python

    def say_hello():
        """This is the say_hello function"""
        print('Hello')


    help(say_hello)
    # Help on function say_hello in module __main__:
    #
    # say_hello()
    #     This is the say_hello function

    print(say_hello.__doc__)
    # This is the say_hello function

Docstring used for documentation:

.. code-block:: python

    def say_hello():
        """
        This is the say_hello function
        And the description is longer then one line
        """
        print('Hello')


    help(say_hello)
    # Help on function say_hello in module __main__:
    #
    # say_hello()
    #     This is the say_hello function
    #     And the description is longer then one line

    print(say_hello.__doc__)
    #    This is the say_hello function
    #    And the description is longer then one line


Assignments
-----------
.. literalinclude:: assignments/function_definition_print.py
    :caption: :download:`Solution <assignments/function_definition_print.py>`
    :end-before: # Solution
