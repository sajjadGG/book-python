class Document:
    extension = None

    def __new__(cls, filename, *args, **kwargs):
        name, extension = filename.split('.')
        for cls in Document.__subclasses__():
            if cls.extension == extension:
                return super().__new__(cls)
        else:
            raise NotImplementedError('File format unknown')


class PDF(Document):
    extension = 'pdf'

class Txt(Document):
    extension = 'txt'

class Word(Document):
    extension = 'docx'


file = Document('myfile.txt')
print(type(file))
# <class '__main__.Txt'>

file = Document('myfile.pdf')
print(type(file))
# <class '__main__.PDF'>
