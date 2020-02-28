*************************
Static and Dynamic Fields
*************************


Static Fields
=============
* Fields created on class
* Simple to use
* Must have default values
* Share state

.. code-block:: python
    :caption: Static Fields

    class Astronaut:
        agency = 'NASA'


    watney = Astronaut()
    jimenez = Astronaut()

    print(watney.agency)
    # NASA

    print(jimenez.agency)
    # NASA

    print(Astronaut.agency)
    # NASA


Dynamic Fields
==============
* Fields created on instance
* Do not share state
* By convention initialized in ``__init__()``
* You can also initialize on living object directly

.. code-block:: python
    :caption: Dynamic fields

    class Astronaut:
        def __init__(self, agency):
            self.agency = agency


    watney = Astronaut('NASA')
    twardowski = Astronaut('POLSA')

    print(watney.agency)
    # NASA

    print(twardowski.agency)
    # POLSA

    print(Astronaut.agency)
    # AttributeError: type object 'Astronaut' has no attribute 'agency'


Static vs. Dynamic Fields
=========================
.. code-block:: python
    :caption: Static vs. Dynamic fields

    class Astronaut:
        agency = 'NASA'


    watney = Astronaut()
    twardowski = Astronaut()
    ivanovic = Astronaut()

    # Check value of field agency
    watney.agency       # NASA
    twardowski.agency   # NASA
    ivanovic.agency     # NASA
    Astronaut.agency    # NASA

    # Let's change ``agency`` of ``ivanovich`` object
    ivanovic.agency = 'Roscosmos'

    watney.agency       # NASA
    twardowski.agency   # NASA
    ivanovic.agency     # Roscosmos
    Astronaut.agency    # NASA

    # Let's change ``agency`` of ``Astronaut`` class
    Astronaut.agency = 'POLSA'

    watney.agency       # POLSA
    twardowski.agency   # POLSA
    ivanovic.agency     # Roscosmos
    Astronaut.agency    # POLSA


Static or Dynamic?
==================
.. code-block:: python

    class Astronaut:
        first_name = ...
        last_name = ...

.. code-block:: python

    class Cosmonaut:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

.. code-block:: python

    class Taikonaut:
        pass

    t = Taikonaut()
    t.first_name = ...
    t.last_name = ...

.. code-block:: python

    class Taikonaut:
        pass

    Taikonaut.first_name
    Taikonaut.last_name

.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Astronaut:
        name: str
        missions: list

