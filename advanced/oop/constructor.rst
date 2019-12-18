*********************
Object initialization
*********************


``__call__()``
==============
* ``__call__()`` method invokes the following:

    * ``__new__()``
    * ``__init__()``

.. code-block:: python
    :caption: Intuition definition of ``__new__()`` and ``__init__()``

    class Iris:
        def __call__(cls):
            iris = Iris.__new__(cls)
            iris.__init__()

.. code-block:: python

    class Astronaut:
        pass


    twardowski = Astronaut      # Creates alias to class (not an instance)
    twardowski()                # Creates instance by calling ``.__call__()``

    twardowski = Astronaut()    # Creates instance by calling ``.__call__()``


``__new__()``
=============
.. highlights::
    * the constructor
    * solely for creating the object
    * ``cls`` as it's first parameter
    * when calling ``__new__()`` you actually don't have an instance yet, therefore no ``self`` exists at that moment

.. code-block:: python
    :emphasize-lines: 2,3,4

    class Iris:
        def __new__(cls):
            print("Iris.__new__() called")
            return super().__new__(cls)

    Iris()
    # Iris.__new__() called


``__init__()``
==============
.. highlights::
    * the initializer
    * for initializing object with data
    * ``self`` as it's first parameter
    * ``__init__()`` is called after ``__new__()`` and the instance is in place, so you can use ``self`` with it
    * it's purpose is just to alter the fresh state of the newly created instance

.. code-block:: python
    :emphasize-lines: 2,3

    class Iris:
        def __init__(self):
            print("Iris.__init__() called")

    Iris()
    # Iris.__init__() called

Example usage
=============
.. code-block:: python
    :emphasize-lines: 3,4

    class Iris:
        def __call__(cls):
            iris = Iris.__new__(cls)
            iris.__init__()

        def __new__(cls):
            print("Iris.__new__() called")
            return super().__new__(cls)

        def __init__(self):
            print("Iris.__init__() called")

    Iris()
    # Iris.__new__() called
    # Iris.__init__() called


Returning values
================

Missing ``return`` from constructor
-----------------------------------
.. code-block:: python
    :emphasize-lines: 3

    class Iris:
        def __new__(cls):
            print("Iris.__new__() called")

        def __init__(self):
            print("Iris.__init__() called")  # -> is actually never called

    Iris()
    # Iris.__new__() called
    # None

The instantiation is evaluated to ``None`` since we don't return anything from the constructor.

Return invalid from constructor
-------------------------------
.. code-block:: python
    :emphasize-lines: 4

    class Iris:
        def __new__(cls):
            print("Iris.__new__() called")
            return 29

    Iris()
    # Iris.__new__() called
    # 29

Return invalid from initializer
-------------------------------
.. code-block:: python
    :emphasize-lines: 4

    class Iris:
        def __init__(self):
            print("Iris.__new__() called")
            return 33

    Iris()
    # TypeError: __init__ should return None

Examples
========
* Factory method
* Could be used to implement Singleton

.. code-block:: python

    class PDF:
        pass

    class Docx:
        pass

    class Document:
        def __call__(self, *args, **kwargs):
            Document.__new__(*args, **kwargs)

        def __new__(cls, *args, **kwargs):
            filename, extension = args[0].split('.')

            if extension == 'pdf':
                return PDF()
            elif extension == 'docx':
                return Docx()


    file1 = Document('myfile.pdf')
    # <__main__.PDF object at 0x1092460f0>

    file2 = Document('myfile.docx')
    # <__main__.DOCX object at 0x107a6c160>

.. code-block:: python

    INPUT = [
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
        (7.1, 3.0, 5.9, 2.1, 'virginica'),
        (4.6, 3.4, 1.4, 0.3, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (5.0, 3.6, 1.4, 0.3, 'setosa'),
        (5.5, 2.3, 4.0, 1.3, 'versicolor'),
        (6.5, 3.0, 5.8, 2.2, 'virginica'),
        (6.5, 2.8, 4.6, 1.5, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (6.9, 3.1, 4.9, 1.5, 'versicolor'),
        (4.6, 3.1, 1.5, 0.2, 'setosa'),
    ]


    class Iris:
        def __new__(cls, *args, **kwargs):
            *measurements, species = args

            if species == 'setosa':
                cls = Setosa
            elif species == 'versicolor':
                cls = Versicolor
            elif species == 'virginica':
                cls = Virginica
            else:
                raise TypeError

            return object.__new__(cls)

        def __init__(self, sepal_length, sepal_width,
                     petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species


    class Setosa(Iris):
        pass

    class Virginica(Iris):
        pass

    class Versicolor(Iris):
        pass


    OUTPUT = []

    for row in INPUT:
        iris = Iris(*row)
        OUTPUT.append(iris)


Initial arguments mutability and shared state
=============================================

.. _Initial arguments mutability and shared state:

Bad
---
.. code-block:: python
    :caption: Initial arguments mutability and shared state

    class Astronaut:
        def __init__(self, name, missions=[]):
            self.name = name
            self.missions = missions


    watney = Astronaut('Mark Watney')
    watney.missions.append('Ares 3')
    print(watney.missions)
    # ['Ares 3']

    twardowski = Astronaut('Jan Twardowski')
    print(twardowski.missions)
    # ['Ares 3']

Good
----
.. code-block:: python
    :caption: Initial arguments mutability and shared state

    class Contact:
        def __init__(self, name, missions=()):
            self.name = name
            self.missions = list(missions)


    watney = Astronaut('Mark Watney')
    watney.missions.append('Ares 3')
    print(watney.missions)
    # ['Ares 3']

    twardowski = Astronaut('Jan Twardowski')
    print(twardowski.missions)
    # []

Do not run methods in ``__init__()``
====================================
* It is better when user can choose a moment when call ``.connect()`` method

.. code-block:: python
    :caption: Let user to call method

    class Server:

        def __init__(self, host, username, password=None):
            self.host = host
            self.username = username
            self.password = password
            self.connect()    # Better ask user to ``connect()`` explicitly

        def connect(self):
            print(f'Logging to {self.host} using: {self.username}:{self.password}')


    localhost = Server(
        host='localhost',
        username='admin',
        password='admin'
    )

    # This is better
    localhost.connect()
