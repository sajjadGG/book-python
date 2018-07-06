class Astronaut:
    first_name = ''  # public
    last_name = ''  # public
    _agency = None  # private

    def print_(self):  # name collision
        print(self.__str__())

    def __str__(self):  # system function
        return f'My name is {self.name}'