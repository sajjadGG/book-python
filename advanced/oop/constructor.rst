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

>>> class Astronaut:
...     def __new__(cls):
...         print('Constructing object')
...         return super().__new__(cls)
>>>
>>>
>>> astro = Astronaut()
Constructing object


Init Method
-----------
* object initializer
* for initializing object with initial values
* ``self`` as it's first parameter
* ``__init__()`` is called after ``__new__()`` and the instance
  is in place, so you can use ``self`` with it
* it's purpose is just to alter the fresh state of the newly created
  instance

>>> class Astronaut:
...     def __init__(self):
...         print('Initializing object')
>>>
>>>
>>> astro = Astronaut()
Initializing object


Return
------
>>> class Astronaut:
...     def __new__(cls):
...         print('Constructing object')
...         return super().__new__(cls)
...
...     def __init__(self):
...         print('Initializing object')
>>>
>>>
>>> astro = Astronaut()
Constructing object
Initializing object

Missing ``return`` from constructor. The instantiation is evaluated to
``None`` since we don't return anything from the constructor:

>>> class Astronaut:
...     def __new__(cls):
...         print('Constructing object')
...         super().__new__(cls)
...
...     def __init__(self):
...         print('Initializing object')  # -> is actually never called
>>>
>>>
>>> astro = Astronaut()
Constructing object
>>>
>>> type(astro)
<class 'NoneType'>

Return invalid from constructor:

>>> class Astronaut:
...     def __new__(cls):
...         return 'Mark Watney'
>>>
>>> astro = Astronaut()
>>>
>>> type(astro)
<class 'str'>
>>> astro
'Mark Watney'

Return invalid from initializer:

>>> class Astronaut:
...     def __init__(self):
...         return 'Mark Watney'
>>>
>>> astro = Astronaut()
Traceback (most recent call last):
TypeError: __init__() should return None, not 'str'


Do not trigger methods for user
-------------------------------
* It is better when user can choose a moment when call ``.connect()`` method

Let user to call method:

>>> class Server:
...     def __init__(self, host, username, password=None):
...         self.host = host
...         self.username = username
...         self.password = password
...         self.connect()    # Better ask user to ``connect()`` explicitly
...
...     def connect(self):
...         print(f'Logging to {self.host} using: {self.username}:{self.password}')
>>>
>>>
>>> connection = Server(
...     host='example.com',
...     username='admin',
...     password='myVoiceIsMyPassword')
Logging to example.com using: admin:myVoiceIsMyPassword

Let user to call method:

>>> class Server:
...     def __init__(self, host, username, password=None):
...         self.host = host
...         self.username = username
...         self.password = password
...
...     def connect(self):
...         print(f'Logging to {self.host} using: {self.username}:{self.password}')
>>>
>>>
>>> connection = Server(
...     host='example.com',
...     username='admin',
...     password='myVoiceIsMyPassword')
>>>
>>> connection.connect()
Logging to example.com using: admin:myVoiceIsMyPassword

However it is better to use ``self.set_position(position_x, position_y)``
than to set those values one by one and duplicate code. Imagine if there
will be a condition boundary checking (for example for negative values):

>>> class PositionBad:
...     def __init__(self, position_x=0, position_y=0):
...         self.position_x = position_x
...         self.position_y = position_y
...
...     def set_position(self, x, y):
...         self.position_x = x
...         self.position_y = y
>>>
>>>
>>> class PositionGood:
...     def __init__(self, position_x=0, position_y=0):
...         self.set_position(position_x, position_y)
...
...     def set_position(self, x, y):
...         self.position_x = x
...         self.position_y = y

>>> class PositionBad:
...     def __init__(self, position_x=0, position_y=0):
...         self.position_x = min(1024, max(0, position_x))
...         self.position_y = min(1024, max(0, position_y))
...
...     def set_position(self, x, y):
...         self.position_x = min(1024, max(0, x))
...         self.position_y = min(1024, max(0, y))
>>>
>>>
>>> class PositionGood:
...     def __init__(self, position_x=0, position_y=0):
...         self.set_position(position_x, position_y)
...
...     def set_position(self, x, y):
...         self.position_x = min(1024, max(0, x))
...         self.position_y = min(1024, max(0, y))


Use Case - 0x01
---------------
* Iris Factory

>>> from dataclasses import dataclass, field
>>>
>>>
>>> DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str = field(repr=False)
...
...     def __new__(cls, *args, **kwargs):
...         *measurements, species = args
...         clsname = species.capitalize()
...         cls = globals()[clsname]
...         return super().__new__(cls)
>>>
>>>
>>> class Setosa(Iris):
...     pass
>>>
>>> class Virginica(Iris):
...     pass
>>>
>>> class Versicolor(Iris):
...     pass
>>>
>>>
>>> result = [Iris(*row) for row in DATA]
>>> result  # doctest: +NORMALIZE_WHITESPACE
[Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
 Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
 Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
 Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
 Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
 Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2)]


Use Case - 0x02
---------------
* Path

Note, that this unfortunately does not work this way. ``Path()`` always returns ``PosixPath``:

