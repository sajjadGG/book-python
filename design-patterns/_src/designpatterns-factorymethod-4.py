class PDF:
    pass

class TXT:
    pass


class File:
    def __new__(cls, *args, **kwargs):
        filename, extension = args[0].split('.')
        if extension == 'pdf':
            return PDF()
        elif extension == 'txt':
            return TXT()


if __name__ == '__main__':
    file = File('myfile.pdf')
    print(file)
    # <__main__.PDF object at 0x...>

    file = File('myfile.txt')
    print(file)
    # <__main__.TXT object at 0x...>
