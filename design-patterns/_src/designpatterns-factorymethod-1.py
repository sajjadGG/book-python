class PDF:
    pass


class Docx:
    pass


class Document:
    def __new__(cls, *args, **kwargs):
        filename, extension = args[0].split('.')

        if extension == 'pdf':
            return PDF()
        elif extension == 'docx':
            return Docx()


file1 = Document('myfile.pdf')
file2 = Document('myfile.docx')

print(file1)
# <__main__.PDF object at 0x10f89afa0>

print(file2)
# <__main__.Docx object at 0x10f6fe9a0>
