"""
* Assignment: Exception Catch Else
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Ask user to input angle in degrees
    2. User can input any value (even nonnumeric)
    2. Cotangent for 180 degrees is infinite
    3. Define own exception `CotangentError`
    4. If user typed angle equal to 180, raise your exception

Polish:
    1. Poproś użytkownika o wprowadzenie kąta
    2. Uwaga, użytkownik może podać dowolną wartość (nawet nienumeryczną)
    2. Cotangens dla konta 180 ma nieskończoną wartość
    3. Zdefiniuj własny wyjątek `CotangentError`
    4. Jeżeli użytkownik wprowadził kąt równy 180, podnieś swój wyjątek

English:
    1. Use data from "Given" section (see below)
    2. Convert value passed to the function as a `float`
        a. If conversion fails, print 'Degrees expects int or float'
    3. Non functional Requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj wartośc przekazaną do funckji jako `float`
        a. Jeżeli konwersja się nie powiedzie, wypisz 'Degrees expects int or float'
        b. Jeżeli nie było błędu sprawdź czy `degree` jest równe 180
        c.
    3. Non functional Requirements
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)



Tests:
    >>> check(1)
    >>> check(180)
    Traceback (most recent call last):
    controlflow_exception_g.CotangentError
"""


# Given
def check(value):
    ...


# Solution
def check(degrees):
    try:
        degrees = float(degrees)
    except ValueError:
        print('Degrees expects int or float')
    else:
        if degrees == 180:
            raise ArithmeticError
