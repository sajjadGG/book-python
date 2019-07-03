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


``__dict__`` - Getting dynamic fields and values
================================================
.. code-block:: python
    :caption: ``__dict__`` - Getting dynamic fields and values

    class Iris:
        def __init__(self, sepal_length, sepal_width,
                     petal_length, petal_width, species):

            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

    flower = Iris(
        sepal_length=5.1,
        sepal_width=3.5,
        petal_length=1.4,
        petal_width=0.2,
        species='setosa'
    )

    flower.__dict__
    # {'sepal_length': 5.1,
    # 'sepal_width': 3.5,
    # 'petal_length': 1.4,
    # 'petal_width': 0.2,
    # 'species': 'setosa'}
