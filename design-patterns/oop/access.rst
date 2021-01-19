.. _OOP Access:

******
Access
******


Rationale
=========
.. highlights::
    * Attributes and methods are always public
    * No protected and private keywords
    * Protecting is only by convention [privatevar]_

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

.. code-block:: python

    class Public:
        firstname: str
        lastname: str

        def __init__(self):
            self.firstname = 'Mark'
            self.lastname = 'Watney'


    class Protected:
        _firstname: str
        _lastname: str

        def __init__(self):
            self._firstname = 'Mark'
            self._lastname = 'Watney'


    class Private:
        __firstname: str
        __lastname: str

        def __init__(self):
            self.__firstname = 'Mark'
            self.__lastname = 'Watney'


    obj = Public()
    print(obj.firstname)
    # Mark
    print(obj.lastname)
    # Watney
    print(obj.__dict__)
    # {'firstname': 'Mark', 'lastname': 'Watney'}

    obj = Protected()
    print(obj._firstname)       # IDE should warn: "Access to a protected member _firstname of a class"
    # Mark
    print(obj._lastname)        # IDE should warn: "Access to a protected member _lastname of a class"
    # Watney
    print(obj.__dict__)
    # {'_firstname': 'Mark', '_lastname': 'Watney'}

    obj = Private()
    print(obj.__firstname)
    # Traceback (most recent call last):
    # AttributeError: 'Private' object has no attribute '__firstname'
    print(obj.__lastname)
    # Traceback (most recent call last):
    # AttributeError: 'Private' object has no attribute '__lastname'
    print(obj.__dict__)
    # {'_Private__firstname': 'Mark', '_Private__lastname': 'Watney'}
    print(obj._Private__firstname)
    # Mark
    print(obj._Private__lastname)
    # Watney


Protected Attribute
===================
* ``_name`` - protected attribute (by convention)

Access modifiers:

.. code-block:: python

    class Temperature:
        pass


    temp = Temperature()
    temp._value = 10

    print(temp._value)  # IDE should warn: "Access to a protected member _value of a class"
    # 10

Access modifiers:

.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname
            self.publicname = f'{firstname} {lastname[0]}.'


    mark = Astronaut('Mark', 'Watney')

    print(mark._firstname)  # IDE should warn: "Access to a protected member _firstname of a class"
    # Mark

    print(mark._lastname)  # IDE should warn: "Access to a protected member _lastname of a class"
    # Watney

    print(mark.publicname)
    # Mark W.

    print(mark.firstname)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'firstname'

    print(mark.lastname)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'lastname'


Private Attribute
=================
* ``__name`` - private attribute

.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.__firstname = firstname
            self.__lastname = lastname
            self.publicname = f'{firstname} {lastname[0]}.'


    astro = Astronaut('Mark', 'Watney')

    print(astro.publicname)
    # Mark W.

    print(astro.__firstname)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '__firstname'

    print(astro.__lastname)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '__firstname'

    print(astro.__dict__)
    # {'_Astronaut__firstname': 'Mark',
    #  '_Astronaut__lastname': 'Watney',
    #  'publicname': 'Mark W.'}


System Attributes
=================
* ``__name__`` - system attribute

``obj.__dict__`` - Getting dynamic fields and values:

.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    astro = Astronaut('Mark', 'Watney')

    print(astro.__dict__)
    # {'firstname': 'Mark',
    #  'lastname': 'Watney'}

``obj.__dict__`` - Getting dynamic fields and values:

.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname
            self.publicname = f'{firstname} {lastname[0]}.'


    astro = Astronaut('Mark', 'Watney')

    print(astro.__dict__)
    # {'_firstname': 'Mark',
    #  '_lastname': 'Watney',
    #  'publicname': 'Mark W.'}

    public_attributes = {attribute: value
                         for attribute, value in astro.__dict__.items()
                         if not attribute.startswith('_')}

    print(public_attributes)
    # {'publicname': 'Mark W.'}


Protected Method
================
.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

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
==============
.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

        def __get_fullname(self):
            return f'{self._firstname} {self._lastname}'

        def get_publicname(self):
            return f'{self._firstname} {self._lastname[0]}.'


    mark = Astronaut('Mark', 'Watney')

    print(dir(mark))
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

    mark.__get_fullname()
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '__get_fullname'


System Method
=============
.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

        def __str__(self):
            return 'stringification'

        def __repr__(self):
            return 'representation'


    mark = Astronaut('Mark', 'Watney')

    print(str(mark))
    # stringification

    print(repr(mark))
    # representation


Assignments
===========

.. literalinclude:: ../_assignments/oop_access_a.py
    :caption: :download:`Solution <../_assignments/oop_access_a.py>`
    :end-before: # Solution

.. literalinclude:: ../_assignments/oop_access_b.py
    :caption: :download:`Solution <../_assignments/oop_access_b.py>`
    :end-before: # Solution


References
==========
.. [privatevar] https://docs.python.org/3/tutorial/classes.html#private-variables
