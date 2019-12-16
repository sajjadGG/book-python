*************************
Static and Dynamic Fields
*************************


Static Fields
=============
* Simple to use
* Must have default values
* Share state

.. code-block:: python
    :caption: Static Fields

    class Iris:
        species = 'setosa'


    setosa = Iris()
    versicolor = Iris()

    setosa.species      # setosa
    versicolor.species  # setosa
    Iris.species        # setosa


Dynamic Fields
==============
* Require ``__init__()``

.. code-block:: python
    :caption: Dynamic fields

    class Iris:
        def __init__(self, species):
            self.species = species


    setosa = Iris('setosa')
    versicolor = Iris('versicolor')

    setosa.species      # setosa
    versicolor.species  # versicolor
    Iris.species        # AttributeError: type object 'Iris' has no attribute 'species'


Static vs. Dynamic Fields
=========================
.. code-block:: python
    :caption: Static vs. Dynamic fields

    class Iris:
        kingdom = 'Plantae'

        def __init__(self, species):
            self.species = species


    setosa = Iris('setosa')
    versicolor = Iris('versicolor')
    virginica = Iris('virginica')


    # Check value of field agency
    setosa.kingdom       # Plantae
    versicolor.kingdom   # Plantae
    virginica.kingdom    # Plantae
    Iris.kingdom         # Plantae


    # Let's change ``kingdom`` of ``setosa`` object
    setosa.kingdom = 'Flower'

    setosa.kingdom       # Flower
    versicolor.kingdom   # Plantae
    virginica.kingdom    # Plantae
    Iris.kingdom         # Plantae


    # Let's change ``kingdom`` of ``Iris`` class
    Iris.kingdom = 'Iris'

    setosa.kingdom       # Flower
    versicolor.kingdom   # Iris
    virginica.kingdom    # Iris
    Iris.kingdom         # Iris

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

