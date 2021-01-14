from abc import ABCMeta, abstractproperty


class Document(metaclass=ABCMeta):
    @abstractproperty
    @property
    def _extension(self):
        return

    def __new__(cls, filename, *args, **kwargs):
        name, extension = filename.split('.')
        for cls in Document.__subclasses__():
            if cls._extension == extension:
                return super().__new__(cls)
        else:
            raise NotImplementedError('File format unknown')


class PDF(Document):
    _extension = 'pdf'

class Txt(Document):
    _extension = 'txt'

class Word(Document):
    _extension = 'docx'


file = Document('myfile.txt')
print(type(file))
# <class '__main__.Txt'>

file = Document('myfile.pdf')
print(type(file))
# <class '__main__.PDF'>
