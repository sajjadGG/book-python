**************
Random Numbers
**************


``random``
==========
.. csv-table:: ``random``
    :header-rows: 1

    "Function", "Description"
    "``random.random()``", "Random float:  0.0 <= x < 1.0"
    "``random.randint(min, max)``", "Return a random integer N such that ``min <= N <= max``. Max is included"
    "``random.gauss(mu, sigma)``", "Gaussian distribution. mu is the mean, and sigma is the standard deviation"
    "``random.shuffle(list)``", "Randomize order of list (in place)"
    "``random.choice(list)``", "Single random element from a sequence"
    "``random.sample(list, k)``", "k random elements from list without replacement"
    "``random.seed(a=None, version=2)``", "Initialize the random number generator. If a is omitted or None, the current system time is used"


Assignments
===========

Random numbers
--------------
* Filename: ``math/random_numbers.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min

#. Napisz program, który wyświetli 6 losowych i nie powtarzających się liczb z zakresu od 1 do 49.
#. Czym sa liczby pseudolosowe?
#. Czy da się stworzyć program czysto losowy?
#. Dlaczego?

:Hints:
    * ``random.randrange()``
    * ``random.sample()``

:The whys and wherefores:
    * Umiejętność wykorzystania gotowych funkcji w bibliotece standardowej
    * Umiejętność wyszukania informacji na temat API funkcji w dokumentacji języka i jego odpowiedniej wersji
    * Stworzenie dwóch alternatywnych podejść do rozwiązania zadania
    * Porównanie czytelności obu rozwiązań
    * Umiejętność sprawdzania czy coś znajduje się w liście oraz ``continue``

Sum of inner elements
---------------------
* Filename: ``math/inner_sum.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min

#. Ustaw ``random.seed(0)``
#. Za pomocą biblioteki ``random`` wygeneruj ``List[List[int]]`` (cyfry z przedziału <0,9> włącznie)
#. Tablica ma mieć 16 wierszy i 16 kolumn
#. Policz sumę środkowych 4x4 elementów
#. Środkowych = centralna macierz 4x4 dokładnie w środku większej
