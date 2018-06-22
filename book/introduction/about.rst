*********************
About Python Language
*********************


Co to jest Python
=================
* Python - język programowania wysokiego poziomu ogólnego przeznaczenia
* Rozbudowany pakiet bibliotek standardowych
* Ideą przewodnią jest czytelność i klarowność kodu źródłowego
* Jego składnia cechuje się przejrzystością i zwięzłością
* Python wspiera różne paradygmaty programowania: obiektowy, imperatywny oraz funkcyjny.
* Posiada w pełni dynamiczny system typów i automatyczne zarządzanie pamięcią.
* Podobnie jak inne języki dynamiczne jest często używany jako język skryptowy.
* Interpretery Pythona są dostępne na wiele systemów operacyjnych.
* Python rozwijany jest jako projekt Open Source zarządzany przez Python Software Foundation, która jest organizacją non-profit.


Historia Pythona
================

Guido
-----
Pythona stworzył we wczesnych latach 90. Guido van Rossum - jako następcę języka ABC, stworzonego w Centrum voor Wiskunde en Informatica (CWI – Centrum Matematyki i Informatyki w Amsterdamie). Van Rossum jest głównym twórcą Pythona, choć spory wkład w jego rozwój pochodzi od innych osób. Z racji kluczowej roli, jaką van Rossum pełni przy podejmowaniu ważnych decyzji projektowych, często określa się go przydomkiem "Benevolent Dictator for Life" (BDFL).

Name
----
Nazwa języka nie pochodzi od zwierzęcia, jak można przypuszczać. Python pochodzi od serialu komediowego emitowanego w latach siedemdziesiątych przez BBC. Ten serial nosi nazwę "Monty Python's Flying Circus" (Latający Cyrk Monty Pythona). Projektant potrzebował nazwy, która była krótka, unikalna i nieco tajemnicza. Na dodatek był fanem serialu, więc uważał, że taka nazwa dla języka była świetna.

History
-------
Wersja 1.2 była ostatnią wydaną przez CWI. Od 1995 roku Van Rossum kontynuował pracę nad Pythonem w Corporation for National Research Initiatives (CNRI) w Reston w Wirginii, gdzie wydał kilka wersji Pythona, do 1.6 włącznie. W 2000 roku van Rossum i zespół pracujący nad rozwojem jądra Pythona przenieśli się do BeOpen.com by założyć zespół BeOpen PythonLabs. Pierwszą i jedyną wersją wydaną przez BeOpen.com był Python 2.0.

Po wydaniu wersji 1.6 i opuszczeniu CNRI przez van Rossuma, który zajął się programowaniem komercyjnym, uznano za wysoce pożądane, by Pythona można było używać z oprogramowaniem dostępnym na licencji GPL. CNRI i Free Software Foundation (FSF) podjęły wspólny wysiłek w celu odpowiedniej modyfikacji licencji Pythona. Wersja 1.6.1 była zasadniczo identyczna z wersją 1.6, z wyjątkiem kilku drobnych poprawek oraz licencji, dzięki której późniejsze wersje mogły być zgodne z licencją GPL. Python 2.1 pochodzi zarówno od wersji 1.6.1, jak i 2.0.

Po wydaniu Pythona 2.0 przez BeOpen.com Guido van Rossum i inni programiści z PythonLabs przeszli do Digital Creations. Cała własność intelektualna dodana od tego momentu, począwszy od Pythona 2.1 (wraz z wersjami alpha i beta), jest własnością Python Software Foundation (PSF), niedochodowej organizacji wzorowanej na Apache Software Foundation.

.. note:: Fragment pochodzi z serwisu `Wikipedia <https://pl.wikipedia.org/wiki/Python>`_.


Rozszerzenia plików Pythona
===========================
Pliki źródłowe języka Python mają rozszerzenie ``.py``.
Podczas wytwarzania oprogramowania spotkasz się jeszcze z kilkoma innymi rozszerzeniami.
Mogą to być:

* ``.pyc`` - plik zawiera tzw. bytecode czyli efekt kompilacji kodu źródłowego. Python tworzy te pliki podczas kompilacji jeżeli nic nie zmienimy w naszym kodzie źródłowym, wykorzystuje je bez potrzeby analizowania i kompilowania kodu ponownie. Od wersji 3.2 pliki ``.pyc`` znajdują się w specjalnym katalogu o nazwie ``__pycache__``.

