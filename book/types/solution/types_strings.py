"""
#. Napisz program, który na podstawie paragrafu tekstu "Lorem Ipsum" podzieli go na zdania
#. Kropka rozdziela zdania
#. Spacja oddziela wyrazy w zdaniu
#. Za pomocą funkcji ``len()`` policz ile jest wyrazów w każdym zdaniu::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

:Założenia:
    * Nazwa pliku: ``types_strings.py``
    * Szacunkowa długość kodu: 3 linie
    * Maksymalny czas na zadanie: 5 min

:Co zadanie sprawdza:
    * Dzielenie stringów
    * Sprawdzanie długości ciągów znaków
    * Iterowanie po elementach w tablicy

:Podpowiedź:
    * .. code-block:: python

        lista = ['Element 1', 'Element 2']

        for element in lista:
            print(element)
"""

TEXT = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'


for sentence in TEXT.split('.'):
    words = sentence.split(' ')
    count = len(words)
    print(count)
