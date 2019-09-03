*********************
Classes and Instances
*********************


Object Paradigm
===============
* Model world as objects that interacts with each other

.. glossary::

    class
        Templates for objects.

    instance
    object
        Object created from class.

    method
        Function inside the class.

    property
    attribute
    field
        Variable inside the class.


Classes
=======
* Capitalized ``CamelCase`` name convention
* Classes are templates for objects

.. code-block:: python
    :caption: Defining class. Classes should have capitalized name

    class Iris:
        pass

.. code-block:: python
    :caption: Multi-word class names should use ``CamelCase``

    class IrisSetosa:
        pass


Instances
=========
* Instances are also known as Objects
* Two newlines between class and code
* ``snake_case`` names

.. figure:: img/blueprint.png
    :scale: 8%
    :align: center

    Intuition definition: Class is a blueprint, instances are homes made from this plan. Image source: :cite:`FigureBlueprintHouse`

.. code-block:: python
    :caption: One class and one instance

    class Iris:
        pass


    flower = Iris()

.. code-block:: python
    :caption: One class and three instances

    class Iris:
        pass


    setosa = Iris()
    versicolor = Iris()
    virginica = Iris()

.. code-block:: python
    :caption: Three classes and four instances

    class IrisSetosa:
        pass

    class IrisVersicolor:
        pass

    class IrisVirginica:
        pass


    iris_setosa1 = IrisSetosa()
    iris_setosa2 = IrisSetosa()
    iris_versicolor = IrisVersicolor()
    iris_virginica = IrisVirginica()


Good engineering practices
==========================
* Never print in a class
* One class per file - when classes are long
* All classes in one file - when classes are short
* You can mix classes and functions in one file

.. code-block:: python
    :caption: Classes and Objects

    class IrisSetosa:
        pass

    class IrisVersicolor:
        pass

    class IrisVirginica:
        pass


    setosa = IrisSetosa()
    versicolor = IrisVersicolor()
    virginica = IrisVirginica()

Assignments
===========

Address Book (dataclass)
------------------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/class_instance.py`

:English:
    #. Create class ``Astronaut``
    #. Create class ``Location``

:Polish:
    #. Stwórz klasę ``Astronaut``
    #. Stwórz klasę ``Location``
