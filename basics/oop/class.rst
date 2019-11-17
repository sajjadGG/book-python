.. _OOP Classes and Instances:

*************************
OOP Classes and Instances
*************************


Object Paradigm
===============
.. highlights::
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
.. highlights::
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
.. highlights::
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
.. highlights::
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

Classes and instances
---------------------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/class_instance.py`

:English:
    #. Define class ``Astronaut``
    #. Define class ``Location``
    #. Create instance ``twardowski`` of a class ``Astronaut``
    #. Create instance ``watney`` of a class ``Astronaut``
    #. Create instance ``jsc`` of a class ``Location``
    #. Create instance ``ksc`` of a class ``Location``
    #. Create instance ``jpl`` of a class ``Location``

:Polish:
    #. Zdefiniuj klasę ``Astronaut``
    #. Zdefiniuj klasę ``Location``
    #. Stwórz instancję ``twardowski`` klasy ``Astronaut``
    #. Stwórz instancję ``watney`` klasy ``Astronaut``
    #. Stwórz instancję ``jsc`` klasy ``Location``
    #. Stwórz instancję ``ksc`` klasy ``Location``
    #. Stwórz instancję ``jpl`` klasy ``Location``

:The whys and wherefores:
    * :ref:`Classes and Instances`
