class Astronaut:
    name = ''

    def set_name(self, name):
        print('I can print some log messages')
        self.name = name

    def get_name(self):
        return self.name


# Java way
jose = Astronaut()
jose.set_name('Jose Jimenez')
print(jose.get_name())

# Python way
ivan = Astronaut()
ivan.name = 'Ivan Ivanovic'
print(ivan.name)
