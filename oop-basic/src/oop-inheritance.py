class Astronaut:
    gender = None

    def what_is_your_gender(self):
        print(f'I am {self.gender}')


class MaleAstronaut(Astronaut):
    gender = 'male'


class FemaleAstronaut(Astronaut):
    gender = 'female'


jose = MaleAstronaut()
jose.what_is_your_gender()       # male

valentina = FemaleAstronaut()
valentina.what_is_your_gender()  # female
