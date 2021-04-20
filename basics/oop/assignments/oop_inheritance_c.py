"""
* Assignment: OOP Inheritance Super
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create class `Astronaut` which inherits from `Person`
    3. Class `Astronaut` takes two arguments `name` and `mission`
    4. Set attribute `mission` in `Astronaut` inicializer method
    5. Call initializer method of `Person` passing `name` as an argument
    6. Define method `show()` returning name and after coma - a mission name
    6. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz klasę `Astronaut` dziedziczącą po `Person`
    3. Klasa `Astronaut` przyjmuje dwa argumenty `name` i `mission`
    4. Ustaw atrybut `mission` w metodzie inicjalizacyjnej w `Astronaut`
    5. Wywołaj metodę inicjalizacyjną z `Person` podając `name` jako argument
    6. Zdefiniuj metodę `show()` zwracającą imię i po przecinku - nazwę misji
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> watney = Astronaut('Watney', 'Ares 3')
    >>> watney.show()
    'Watney, Ares 3'
    >>> lewis = Astronaut('Lewis', 'Ares 3')
    >>> lewis.show()
    'Lewis, Ares 3'
"""


# Given
class Person:
    def __init__(self, name):
        self.name = name


# Solution
class Astronaut(Person):
    def __init__(self, name, mission):
        super().__init__(name)
        self.mission = mission

    def show(self):
        return f'{self.name}, {self.mission}'
