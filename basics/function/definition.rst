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
>>> def say_hello():
...     print('My name... José Jiménez')
>>>
>>>
>>> say_hello()
My name... José Jiménez
>>> say_hello()
My name... José Jiménez
>>> say_hello()
My name... José Jiménez


Convention
----------
* Add underscore (``_``) at the end of name when name collide
* System functions names starts and ends with 'dunder' - double underscore: ``__``

Do not use ``camelCase`` or ``PascalCase`` names.

The ``camelCase`` name is c/c++/Java/JavaScript convention. It is not good
to mix conventions from different languages. If you write C code, use C
conventions. If you program in Python, use Python conventions. Remember,
there are different communities around both of those languages:

>>> def sayHello():
...     pass

The ``PascalCase`` name has completely different meaning in Python - it is
used for classes. Using such name convention will mistake others.

>>> def SayHello():
...     pass

Use ``snake_case`` names in Python. It is easy to remember. Python looks like
a snake, and sounds like a snake ;) This is double internal joke, because
Python name came from Monty Python, of which Guido van Rossum was a big fun.
The other reference is to duck typing (dynamic typing) - "If it walks like a duck and it quacks like a duck, then it must be a duck":

This is ``snake_case()`` name. It is Pythonic way:

>>> def say_hello():
...     pass

Use better names, rather than comments:

>>> def cal_var(data, m):
...     # Calculate variance
...     return sum((Xi-m) ** 2 for Xi in data) / len(data)

>>> def calculate_variance(data, m):
...     return sum((Xi-m) ** 2 for Xi in data) / len(data)

Add underscore (``_``) at the end of name when name collide. Although prefer naming it differently:

>>> def print_(text):
...     # Add underscore (``_``) at the end of name when name collide.
...     print(f'<strong>{text}</strong>')

>>> def print_html(text):
...     # Although prefer naming it differently.
...     print(f'<strong>{text}</strong>')

System functions names starts and ends with 'dunder' - double underscore: ``__``:

>>> def __import__(module_name):
...     pass


Assignments
-----------
.. literalinclude:: assignments/function_definition_a.py
    :caption: :download:`Solution <assignments/function_definition_a.py>`
    :end-before: # Solution
