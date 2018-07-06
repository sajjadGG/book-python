class File:

    def __init__(self, name, content=[]):
        self.name = name
        self.content = content

    def append(self, line):
        self.content.extend(line)

    def write(self):
        with open(self.name, 'w') as file:
            file.write(self.content)

    def __enter__(self):
        pass

    def __exit__(self, **kwargs):
        return self.write()


with File('asd.txt') as file:
    file.append('nowa linia')

# dopiero po wyjsciu z with, plik zostanie zapisany
