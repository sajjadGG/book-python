"""
* Assignment: OOP Method Mean
* Filename: oop_method_mean.py
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Define class `Stats`
    3. Define method `mean()` in `Stats` class
    4. Method takes `data: list[float]` as an argument
    5. Method returns arithmetic mean of the `data`
    6. Returned value must me rounded to one decimal places
    7. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasę `Stats`
    3. Zdefiniuj metodę `mean()` w klasie `Stats`
    4. Metoda przyjmuje `data: list[float]` jako argument
    5. Metoda zwraca średnią arytmetyczną z `data`
    6. Zwracana wartość ma być zaokrąglona do jednego miejsca po przecinku
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `round()`

Tests:
    >>> from inspect import isclass, ismethod
    >>> assert isclass(Stats)
    >>> stats = Stats()
    >>> assert ismethod(stats.mean)
    >>> stats.mean([1, 2])
    1.5
    >>> stats.mean([5.8, 2.7, 5.1, 1.9])
    3.9
"""


# Solution
class Stats:
    def mean(self, data):
        mean = sum(data) / len(data)
        return round(mean, 1)
