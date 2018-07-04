from abc import ABC, abstractmethod


class Document(ABC):
    def __init__(self, filename):
        self.filename = filename

    def open(self):
        with open(self.filename) as file:
            return file.read()

    @abstractmethod
    def display(self):
        raise NotImplementedError


class PDFDocument(Document):
    def display(self):
        content = self.open()
        # parse as PDF Document


class WordDocument(Document):
    def display(self):
        content = self.open()
        # parse as Word Document


file1 = PDFDocument('filename.pdf')
file1.display()

file2 = Document('filename.txt')  # TypeError: Can't instantiate abstract class Document with abstract methods display
