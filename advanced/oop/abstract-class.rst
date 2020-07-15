****************
Abstract Classes
****************


Rationale
=========
* Cannot instantiate
* Possible to indicate which method must be implemented by child
* Inheriting class must implement all methods
* Some methods can have implementation

.. glossary::
    abstract class
        Class which can only be inherited, not instanciated

    abstract method
        Method must be implemented in a subclass

    abstract static method
        Static method which must be implemented in a subclass


Syntax
======
.. code-block:: python

    from abc import ABC, abstractmethod


    class Astronaut(ABC):
        @abstractmethod
        def hello(self):
            print('My name... José Jiménez ')


    astro = Astronaut()
    # TypeError: Can't instantiate abstract class Astronaut with abstract methods hello


Examples
========
.. code-block:: python
    :caption: Abstract Class

    from abc import ABC, abstractmethod


    class Document(ABC):
        def __init__(self, filename):
            self.filename = filename

        def open(self):
            with open(self.filename) as file:
                return file.read()

        @abstractmethod
        def display(self):
            pass


    class PDFDocument(Document):
        def display(self):
            content = super().display()
            # display ``content`` as PDF Document

    class WordDocument(Document):
        def display(self):
            content = self.display()
            # display ``content`` as Word Document


    file1 = PDFDocument('filename.pdf')
    file1.display()

    file2 = Document('filename.txt')  # TypeError: Can't instantiate abstract class Document with abstract methods display


Assignments
===========

OOP Abstract Class
------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/oop_abstract_class.py`

:English:
    #. Create abstract class ``Iris``
    #. Create abstract method ``get_name()`` in ``Iris``
    #. Create class ``Setosa`` inheriting from ``Iris``
    #. Try to create instance of a class ``Setosa``
    #. Try to create instance of a class ``Iris``

:Polish:
    #. Stwórz klasę abstrakcyjną ``Iris``
    #. Stwórz metodę abstrakcyjną ``get_name()`` w ``Iris``
    #. Stwórz klasę ``Setosa`` dziedziczące po ``Iris``
    #. Spróbuj stworzyć instancje klasy ``Setosa``
    #. Spróbuj stworzyć instancję klasy ``Iris``
