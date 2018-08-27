****************************************
IDE - Integrated Development Environment
****************************************


What is IDE?
============
* Refactoring
* Syntax helping and highlighting
* Type hinting and checking
* VCS support
* Virtualenv support
* Debugging
* Spell checking
* Running code and inspections


How to choose?
==============
* Do edycji skryptów Pythona wystarczy sam Notatnik.
* Kod źródłowy jest na tyle czytelny i prosty, że bardzo łatwo będziemy w stanie poradzić sobie z prostymi skryptami bez jakiejkolwiek pomocy od zaawansowanego edytora.
* W miarę rośnięcia złożoności projektu oraz ilości plików przyda nam się coś co ułatwi nam pracę.
* Wybór edytora to temat wielce kontrowersyjny.
* Od kilku dziesięcioleci w środowisku programistów jest prowadzona wojna między minimalistycznym VIMem oraz posiadającym ogromne możliwości EMACSem.
* Jeden i drugi edytor wspaniale posłuży nam do pisania skryptów w Pythonie i po odpowiedniej konfiguracji lub instalacji pluginów podpowie składnię.
* Po przetestowaniu kilkunastu środowisk IDE zaprzyjaźniłem się z edytorem PyCharm.
* PyCharm ma dwie wersję płatną oraz darmową.
* Wersja darmowa w zupełności nam wystarczy.
* Ciekawą alternatywą może być PyDev - plugin do środowiska Eclipse.
* W poniższych materiałach będę posługiwał się kodem źródłowym, który wykonywany jest przez interpreter i nie ma znaczenia z jakiego IDE skorzystasz.


Which one is the best?
======================
#. PyCharm Professional EAP
#. PyCharm Community
#. PyCharm Professional
#. PyDev

* https://www.jetbrains.com/pycharm/download/
* http://www.pydev.org/download.html


Assignments
===========

Create Project from VCS
-----------------------
#. Prowadzący poda Ci link do repozytorium na ``github.com``
#. Stwórz projekt pobierając kod z GIT
#. Upewnij się, że jest plik ``.gitconfig`` oraz ma wpisaną linię ``.idea/``

Know thou IDE
-------------
#. Po stworzeniu projektu, załóż katalog o nazwie jak twoje nazwisko
#. WAŻNE: Już do końca książki będziesz w nim tworzył wszystkie rozwiązania do zadań
#. Skonfiguruj aby używać ``venv``
#. Jak zrobić w Twoim IDE:

    * Run in console
    * Run...
    * Debug...
    * Python Console
    * Terminal
    * Full Screen
    * Distraction Free Mode
    * Reformat Code

#. Jakie są skróty klawiszowe do poszczególnych opcji?
#. Czym się różni ``Run...`` od ``Debug...```?
#. Czym się różni ``Python Console`` od ``Terminal``
#. Czym się różni ``Distraction Free Mode`` od ``Full Screen``

:About:
    * Lines of code to write: 0 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Korzystanie z IDE
    * Uruchamianie debuggera
    * Znajomość różnicy między uruchamianiem i debuggingiem
    * Znajomość różnicy między terminalem i konsolą

Spellchecker
------------
#. Zainstaluj plugin 'Hunspell'
#. Pobierz z https://github.com/LibreOffice/dictionaries słownik ``.dic`` oraz ``.aff`` dla języka polskiego
#. Skonfiguruj IDE do korzystania z tego słownika

:About:
    * Lines of code to write: 0 lines
    * Estimated time of completion: 3 min

:The whys and wherefores:
    * Korzystanie z IDE
    * Konfiguracja IDE
