Access Modifiers
================


Rationale
---------
* Attributes and methods are always public
* No protected and private keywords
* Protecting is only by convention [#PyDocPrivatevar]_

Attributes:

    * ``name`` - public attribute
    * ``_name`` - protected attribute (non-public by convention)
    * ``__name`` - private attribute (name mangling)
    * ``__name__`` - system attribute
    * ``name_`` - avoid name collision

Methods:

    * ``name(self)`` - public method
    * ``_name(self)`` - protected method (non-public by convention)
    * ``__name(self)`` - private method (name mangling)
    * ``__name__(self)`` - system method
    * ``name_(self)`` - avoid name collision


Example
-------
.. code-block:: python

    class Public:
        firstname: str
        lastname: str

    class Protected:
        _firstname: str
        _lastname: str

    class Private:
        __firstname: str
        __lastname: str


DataClasses
-----------
.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Public:
        firstname: str
        lastname: str


    @dataclass
    class Protected:
        _firstname: str
        _lastname: str


    @dataclass
    class Private:
        __firstname: str
        __lastname: str


Public Attribute
----------------
* ``name`` - public attribute

.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Astronaut:
        firstname: str
        lastname: str


    astro = Astronaut('Mark', 'Watney')

    vars(astro)
    # {'firstname': 'Mark', 'lastname': 'Watney'}

    print(astro.firstname)
    # Mark

    print(astro.lastname)
    # Watney


Protected Attribute
-------------------
* ``_name`` - protected attribute (non-public by convention)
* IDE should warn: "Access to a protected member _firstname of a class"

.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Astronaut:
        _firstname: str
        _lastname: str


    astro = Astronaut('Mark', 'Watney')

    vars(astro)
    # {'_firstname': 'Mark', '_lastname': 'Watney'}

    print(astro._firstname)       # IDE should warn: "Access to a protected member _firstname of a class"
    # Mark

    print(astro._lastname)        # IDE should warn: "Access to a protected member _lastname of a class"
    # Watney


Private Attribute
-----------------
* ``__name`` - private attribute (name mangling)

.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Astronaut:
        __firstname: str
        __lastname: str


    astro = Astronaut('Mark', 'Watney')

    vars(astro)
    # {'_Private__firstname': 'Mark', '_Private__lastname': 'Watney'}

    print(astro._Private__firstname)
    # Mark

    print(astro._Private__lastname)
    # Watney

    print(astro.__firstname)
    # Traceback (most recent call last):
    # AttributeError: 'Private' object has no attribute '__firstname'

    print(astro.__lastname)
    # Traceback (most recent call last):
    # AttributeError: 'Private' object has no attribute '__lastname'


Show Attributes
---------------
* ``vars()`` display ``obj.__dict__``

.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname
            self.publicname = f'{firstname} {lastname[0]}.'


    astro = Astronaut('Mark', 'Watney')

    vars(astro)
    # {'_firstname': 'Mark',
    #  '_lastname': 'Watney',
    #  'publicname': 'Mark W.'}

    public_attributes = {attribute: value
                         for attribute, value in vars(astro).items()
                         if not attribute.startswith('_')}

    protected_attributes = {attribute: value
                            for attribute, value in vars(astro).items()
                            if not attribute.startswith('_')}


    print(public_attributes)
    # {'publicname': 'Mark W.'}

    print(protected_attributes)
    # {'_firstname': 'Mark',
    #  '_lastname': 'Watney'}


System Attributes
-----------------
* ``__name__`` - Current module
* ``obj.__class__``
* ``obj.__dict__`` - Getting dynamic fields and values
* ``obj.__doc__`` - Docstring
* ``obj.__annotations__`` - Type annotations of an object
* ``obj.__module__``

.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Astronaut:
        firstname: str
        lastname: str


    astro = Astronaut('Mark', 'Watney')

    vars(astro)
    # {'firstname': 'Mark',
    #  'lastname': 'Watney'}

    print(astro.__dict__)
    # {'firstname': 'Mark',
    #  'lastname': 'Watney'}


Protected Method
----------------
.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Astronaut:
        _firstname: str
        _lastname: str

        def _get_fullname(self):
            return f'{self._firstname} {self._lastname}'

        def get_publicname(self):
            return f'{self._firstname} {self._lastname[0]}.'


    astro = Astronaut('Mark', 'Watney')

    print(dir(astro))
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    # '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
    # '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_firstname',
    # '_get_fullname', '_lastname', 'get_publicname']

    public_methods = [method
                      for method in dir(astro)
                      if not method.startswith('_')]

    print(public_methods)
    # ['get_publicname']


Private Method
--------------
.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

        def __get_fullname(self):
            return f'{self._firstname} {self._lastname}'

        def get_publicname(self):
            return f'{self._firstname} {self._lastname[0]}.'


    astro = Astronaut('Mark', 'Watney')

    astro.__get_fullname()
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '__get_fullname'


System Method
-------------
.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

        def __str__(self):
            return 'stringification'

        def __repr__(self):
            return 'representation'


    astro = Astronaut('Mark', 'Watney')

    print(str(astro))
    # stringification

    print(repr(astro))
    # representation


Show Methods
------------
* ``dir()``

.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

        def __get_fullname(self):
            return f'{self._firstname} {self._lastname}'

        def get_publicname(self):
            return f'{self._firstname} {self._lastname[0]}.'


    astro = Astronaut('Mark', 'Watney')

    print(dir(astro))
    # ['_Astronaut__get_fullname', '__class__', '__delattr__', '__dict__',
    #  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    #  '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
    #  '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    #  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    #  '__weakref__', '_firstname', '_lastname', 'get_publicname']

    public_methods = [method
                      for method in dir(astro)
                      if not method.startswith('_')]

    print(public_methods)
    # ['get_publicname']



Assignments
-----------
.. literalinclude:: assignments/oop_accessmodifiers_a.py
    :caption: :download:`Solution <assignments/oop_accessmodifiers_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_accessmodifiers_b.py
    :caption: :download:`Solution <assignments/oop_accessmodifiers_b.py>`
    :end-before: # Solution


References
----------
.. [#PyDocPrivatevar] https://docs.python.org/3/tutorial/classes.html#private-variables
