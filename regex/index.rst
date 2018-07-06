*******************
Wyrażenia regularne
*******************


Konstruowanie wyrażeń
=====================

Regular Expression Syntax
-------------------------
.. csv-table:: Regular Expression Syntax
    :header-rows: 1
    :file: data/re-syntax.csv
    :widths: 25, 75

Wizualizacja regexpów
---------------------
* https://regexper.com/
* https://regex101.com/

.. figure:: img/regexp-vizualization.png
    :name: figure-regexp-vizualization
    :scale: 100%
    :align: center


Najczęściej wykorzystywane funkcje
==================================

``re.match()``
--------------
.. literalinclude:: src/re-match.py
    :name: listing-re-match
    :language: python
    :caption: Usage of ``re.match()``

``re.search()``
---------------
.. literalinclude:: src/re-search.py
    :name: listing-re-search()
    :language: python
    :caption: Usage of ``re.search()``

``re.findall()`` and ``re.finditer()``
--------------------------------------
.. literalinclude:: src/re-find.py
    :name: listing-re-find
    :language: python
    :caption: Usage of ``re.findall()`` and ``re.finditer()``

``re.compile()``
----------------
.. literalinclude:: src/re-compile.py
    :name: listing-re-compile
    :language: python
    :caption: Usage of compile

``re.sub()``
------------
.. literalinclude:: src/re-sub.py
    :name: listing-re-sub
    :language: python
    :caption: Usage of ``re.sub()``

``re.split()``
--------------
.. literalinclude:: src/re-split.py
    :name: listing-re-split
    :language: python
    :caption: Usage of ``re.split()``


Regex Flags
===========
.. csv-table:: Regular Expression Flags
    :header-rows: 1
    :file: data/re-flags.csv
    :widths: 25, 75

.. literalinclude:: src/re-multiline.py
    :name: listing-re-regexp
    :language: python
    :caption: Usage of regexp


Wyciąganie parametrów (zmiennych)
=================================
.. literalinclude:: src/re-group.py
    :name: listing-re-group
    :language: python
    :caption: Usage of group in ``re.match()``


Greedy i non-greedy search
==========================
The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible. Sometimes this behaviour isn’t desired; if the RE <.*> is matched against '<a> b <c>', it will match the entire string, and not just '<a>'. Adding ? after the qualifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched. Using the RE <.*?> will match only '<a>'.

.. literalinclude:: src/re-greedy.py
    :name: listing-re-greedy
    :language: python
    :caption: Usage of greedy and non-greedy search in ``re.findall()``


Practical example of Regex usage
================================

Making a Phonebook
------------------
.. literalinclude:: src/re-example-1.py
    :name: listing-re-example-1
    :language: python
    :caption: Practical example of Regex usage

Finding all Adverbs
-------------------
.. literalinclude:: src/re-example-2.py
    :name: listing-re-example-2
    :language: python
    :caption: Finding all Adverbs

Writing a Tokenizer
-------------------
.. literalinclude:: src/re-example-3.py
    :name: listing-re-example-3
    :language: python
    :caption: Writing a Tokenizer.


Assignments
===========

Walidacja PESEL
---------------
Za pomocą wyrażeń regularnych sprawdź:

* czy pesel jest poprawny
* jaka jest data urodzenia? (podaj obiekt ``datetime.date``
* płeć użytkownika który podał PESEL


:Założenia:
    * Nazwa pliku: ``regex_pesel.py``
    * Linii kodu do napisania: około 10 linii
    * Maksymalny czas na zadanie: 20 min

:Z gwiazdką:
    * sprawdź walidację numerów PESEL dla osób urodzonych po 2000 roku.
    * sprawdź sumę kontrolną
