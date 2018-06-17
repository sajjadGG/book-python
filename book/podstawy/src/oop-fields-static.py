class Astronaut:
    first_name = 'Jose'
    last_name = 'Jimenez'
    age = 30


astro = Astronaut()
astro.first_name
# José


class Astronaut:
    first_name: str = 'Jose'
    last_name: str = 'Jimenez'
    age: int = 30


astro = Astronaut()
astro.first_name
# José
