class Bear:
    def sound(self):
        print('Groarrr')


class Dog:
    def sound(self):
        print('Woof woof!')


def makeSound(animal):
    animal.sound()


koala = Bear()
hart = Dog()

makeSound(koala)
makeSound(hart)
