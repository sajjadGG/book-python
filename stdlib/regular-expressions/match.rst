************
Regexp Match
************


About
=====
* ``re.match()``
* Checks exact match
* Checking if user input is correct (email, url, NIP, VAT ID, PESEL)


Examples
========
.. code-block:: python
    :caption: Usage of ``re.match()``

    import re


    def is_valid_email(email: str) -> bool:
        PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'

        if re.match(PATTERN, email):
            return True
        else:
            return False


    is_valid_email('mark.watney@nasa.gov')     # True
    is_valid_email('mark.watney@nasa.g')       # False


Good Engineering Practices
==========================
* Doctests

.. code-block:: python
    :caption: Doctests

    import re


    def is_valid_email(email: str) -> bool:
        """Function check email address against Regular Expression
        >>> is_valid_email('jose.jimenez@nasa.gov')
        True
        >>> is_valid_email('José.Jiménez@nasa.gov')
        True
        >>> is_valid_email('+jose.jimenez@nasa.gov')
        False
        >>> is_valid_email('jose.jimenez+@nasa.gov')
        True
        >>> is_valid_email('jose.jimenez+newsletter@nasa.gov')
        True
        >>> is_valid_email('jose.jimenez@.gov')
        False
        >>> is_valid_email('@nasa.gov')
        False
        >>> is_valid_email('jose.jimenez@nasa.g')
        False
        """
        PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'

        if re.match(PATTERN, email):
            return True
        else:
            return False


Assignments
===========

Regexp Match Phones
-------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/regexp_match_phones.py`

:English:
    #. Use data from "Input" section (see below)
    #. Use regular expressions to validate phone numbers
    #. Check all given numbers (see input section)
    #. Valid phone number formats:

        * Easy version: ``+## ### ### ###``
        * Harder version: ``+## ### ### ###`` or ``+## ## ### ####``

    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Użyj wyrażeń regularnych do walidacji numeru telefonu
    #. Sprawdź wszystkie podane numery (patrz sekcja input)
    #. Poprawne formaty numeru:

        * Wersja łatwa: ``+## ### ### ###``
        * Wersja trudniejsza: ``+## ### ### ###`` lub ``+## ## ### ####``

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            '+48 (12) 355 5678',
            '+48 123 555 678',
            '123 555 678',
            '+48 12 355 5678',
            '+48 123-555-678',
            '+48 123 555 6789',
            '+1 (123) 555-6789',
            '+1 (123).555.6789',
            '+1 800-python',
            '+48123555678',
            '+48 123 555 678 wew. 1337',
            '+48 123555678,1',
            '+48 123555678,1,2,3',
        ]

        for number in DATA:
            result = is_valid_phone(number)
            print(f'{result}\t{number}')

:Output:
    .. code-block:: text

        False	+48 (12) 355 5678
        True	+48 123 555 678
        False	123 555 678
        True	+48 12 355 5678
        False	+48 123-555-678
        False	+48 123 555 6789
        False	+1 (123) 555-6789
        False	+1 (123).555.6789
        False	+1 800-python
        False	+48123555678
        False	+48 123 555 678 wew. 1337
        False	+48 123555678,1
        False	+48 123555678,1,2,3

Regexp Match Git Flow
---------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/regexp_match_gitflow.py`

:English:
    #. Use regular expressions to validate Git branch names
    #. Check all given branch names (see input section)
    #. Branch names should comply with Git Flow convention:

    #. Where:

        * ``release/major.minor`` - major and minor are unsigned integers
        * ``feature/``, ``bugfix/``, ``hotfix/`` - branch prefixes
        * ``prefix/ISSUEKEY-NUMBER-summary``
        * ``ISSUEKEY`` - uppercase, only ASCII letters, minimum 2 characters, not longer than 10
        * ``NUMBER`` - positive integer, maximal 5 digits
        * ``summary`` - lowercase, ASCII letters and numbers, dashes instead whitespaces, not longer than 30
        * ``pull-request/NUMBER`` - positive integer, maximal 5 digits

    #. Example of valid branches:

        * ``master``
        * ``develop``
        * ``release/1.0``
        * ``feature/ID-1337-some-new-feature``
        * ``bugfix/ID-1337-fixing-old-bug``
        * ``hotfix/ID-1337-bug-on-production``
        * ``pull-request/42``


:Polish:
    #. Użyj wyrażeń regularnych do walidacji nazwy gałęzi w Git
    #. Sprawdź wszystkie dane nazwy gałęzi (patrz sekcja input)
    #. Nazwy gałęzi powinny stosować się do konwencji Git Flow:

        * ``release/major.minor`` - major i minor nieujemne liczby całkowite
        * ``feature/``, ``bugfix/``, ``hotfix/`` - prefiks nazwy gałęzi
        * ``prefix/ISSUEKEY-NUMBER-summary``
        * ``ISSUEKEY`` - duże litery, tylko litery ASCII, minimum 2 znaki, nie więcej niż 10
        * ``NUMBER`` - dodatnia liczba całkowita, maksymalnie 5 cyfr
        * ``summary`` - małe litery, litery ASCII i liczby, myślniki zamiast białych spacji, nie dłuższa niż 30
        * ``pull-request/NUMBER`` - dodatnia liczba całkowita, maksymalnie 5 cyfr

    #. Przykład poprawnych gałęzi:

        * ``master``
        * ``develop``
        * ``release/1.0``
        * ``feature/ID-1337-some-new-feature``
        * ``bugfix/ID-1337-fixing-old-bug``
        * ``hotfix/ID-1337-bug-on-production``
        * ``pull-request/42``

