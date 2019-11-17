****************
Abstract classes
****************


What it is?
===========
* Cannot instantiate
* Possible to indicate which method must be implemented by child
* Inheriting class must implement all methods
* Some methods can have implementation


When use it?
============


Abstract classes and methods
============================
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
            return self.open()


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
