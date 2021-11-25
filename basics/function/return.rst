Function Return
===============


Syntax
------
.. code-block:: python

    def myfunction():
        return <expression>

>>> def mean():
...     return (1+2) / 2

>>> def add():
...     a = 1
...     b = 2
...     return a + b


Return Keyword
--------------
* ``return`` keyword indicates outcome of the function

>>> def hello():
...     return 'hello world'
>>>
>>>
>>> hello()
'hello world'

Code after ``return`` will not execute:

>>> def hello():
...     return 'hello world'
...     print('This will not be executed')
>>>
>>>
>>> hello()
'hello world'

You can have more than one ``return`` keyword in a function, although function
will close after hitting any of them, and will not proceed any further.

>>> def add():
...     if True:
...         return 'yes'
...     else:
...         return 'no'


Return Basic Type
-----------------
>>> def myfunction():
...     return 42

>>> def myfunction():
...     return 13.37

>>> def myfunction():
...     return 'Mark Watney'

>>> def myfunction():
...     return True


Return Sequence
---------------
>>> def myfunction():
...     return list([42, 13.37, 'Mark Watney'])

>>> def myfunction():
...     return [42, 13.37, 'Mark Watney']

>>> def myfunction():
...     return tuple((42, 13.37, 'Mark Watney'))

>>> def myfunction():
...     return (42, 13.37, 'Mark Watney')

>>> def myfunction():
...     return 42, 13.37, 'Mark Watney'

>>> def myfunction():
...     return set({42, 13.37, 'Mark Watney'})

>>> def myfunction():
...     return {42, 13.37, 'Mark Watney'}


Return Mapping
--------------
>>> def myfunction():
...     return dict(firstname='Mark', lastname='Watney')

>>> def myfunction():
...     return {'firstname': 'Mark', 'lastname': 'Watney'}


Return Nested Sequence
----------------------
>>> def myfunction():
...     return [('Mark', 'Watney'),
...             {'Jan Twardowski', 'Melissa Lewis'},
...             {'astro': 'Иван Иванович', 'agency': {'name': 'Roscosmos'}},
...             {'astro': 'Jiménez', 'missions': ('Mercury', 'Gemini')},
...             {'astro': 'Martinez', 'missions': (list(), tuple(), set())}]


Return None
-----------
* Python will ``return None`` if no explicit return is specified

>>> def myfunction():
...     return None

>>> def myfunction():
...     print('hello')

>>> def myfunction():
...     pass

>>> def myfunction():
...     """My function"""


Intercept returned value
------------------------
>>> def myfunction():
...     return 1
>>>
>>>
>>> result = myfunction()
>>> print(result)
1


Assignments
-----------
.. literalinclude:: assignments/function_return_a.py
    :caption: :download:`Solution <assignments/function_return_a.py>`
    :end-before: # Solution