* ``.pyd`` - Windowsowy plik ze skompilowanym kodem Pythona w formie biblioteki DLL.

* ``.pyw`` - Windowsowy plik z kodem źródłowym. Takie pliki odpalane są za pomocą polecenia ``pythonw.exe``

* ``.pyx`` - Źródło cPythona, które będzie przekonwertowane do C/C++

* ``.pyz`` - Python 3.5 wprowadził możliwość tworzenia Python ZIP Archive. Takie spakowane archiwum zawiera wszystkie pliki niezbędne do uruchomienia programu. Rozszerzenie dla obiektów tego typu jest ``.pyz``. Do pakowania służy biblioteka `zipapp <https://docs.python.org/3/library/zipapp.html>`_.


Którego wersję wybrać?
======================
Python kilka lat temu przeszedł drastyczną transformację. Projekt Python 3 miał całkowicie zmienić sposób w jaki kompilator traktuje kod źródłowy. Dotychczas wszystkie ciągi znaków traktowane były jako ciągi ASCII. Od teraz miało to ulec zmianie a konto popularnego na całym świecie kodowania UTF-8. Wcześniej, aby skorzystać z takiego zachowania należało przed stringiem umieścić literkę "u", np. ``u'Hello World!'`` aby kompilator zrozumiał kodowanie. Niestety nie było to domyślne kodowanie i z tego powodu konieczne było ciągłe żonglowanie funkcjami ``.encode()`` i ``.decode()``.

Ponadto w nowym języku Python 3 (czasami zwanym Python 3k [3k = 3000] aby pokazać, że drastycznie się różni od wersji 2) scalono niektóre moduły biblioteki standardowej oraz zmieniono zachowanie niektórych funkcji w tym bardzo często wykorzystywanej ``print()``, która wcześniej była słowem kluczowym w języku.

Jeżeli rozpoczynasz naukę programowania wybierz nowego Pythona 3. Jeżeli tworzysz nowy projekt wybierz podobnie. Na chwilę obecną jedynym uzasadnieniem wyboru starszej wersji jest niekompatybilność niektórych bibliotek i projektów zewnętrznych. Na szczęście z miesiąca na miesiąc lista projektów "Python 3 compliant" wzrasta i wybór pozostaje coraz bardziej oczywisty.

Ostatnią wersją gałęzi 2 jest 2.7. Wersja ta zawiera elementy i składnię ułatwiające konwersję programów do nowego środowiska i pozwala na pisanie aplikacji i skryptów, które powinny uruchomić się zarówno przy wykorzystaniu interpretera ``python2`` jak i ``python3``. Wersja 2.7 jest ostatnią z rodziny 2 i będą do niej wypuszczane jedynie poprawki bezpieczeństwa.


Który interpreter?
==================
Sam Python jest tak naprawdę tylko specyfikacją składni oraz wyglądu biblioteki standardowej. Python ma obecnie kilka interpreterów z których najbardziej popularny jest cPython, który jest wydawany razem z nową wersją specyfikacji języka.

cPython
-------
Domyślną wersją Pythona jest cPython. Jest to tzw. implementacja wzorcowa i to jej kompilator jest wydawany wraz ze specyfikacją nowych funkcjonalności przy każdym wydaniu Python. Sam kompilator jest rozwijany w języku C. cPython jest najbardziej popularną dystrybucją z wszystkich wydań. W poniższych materiałach to właśnie z tej wersji będziemy korzystać.

PyPy
----
Bardzo ciekawy projekt napisania interpretera Pythona w... Pythonie. Kompilator dokonuje bardzo wielu niskopoziomowych optymalizacji dlatego ta wersja języka jest wyjątkowo szybka. Niestety nie wszystkie biblioteki zewnętrzne są z nią kompatybilne. Nie mniej projekt jest wciąż aktywnie rozwijany przez bardzo pomysłowych programistów i stanowi solidną alternatywę dla cPythona. Niektóre programy przy wykorzystaniu PyPy potrafią przyspieszyć kilkuset do kilkutysiąc krotnie.

