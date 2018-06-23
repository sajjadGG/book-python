*********************
About Python Language
*********************


What is Python?
===============
* Python - język programowania wysokiego poziomu ogólnego przeznaczenia
* Rozbudowany pakiet bibliotek standardowych
* Ideą przewodnią jest czytelność i klarowność kodu źródłowego
* Jego składnia cechuje się przejrzystością i zwięzłością
* Python wspiera różne paradygmaty programowania: obiektowy, imperatywny oraz funkcyjny.
* Posiada w pełni dynamiczny system typów i automatyczne zarządzanie pamięcią.
* Podobnie jak inne języki dynamiczne jest często używany jako język skryptowy.
* Interpretery Pythona są dostępne na wiele systemów operacyjnych.
* Python rozwijany jest jako projekt Open Source zarządzany przez Python Software Foundation, która jest organizacją non-profit.


Which version?
==============
* newest Python 3

Python kilka lat temu przeszedł drastyczną transformację. Projekt Python 3 miał całkowicie zmienić sposób w jaki kompilator traktuje kod źródłowy. Dotychczas wszystkie ciągi znaków traktowane były jako ciągi ASCII. Od teraz miało to ulec zmianie a konto popularnego na całym świecie kodowania UTF-8. Wcześniej, aby skorzystać z takiego zachowania należało przed stringiem umieścić literkę "u", np. ``u'Hello World!'`` aby kompilator zrozumiał kodowanie. Niestety nie było to domyślne kodowanie i z tego powodu konieczne było ciągłe żonglowanie funkcjami ``.encode()`` i ``.decode()``.

Ponadto w nowym języku Python 3 (czasami zwanym Python 3k [3k = 3000] aby pokazać, że drastycznie się różni od wersji 2) scalono niektóre moduły biblioteki standardowej oraz zmieniono zachowanie niektórych funkcji w tym bardzo często wykorzystywanej ``print()``, która wcześniej była słowem kluczowym w języku.

Jeżeli rozpoczynasz naukę programowania wybierz nowego Pythona 3. Jeżeli tworzysz nowy projekt wybierz podobnie. Na chwilę obecną jedynym uzasadnieniem wyboru starszej wersji jest niekompatybilność niektórych bibliotek i projektów zewnętrznych. Na szczęście z miesiąca na miesiąc lista projektów "Python 3 compliant" wzrasta i wybór pozostaje coraz bardziej oczywisty.

Ostatnią wersją gałęzi 2 jest 2.7. Wersja ta zawiera elementy i składnię ułatwiające konwersję programów do nowego środowiska i pozwala na pisanie aplikacji i skryptów, które powinny uruchomić się zarówno przy wykorzystaniu interpretera ``python2`` jak i ``python3``. Wersja 2.7 jest ostatnią z rodziny 2 i będą do niej wypuszczane jedynie poprawki bezpieczeństwa.


File types and extensions
=========================
* Pliki źródłowe języka Python mają rozszerzenie ``.py``.
* Podczas wytwarzania oprogramowania spotkasz się jeszcze z kilkoma innymi rozszerzeniami.
* Mogą to być:

    * ``.pyc`` - plik zawiera tzw. bytecode czyli efekt kompilacji kodu źródłowego. Python tworzy te pliki podczas kompilacji jeżeli nic nie zmienimy w naszym kodzie źródłowym, wykorzystuje je bez potrzeby analizowania i kompilowania kodu ponownie. Od wersji 3.2 pliki ``.pyc`` znajdują się w specjalnym katalogu o nazwie ``__pycache__``.

    * ``.pyd`` - Windowsowy plik ze skompilowanym kodem Pythona w formie biblioteki DLL.

    * ``.pyw`` - Windowsowy plik z kodem źródłowym. Takie pliki odpalane są za pomocą polecenia ``pythonw.exe``

    * ``.pyx`` - Źródło cPythona, które będzie przekonwertowane do C/C++

    * ``.pyz`` - Python 3.5 wprowadził możliwość tworzenia Python ZIP Archive. Takie spakowane archiwum zawiera wszystkie pliki niezbędne do uruchomienia programu. Rozszerzenie dla obiektów tego typu jest ``.pyz``. Do pakowania służy biblioteka `zipapp <https://docs.python.org/3/library/zipapp.html>`_.


