OOP Constructor
===============


Rationale
---------
In Object Oriented Programming constructor is:

    a. Special method
    b. Called automatically on object creation
    c. Can set instance attributes with initial values
    d. Works on not fully created object
    e. Method calls are not allowed (as of object is not ready)
    f. Returns None

Python ``__init__()`` method:

    a. Yes
    b. Yes
    c. Yes
    d. No
    e. No
    f. Yes

Python ``__new__()`` method:

    a. Yes
    b. Yes
    c. Yes (could be)
    d. Yes
    e. Yes (before instantiating) / No (after instantiating)
    f. No

In Python by definition both methods ``__new__()`` and ``__init__()``
combined and called consecutively are constructors. This is something
which is not existing in other programming languages, hence programmers
has problem with grasping this idea.

In most cases people will take their "experience" and "habits" from other
languages, mixed with vogue knowledge about ``__new__()`` and call
``__init__()`` a constructor.


Example
-------
>>> class Astronaut:
...     def __new__(cls, *args, **kwargs):
...         print('Before instantiating')
...         result = super().__new__(cls, *args, **kwargs)
...         print('After instantiating')
...         return result
...
...     def __init__(self):
...         print('Initializing')
>>>
>>>
>>> astro = Astronaut()
Before instantiating
After instantiating
Initializing


New Method
----------
* object constructor
* solely for creating the object
* ``cls`` as it's first parameter
* when calling ``__new__()`` you actually don't have an instance yet,
  therefore no ``self`` exists at that moment

.. code-block:: python

    class Astronaut:
        def __new__(cls):
            print('Constructing object')
            return super().__new__(cls)


    Astronaut()
    # Constructing object


Init Method
-----------
* object initializer
* for initializing object with initial values
* ``self`` as it's first parameter
* ``__init__()`` is called after ``__new__()`` and the instance
  is in place, so you can use ``self`` with it
* it's purpose is just to alter the fresh state of the newly created
  instance

.. code-block:: python

    class Astronaut:
        def __init__(self):
            print('Initializing object')


    Astronaut()
    # Initializing object


Return
------
.. code-block:: python

    class Astronaut:
        def __new__(cls):
            print('Constructing object')
            return super().__new__(cls)

        def __init__(self):
            print('Initializing object')


    Astronaut()
    # Constructing object
    # Initializing object


Missing ``return`` from constructor. The instantiation is evaluated to
``None`` since we don't return anything from the constructor:

.. code-block:: python

    class Astronaut:
        def __new__(cls):
            print('Constructing object')
            super().__new__(cls)

        def __init__(self):
            print('Initializing object')  # -> is actually never called


    Astronaut()
    # Constructing object

Return invalid from constructor:

.. code-block:: python

    class Astronaut:
        def __new__(cls):
            return 'Mark Watney'

    Astronaut()
    # 'Mark Watney'

Return invalid from initializer:

.. code-block:: python

    class Astronaut:
        def __init__(self):
            return 'Mark Watney'

    Astronaut()
    # Traceback (most recent call last):
    # TypeError: __init__() should return None, not 'str'



Do not trigger methods for user
-------------------------------
* It is better when user can choose a moment when call ``.connect()`` method

Let user to call method:

.. code-block:: python

    class Server:
        def __init__(self, host, username, password=None):
            self.host = host
            self.username = username
            self.password = password
            self.connect()    # Better ask user to ``connect()`` explicitly

        def connect(self):
            print(f'Logging to {self.host} using: {self.username}:{self.password}')


    connection = Server(
        host='example.com',
        username='myusername',
        password='mypassword')

Let user to call method:

.. code-block:: python

    class Server:
        def __init__(self, host, username, password=None):
            self.host = host
            self.username = username
            self.password = password

        def connect(self):
            print(f'Logging to {self.host} using: {self.username}:{self.password}')


    connection = Server(
        host='example.com',
        username='myusername',
        password='mypassword')

    connection.connect()

