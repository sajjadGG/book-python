******************
Initializer Method
******************


* It's a first method run after object is initiated
* All classes has default ``__init__()``
* ``__init__()`` is not a constructor!


Initializer method without arguments
====================================
.. code-block:: python
    :caption: Initializer method without arguments

    class Iris:
        def __init__(self):
            print('Latin name: Iris Setosa')


    flower = Iris()
    # Latin name: Iris Setosa


Initializer method with arguments
=================================
.. code-block:: python
    :caption: Initializer method with arguments

    class Iris:
        def __init__(self, species):
            print(f'Latin name: {species}')


    setosa = Iris('Iris Setosa')
    # Latin name: Iris Setosa

    virginica = Iris(species='Iris Virginica')
    # Latin name: Iris Virginica

    iris = Iris()
    # TypeError: __init__() missing 1 required positional argument: 'species'


Assignment
==========

Classes and instances
---------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/syntax_instances.py`

:English:
    #. Create one class ``Temperature``
    #. Create three instances of ``Temperature`` class
    #. Values must be passed at the initialization
    #. At initialization instances print:

        #. Instance ``celsius`` prints temperature 36.6
        #. Instance ``fahrenheit`` prints temperature 97.88
        #. Instance ``kelvin`` prints temperature 309.75

:Polish:
    #. Stwórz jedną klasę ``Temperature``
    #. Stwórz trzy instancje klasy ``Temperature``
    #. Wartości mają być podawane przy inicjalizacji
    #. Przy inicjalizacji instancje wypisują:

        #. Instancja ``celsius`` wyświetla temperaturę 36.6
        #. Instancja ``fahrenheit`` wyświetla temperaturę 97.88
        #. Instancja ``kelvin`` wyświetla temperaturę 309.75