Read–Eval–Print Loop
====================
Python spopularyzował wykorzystanie tzw. interpretera REPL (read–eval–print loop). REPL to interaktywny interpreter poleceń wykonujący wyrażenia z języka (zwykle linie), których wyniki są wyświetlane użytkownikowi natychmiast po ich wykonaniu. W uproszczeniu można powiedzieć, że REPL jest to linia poleceń programu ``python``. Znakiem zachęty do wprowadzania tekstu takiego programu są trzy znaki większości ``>>>``. Polecenia wpisane po tych znaczkach są interpretowane i natychmiast wykonywane. Ich wynik przedstawiany jest w następnej linijce. Jeżeli wykorzystamy konstrukcję, która wymaga więcej niż jednej linii, każda kolejna linijka będzie poprzedzona trzema kropkami ``...``. Przykłady takiej interakcji zobaczymy przy omawianiu "Hello World".

Rozwiązanie REPL idealnie pasuje do szybkiego testowania składni oraz funkcjonalności programów i bibliotek. Dzięki REPL jesteśmy w stanie przeprowadzić interaktywną sesję z linią poleceń a po przetestowaniu rozwiązania wkleić działające linie do naszego skryptu. Taki styl znacząco przyspiesza development i debugging.

Uproszczoną implementację takiego rozwiązania można przedstawić w następujący sposób:

.. code-block:: python

    while True:
        command = raw_input('>>> ')
        output = eval(command)
        print(output)

W dalszej części omówimy poszczególne elementy, które są tu wymienione.

Skrypty czy programy tego typu nie mają na celu pokazania jak minimalną ilością znaków da się wyświetlić coś na ekranie, a sposób interakcji i przepływu programista-komputer.
W Pythonie mamy możliwość wykorzystania interpretera REPL, przykład poniżej oraz stworzenia skryptu, który wykonamy z linii poleceń.

.. code-block:: console

    $ python

    Python 3.6.0 (default, Dec 24 2016, 08:01:42)
    [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.

    >>> print('Ehlo World!')
    Ehlo World!

Zwróć uwagę na wersję Pythona.
Jeżeli po wpisaniu polecenia ``python`` uruchomi się wersja 2.x, możesz spróbować polecenia ``python3``

Powyższy przykład ilustruje moment wpisania polecenia ``python``.
Standardowy tekst informujący o wersji i kompilacji języka oraz znak zachęty ``>>>`` (ang. prompt).
Polecenia wpisujemy po tym znaku a ich wynik wyświetla się poniżej (i nie zawiera wcięcia).
Dalej w materiałach będziemy posługiwali się już samym znakiem zachęty.

Scripts
=======
Drugim sposobem jest stworzenie skryptu posiadającego następujące linie.
Ta metoda przydaje nam się gdy nasze programy zaczną rosnąć na więcej niż jedną dwie linijki.
Warto zwrócić uwagę na pierwszą linię, na tzw. shebang ``#!`` i następujące po nim polecenie.
To jest deklaracja programu, którego kod źródłowy znajduje się poniżej.
Linijka ta jest opcjonalna, ale dla zachowania poprawności i warto w naszych skryptach coś takiego zadeklarować.
Już po pierwszej linii widzimy, że skrypt będzie zinterpretowany jako kod źródłowy trzeciej wersji Pythona.

.. code-block:: python

    #!/usr/bin/env python3

    print('Ehlo World!')

Wynik uruchomienia powyższego skryptu będzie identyczny z efektem uzyskanym w REPL, tzn, na naszym ekranie ukaże się napis ``Ehlo World``.
Dla wszystkich, którzy potrzebują wiedzieć jak wygląda najmniejszy kod, który wyświetli nam te słowa polecam poniższy kod.

.. code-block:: python

    print('Ehlo World!')

Interpreter declaration
-----------------------
Jest to specjalny rodzaj komentarza który opisaliśmy pokrótce powyżej. Ten typ komentarza występuje tylko w pierwszej linii programu i definiuje interpreter kodu źródłowego dla kodu poniżej.

.. code-block:: bash

    #!/usr/bin/env python3

PATH
----

PYTHON_PATH
-----------