However it is better to use ``self.set_position(position_x, position_y)``
than to set those values one by one and duplicate code. Imagine if there
will be a condition boundary checking (for example for negative values):

.. code-block:: python

    class PositionBad:
        def __init__(self, position_x=0, position_y=0):
            self.position_x = position_x
            self.position_y = position_y

        def set_position(self, x, y):
            self.position_x = x
            self.position_y = y


    class PositionGood:
        def __init__(self, position_x=0, position_y=0):
            self.set_position(position_x, position_y)

        def set_position(self, x, y):
            self.position_x = x
            self.position_y = y

.. code-block:: python

    class PositionBad:
        def __init__(self, position_x=0, position_y=0):
            self.position_x = min(1024, max(0, position_x))
            self.position_y = min(1024, max(0, position_y))

        def set_position(self, x, y):
            self.position_x = min(1024, max(0, x))
            self.position_y = min(1024, max(0, y))


    class PositionGood:
        def __init__(self, position_x=0, position_y=0):
            self.set_position(position_x, position_y)

        def set_position(self, x, y):
            self.position_x = min(1024, max(0, x))
            self.position_y = min(1024, max(0, y))


Use Cases - Abstract Factory
----------------------------
* Factory method
* Could be used to implement Singleton

.. code-block:: python

    class PDF:
        pass

    class Docx:
        pass

    class Document:
        def __new__(cls, *args, **kwargs):
            filename, extension = args[0].split('.')

            if extension == 'pdf':
                return PDF()
            elif extension == 'docx':
                return Docx()


    file1 = Document('myfile.pdf')
    file2 = Document('myfile.docx')

    print(file1)
    # <__main__.PDF object at 0x10f89afa0>

    print(file2)
    # <__main__.Docx object at 0x10f6fe9a0>


Use Case - Iris Factory
-----------------------
.. code-block:: python

    from dataclasses import dataclass


    DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa')]


    @dataclass(repr=False)
    class Iris:
        sepal_length: float
        sepal_width: float
        petal_length: float
        petal_width: float

        def __new__(cls, *args, **kwargs):
            *measurements, species = args
            clsname = species.capitalize()
            cls = globals()[clsname]
            return super().__new__(cls)

        def __repr__(self):
            cls = self.__class__.__name__
            args = tuple(vars(self).values())
            return f'\n{cls}{args}'


    class Setosa(Iris):
        pass

    class Virginica(Iris):
        pass

    class Versicolor(Iris):
        pass


    result = [Iris(*row) for row in DATA]
    result
    # [Virginica(5.8, 2.7, 5.1, 1.9),
    #  Setosa(5.1, 3.5, 1.4, 0.2),
    #  Versicolor(5.7, 2.8, 4.1, 1.3),
    #  Virginica(6.3, 2.9, 5.6, 1.8),
    #  Versicolor(6.4, 3.2, 4.5, 1.5),
    #  Setosa(4.7, 3.2, 1.3, 0.2)]


Use Cases - Path
----------------
Note, that this unfortunately does not work this way. ``Path()`` always returns ``PosixPath``:

.. code-block:: python

    from pathlib import Path


    Path('/etc/passwd')
    # PosixPath('/etc/passwd')

    Path('c:\\Users\\Admin\\myfile.txt')
    # WindowsPath('c:\\Users\\Admin\\myfile.txt')

    Path(r'C:\Users\Admin\myfile.txt')
    # WindowsPath('C:\\Users\\Admin\\myfile.txt')

    Path(r'C:/Users/Admin/myfile.txt')
    # WindowsPath('C:/Users/Admin/myfile.txt')


Assignments
-----------
.. literalinclude:: assignments/oop_constructor_a.py
    :caption: :download:`Solution <assignments/oop_constructor_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_constructor_b.py
    :caption: :download:`Solution <assignments/oop_constructor_b.py>`
    :end-before: # Solution
