.. _OOP Classes and Instances:

*********************
Classes and Instances
*********************



About
=====
.. highlights::
    * Object Oriented Paradigm
    * Model world as objects that interacts with each other

.. glossary::

    class
        Templates for objects.

    instance
    object
        Object created from class.


Classes
=======
.. highlights::
    * Capitalized ``CamelCase`` name convention
    * Classes are templates for objects

.. code-block:: python
    :caption: Defining class. Classes should have capitalized name

    class Astronaut:
        pass

    class Iris:
        pass

.. code-block:: python
    :caption: Multi-word class names should use ``CamelCase``

    class MyClass:
        pass

    class IrisSetosa:
        pass


Instances
=========
.. highlights::
    * Instances are also known as Objects
    * Two newlines between class and code
    * ``snake_case`` names

Example with Astronauts
-----------------------
.. code-block:: python
    :caption: One class and one instance

    class Astronaut:
        pass


    watney = Astronaut()

.. code-block:: python
    :caption: One class and three instances

    class Astronaut:
        pass


    watney =  = Astronaut()
    twardowski = Astronaut()
    jimenez = Astronaut()

.. code-block:: python
    :caption: Two classes and two instances

    class Astronaut:
        pass

    class Cosmonaut:
        pass


    mark = Astronaut()
    ivan = Cosmonaut()

.. code-block:: python
    :caption: Two classes and four instances (two instances of an ``Astronaut`` class, and two of a ``Cosmonaut`` class)

    class Astronaut:
        pass

    class Cosmonaut:
        pass


    mark = Astronaut()
    melissa = Astronaut()
    ivan = Cosmonaut()
    jan = Cosmonaut()

Examples with Iris
------------------
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
    :caption: Three classes and four instances (two instances of a one class)

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


Class vs Instance
=================
.. figure:: img/blueprint.png
    :width: 75%
    :align: center

    Intuition definition: Class is a blueprint, instances are homes made from this plan. Image source: :cite:`FigureBlueprintHouse`


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

Example
-------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/class_example.py`

:English:
    #. Define class ``Iris``
    #. Create instance ``setosa`` of a class ``Iris``
    #. Create instance ``virginica`` of a class ``Iris``
    #. Create instance ``versicolor`` of a class ``Iris``

:Polish:
    #. Zdefiniuj klasę ``Iris``
    #. Stwórz instancję ``setosa`` klasy ``Iris``
    #. Stwórz instancję ``virginica`` klasy ``Iris``
    #. Stwórz instancję ``versicolor`` klasy ``Iris``

:Solution:
    .. literalinclude:: solution/class_example.py
        :language: python

:The whys and wherefores:
    * :ref:`OOP Classes and Instances`

Class instantiation
-------------------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/class_instance.py`

:English:
    #. Define class ``Astronaut``
    #. Define class ``SpaceAgency``
    #. Create instance ``twardowski`` of a class ``Astronaut``
    #. Create instance ``watney`` of a class ``Astronaut``
    #. Create instance ``nasa`` of a class ``SpaceAgency``
    #. Create instance ``esa`` of a class ``SpaceAgency``
    #. Create instance ``polsa`` of a class ``SpaceAgency``

:Polish:
    #. Zdefiniuj klasę ``Astronaut``
    #. Zdefiniuj klasę ``SpaceAgency``
    #. Stwórz instancję ``twardowski`` klasy ``Astronaut``
    #. Stwórz instancję ``watney`` klasy ``Astronaut``
    #. Stwórz instancję ``nasa`` klasy ``SpaceAgency``
    #. Stwórz instancję ``esa`` klasy ``SpaceAgency``
    #. Stwórz instancję ``polsa`` klasy ``SpaceAgency``

:The whys and wherefores:
    * :ref:`OOP Classes and Instances`