>>> from pathlib import Path
>>>
>>>
>>> Path('/etc/passwd')
PosixPath('/etc/passwd')
>>>
>>> Path('c:\\Users\\Admin\\myfile.txt')  # doctest: +SKIP
WindowsPath('c:\\Users\\Admin\\myfile.txt')
>>>
>>> Path(r'C:\Users\Admin\myfile.txt')  # doctest: +SKIP
WindowsPath('C:\\Users\\Admin\\myfile.txt')
>>>
>>> Path(r'C:/Users/Admin/myfile.txt')  # doctest: +SKIP
WindowsPath('C:/Users/Admin/myfile.txt')


Use Case - 0x03
---------------
* Document Factory 1
* Factory method
* Could be used to implement Singleton

>>> class PDF:
...     pass
>>>
>>> class Docx:
...     pass
>>>
>>> class Document:
...     def __new__(cls, *args, **kwargs):
...         filename, extension = args[0].split('.')
...         if extension == 'pdf':
...             return PDF()
...         elif extension == 'docx':
...             return Docx()
>>>
>>>
>>> file1 = Document('myfile.pdf')
>>> file2 = Document('myfile.docx')
>>>
>>> print(file1)  # doctest: +ELLIPSIS
<PDF object at 0x...>
>>>
>>> print(file2)  # doctest: +ELLIPSIS
<Docx object at 0x...>


Use Case - 0x04
---------------
* Document Factory 2

>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class Filetype(ABC):
...     @abstractmethod
...     def display(self):
...         raise NotImplementedError
...
...     def __init__(self, filename):
...         self.filename = filename
>>>
>>>
>>> class PDF(Filetype):
...     def display(self):
...         pass
>>>
>>>
>>> class DOCX(Filetype):
...     def display(self):
...         pass
>>>
>>>
>>> class Document:
...     def __new__(cls, filename):
...         filetypes = Filetype.__subclasses__()
...         _, extension = filename.split('.')
...
...         for typ in filetypes:
...             if typ.__name__ == extension.upper():
...                 return typ(filename)
...         else:
...             raise NotImplementedError('Filetype is not recognized')
>>>
>>>
>>> Document('myfile.pdf')  # doctest: +ELLIPSIS
<PDF object at 0x...>
>>> Document('myfile.docx')  # doctest: +ELLIPSIS
<DOCX object at 0x...>


Use Case - 0x05
---------------
* Document Factory 3

>>> from abc import ABC, abstractmethod, abstractproperty
>>>
>>>
>>> class Filetype(ABC):
...     @abstractproperty
...     def EXTENSIONS(self) -> str: ...
...
...     @abstractmethod
...     def display(self):
...         raise NotImplementedError
...
...     def __init__(self, filename):
...         self.filename = filename
>>>
>>>
>>> class PDF(Filetype):
...     EXTENSIONS = ['pdf']
...
...     def display(self):
...         pass
>>>
>>>
>>> class DOCX(Filetype):
...     EXTENSIONS = ['docx', 'doc']
...
...     def display(self):
...         pass
>>>
>>>
>>> class Document:
...     def __new__(cls, filename):
...         filetypes = Filetype.__subclasses__()
...         _, extension = filename.split('.')
...
...         for typ in filetypes:
...             if extension in typ.EXTENSIONS:
...                 return typ(filename)
...         else:
...             raise NotImplementedError('Filetype is not recognized')
>>>
>>>
>>> Document('myfile.pdf')  # doctest: +ELLIPSIS
<PDF object at 0x...>
>>> Document('myfile.doc')  # doctest: +ELLIPSIS
<DOCX object at 0x...>
>>> Document('myfile.docx')  # doctest: +ELLIPSIS
<DOCX object at 0x...>


Use Case - 0x06
---------------
* Document Factory 4

>>> from abc import ABC, abstractmethod, abstractproperty
>>>
>>>
>>> class Document(ABC):
...     @abstractproperty
...     def EXTENSIONS(self) -> list[str]: ...
...
...     def __new__(cls, filename):
...         filetypes = cls.__subclasses__()
...         _, extension = filename.split('.')
...
...         for typ in filetypes:
...             if extension in typ.EXTENSIONS:
...                 instance = object.__new__(typ)
...                 instance.__init__(filename)
...                 return instance
...         else:
...             raise NotImplementedError('Filetype is not recognized')
...
...     def __init__(self, filename):
...         self.filename = filename
...
...     @abstractmethod
...     def display(self):
...         raise NotImplementedError
>>>
>>>
>>> class PDF(Document):
...     EXTENSIONS = ['pdf']
...
...     def display(self):
...         pass
>>>
>>>
>>> class DOCX(Document):
...     EXTENSIONS = ['docx', 'doc']
...
...     def display(self):
...         pass
>>>
>>>
>>> Document('myfile.pdf')  # doctest: +ELLIPSIS
<PDF object at 0x...>
>>> Document('myfile.doc')  # doctest: +ELLIPSIS
<DOCX object at 0x...>
>>> Document('myfile.docx')  # doctest: +ELLIPSIS
<DOCX object at 0x...>


Assignments
-----------
.. literalinclude:: assignments/oop_constructor_a.py
    :caption: :download:`Solution <assignments/oop_constructor_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_constructor_b.py
    :caption: :download:`Solution <assignments/oop_constructor_b.py>`
    :end-before: # Solution
