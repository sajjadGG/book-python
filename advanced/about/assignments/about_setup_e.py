"""
* Assignment: About Setup Doctest
* Complexity: easy
* Lines of code: 0 lines
* Time: 5 min

English:
    1. Copy this assignment to file named `about_doctest.py` in your directory
    2. Run doctests from this file
        a. Top menu -> Run -> Run... -> Doctest in about_setup_doctest
        b. Right mouse click -> Run 'Doctests in about_setup_doctest'
    3. All tests must pass
    4. Note the line with comment `# doctest: +NORMALIZE_WHITESPACE`
        a. This is the doctest flag
        b. It allows to ignore whitesapces and newlines in lists, tuples, dicts, etc.
        c. Try to remove it (without chaning the result) and check if tests still passes
    5. Write `100%` in shared spreadsheet at assignment row

Polish:
    1. Skopiuj to zadanie do pliku o nazwie `about_doctest.py` w Twoim katalogu
    2. Uruchom doctesty z tego pliku
        a. Górne menu -> Run -> Run... -> Doctest in about_setup_doctest
        b. Prawy przycisk myszy -> Run 'Doctests in about_setup_doctest'
    3. Wszystkie testy muszą przechodzić
    4. Zwróć uwagę na linijkę z komentarzem `# doctest: +NORMALIZE_WHITESPACE`
        a. To jest tzw. flaga sterująca doctest
        b. Pozwala na zignorowanie łamań linii i spacji w listach, tuplach, dictach, itp
        c. Spróbuj usunąć ten zapis (nie modyfikuj wyniku) i zobacz czy testy nadal przechodzą
    5. Zapisz `100%` we współdzielonym arkuszu kalkulacyjnym w wierszu zadania

Tests:
    >>> type(firstname)
    <class 'str'>
    >>> type(lastname)
    <class 'str'>
    >>> f'{firstname} {lastname}'
    'Mark Watney'
    >>> firstname + lastname
    'MarkWatney'
    >>> firstname + ' ' + lastname
    'Mark Watney'
    >>> [firstname] + [lastname]
    ['Mark', 'Watney']
    >>> [firstname] + [lastname] # doctest: +NORMALIZE_WHITESPACE
    ['Mark',
     'Watney']
    >>> name = 'Mark Watney'
    >>> print(name)
    Mark Watney
    >>> if True:
    ...     print('ok')
    ... else:
    ...     print('not ok')
    ...
    ok
"""


# Given
firstname = 'Mark'
lastname = 'Watney'


# Solution
firstname = 'Mark'
lastname = 'Watney'
