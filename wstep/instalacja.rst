**********
Instalacja
**********


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


Instalacja
==========


Windows
-------

Aby zainstalować Python na środowisku Windows należy pobrać instalator z python.org a następnie przejść przez wszystkie kroki kreatora.
Po instalacji należy wylogować się i zalogować ponownie aby odświeżyć zmienną PATH. Po tym procesie w Windowsowej liście poleceń (cmd) będzie dostępny program ``python``.
Ponadto wraz z instalacją Pythona na Twoim komputerze zainstaluje się edytor Idle, który w początkowej fazie nauki tworzenia oprogramowania powinien nam w zupełności wystarczyć.


OS X
----

Jeżeli posiadasz OS X to Python powinien być domyślnie zainstalowany na Twoim komputerze. Apple w najnowszych systemach operacyjnych standardowo dostarcza Pythona w wersji 2.7 i 2.6. Domyślnie po wpisaniu polecenia ``python`` uruchamiany jest 2.7. Aby zainstalować Pythona w wersji 3 możemy skorzystać z managera pakietów ``brew`` albo z tzw. macports. Osobiście polecam to pierwsze podejście. Brew dostępny jest za darmo i można pobrać go z internetu uruchamiając polecenie ze strony `Brew <http://brew.sh>`_. Najpierw jednak konieczne będzie zainstalowanie najnowszej wersji Xcode z AppStore. Brew powinien zrobić to za Ciebie.

Sama instalacja brew sprowadza do uruchomienia polecenia wyglądającego jak następujące:

.. code:: console

    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Następnie po instalacji:

.. code:: console

    $ brew install python3

I już możemy cieszyć się najnowszym Pythonem.


Linux
-----

Niemalże wszystkie dystrybucje Linuxa posiadają zainstalowaną wersję Pythona w wersji 2. Aby zainstalować trójkę użyj swojego managera pakietów ``apt-get``, ``yum`` czy ``emerge`` czy ``rpm`` w zależności od dystrybucji.


PYTHON_PATH
===========