IronPython
----------
Próba implementacji języka Python wykorzystując platformę .NET firmy Microsoft. Dzięki temu język bardzo dobrze integruje się z całym środowiskiem.

Jython
------
Próba implementacji języka Python wykorzystując platformę wirtualnej maszyny JAVA (JVM). Projekt bardzo obiecujący lecz niestety ostatnio słabo rozwijany. JVM stanowi bardzo dobrą platformę dobrze "wygrzaną" oraz poznaną pod względem wydajnościowym jak i środowiska developerskiego.

Inne
----
W internecie jest dostępnych jeszcze więcej implementacji języka. Niektóre projekty są jeszcze rozwijane, niektóre (Stackless Python) weszły w skład lub transformowały się w wyżej wymienionych lub zostały zarzucone (Unleaden Swallow).


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


Duck typing
===========
W językach programowania można doszukać się wielu systemów typowania. System typowania informuje kompilator o obiekcie oraz o jego zachowaniach. Ponadto niesie za sobą informację na temat ilości pamięci, którą trzeba dla takiego obiektu zarezerwować. Istnieje nawet cała gałąź zajmująca się systemami typów. Obecnie najczęściej wykorzystywane języki programowania dzielą się na statycznie - silnie typowane (JAVA, C, C++ i pochodne) oraz dynamicznie - słabo typowane (Python, Ruby, PHP itp.). Oczywiście mogą znaleźć się rozwiązania hybrydowe oraz z tzw. inrefencją typów itp.

W naszym przypadku skupmy się na samym mechanizmie dynamicznego typowania. Określenie to oznacza, że język nie posiada typów zmiennych i obiektów, które jawnie trzeba deklarować. Inicjując zmienną nie musimy powiedzieć, że jest to ``int``. Co więcej po chwili do tej zmiennej możemy przypisać dowolny obiekt, np. łańcuch znaków i kompilator nie powie nam złego słowa. Kompilator podczas działania oprogramowania niejawnie może zmienić typ obiektu i dokonać na nim konwersji.

Wśród programistów popularne jest powiedzenie "jeżeli chodzi jak kaczka i kwacze jak kaczka, to musi być to kaczka". Od tego powiedzenia wzięła się nazwa Duck typing. Określenie to jest wykorzystywane w stosunku do języków, których typy obiektów rozpoznawane są po metodach, które można na nich wykonać. Nie zawsze takie zgadywanie jest celne i jednoznacznie i precyzyjnie określa typ. Może się okazać, że obiekt np. ``Samochód`` posiada metody ``uruchom_silnik()`` i ``jedz_prosto()`` podobnie jak ``Motor``. Jeden i drugi obiekt będzie zachowywał się podobnie. Języki wykorzystujące ten mechanizm wykorzystują specjalne metody porównawcze, które jednoznacznie dają informację kompilatorowi czy dwa obiekty są równe.

Sam mechanizm dynamicznego typowania jest dość kontrowersyjny, ze względu na możliwość bycia nieścisłym. W praktyce okazuje się, że rozwój oprogramowania wykorzystującego ten sposób jest dużo szybszy. Za to zwolennicy statycznego typowania, twierdzą, że projekty wykorzystujące duck typing są trudne w utrzymaniu po latach. Celem tego dokumentu nie jest udowadnianie wyższości jednego rozwiązania nad drugim. Zachęcam jednak do zapoznania się z wykładem "The Unreasonable Effectiveness of Dynamic Typing for Practical Programs", którego autorem jest "Robert Smallshire". Wykład zamieszczonym został w serwisie InfoQ (http://www.infoq.com/presentations/dynamic-static-typing). Wykład w ciekawy sposób dotyka problematyki porównania tych dwóch metod systemu typów. Wykład jest o tyle ciekawy, że bazuje na statystycznej analizie projektów umieszczonych na https://github.com a nie tylko bazuje na domysłach i flamewar jakie programiści lubią prowadzić.

Wszystko jest obiektem
----------------------
W Pythonie wszystkie rzeczy są obiektem. Każdy element posiada swoje metody, które możemy na nim uruchomić. W dalszej części tych materiałów będziemy korzystali z polecenia ``help()`` aby zobaczyć jakiego z jakiego typu obiektem mamy okazję pracować oraz co możemy z nim zrobić.
