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

