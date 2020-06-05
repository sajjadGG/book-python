#######################################
Python 3: From None to Machine Learning
#######################################


:Original Title: Python 3: from None to Machine Learning
:English Title: Python 3: from None to Machine Learning
:Author: Matt Harasymczuk
:Language: English
:ISBN: 978-83-957186-2-5
:Year: 2019-2020
:Online Access: https://python.astrotech.io
:License: Creative Commons Attribution-ShareAlike 4.0 International License


Author
======
.. figure:: /_static/AstroMatt.jpg
    :align: left
    :scale: 39%

.. csv-table::
    :widths: 15, 65

    "author", "`Matt Harasymczuk <https://www.astronaut.center>`_"
    "email", "book-python@astronaut.center"
    "www", "https://www.astronaut.center"
    "github", "https://github.com/astromatt"
    "linkedin", "https://linkedin.com/in/mattharasymczuk"
    "facebook", "https://facebook.com/matt.harasymczuk"
    "slideshare", "https://www.slideshare.net/astrotech/presentations"

.. csv-table:: Other Books from Author. More information at https://www.astronaut.center/books
    :widths: 25, 20, 55
    :header: "ISBN", "Online Access", "Title"

    "9788395718625", "https://python.astrotech.io", "Python 3: from None to Machine Learning"
    "9788395718632", "https://dev.astrotech.io", "The Software Engineering: DevOps, CI/CD, Docker, Provisioning and Git Flow"
    "9788395718601", "https://www.astronaut.pl", "Astronaut Selection and Training for Long Duration Spaceflight and Extraterrestrial Activity"
    "9788395675201", "https://www.astronaut.center/books", "Space in Practice: How to Prepare and Conduct Stratospheric Balloon Mission"
    "9788395718649", "https://pl.habitatos.space", "HabitatOS - Development of operating system prototype for Lunar and Martian habitats"
    "9788395718618", "https://alsep.astronaut.center", "Geophysics experiments from Apollo Lunar Surface Experiments Package"


Note
====
* For consulting or training course requests please email book-python@astronaut.center
* Before training course please setup your environment as described here :ref:`Install`.


.. _Install:

Install
=======
#. Można korzystać ze swojego komputera i dowolnego systemu operacyjnego
#. Materiały szkoleniowe dostosowane są do Python 3.7 i 3.8 (nowsza wersja jest preferowana)
#. Python może być zainstalowany albo za pomocą oficjalnej dystrybucji albo z pakietu Anaconda
#. Wybór dystrybucji Python nie będzie miał wpływu na przebieg szkolenia
#. Podczas szkolenia trener będzie korzystał z PyCharm jako środowisko programistyczne (IDE)
#. Można korzystać z innego IDE, ale proszę zaznajomić się z nim przed szkoleniem
#. Niestety nie będzie czasu na rozwiązywanie problemów technicznych z IDE
#. Podczas instalacji PyCharm zaznacz opcję: "powiąż z rozszerzeniem plików ``.py``" (nie jest to konieczne ale ułatwia pracę)
#. Proszę o zainstalowanie Git i założenie darmowego konta na Github oraz potwierdzenie linka aktywacyjnego na mailu
#. Odnośniki do pobierania oprogramowania:

    * Python: https://www.python.org/downloads/
    * Git: https://git-scm.com/download/
    * PyCharm: https://www.jetbrains.com/pycharm/download/

#. Dla szkolenia z Analizy Numerycznej lub Machine Learning dodatkowo trzeba:

    * Posiadać uprawnienia na komputerze do instalacji pakietów Python za pomocą ``pip``
    * Do instalacji pakietów konieczny jest dostęp do internetu (zapewniany przez organizatora szkolenia)
    * Instalacja: ``pip3 install --upgrade jupyter numpy pandas matplotlib scikit-learn statsmodels seaborn bokeh``

Install on macOS
----------------
#. macOS domyślnie ma zainstalowaną starą wersję Pythona (z rodziny 2)
#. Pobierz i zainstaluj najnowszą wersję Pythona z oficjalnej strony internetowej (https://www.python.org/downloads/)
#. Alternatywnie użyj Brew (https://brew.sh) i zainstaluj Python za pomocą: ``brew install python3``
#. Wykonaj w terminalu ``python3 --version`` - sprawdzanie wersji Python
#. Wykonaj w terminalu ``pip3 --version`` - sprawdzanie wersji managera pakietów ``pip``
#. Wersja Python powinna być zgodna z wymienionymi powyżej
#. Wersja ``pip`` w nie ma większego znaczenia podczas kursu, ale ważne aby polecenie nie wyrzuciło błędu (``pip`` by był poprawnie zainstalowany).

Install on Linux
----------------
#. Niemalże wszystkie dystrybucje Linuxa posiadają zainstalowanego Pythona
#. Pobierz i zainstaluj najnowszą wersję Pythona z oficjalnej strony internetowej (https://www.python.org/downloads/)
#. Alternatywnie zainstaluj używając managera pakietów dla dystrybucji z której korzystasz:

    * ``apt`` - Debian, Ubuntu
    * ``snap`` - Ubuntu
    * ``yum`` - SuSe
    * ``emerge`` - Gentoo
    * ``rpm`` - RedHat, Fedora

#. Wykonaj w terminalu ``python3 --version`` - sprawdzanie wersji Python
#. Wykonaj w terminalu ``pip3 --version`` - sprawdzanie wersji managera pakietów ``pip``
#. Wersja Python powinna być zgodna z wymienionymi powyżej
#. Wersja ``pip`` w nie ma większego znaczenia podczas kursu, ale ważne aby polecenie nie wyrzuciło błędu (``pip`` by był poprawnie zainstalowany).

.. note:: W Ubuntu może nie być ``pip`` wtedy trzeba uruchomić ``sudo apt update; sudo apt install --yes python3-pip``

Install on Windows
------------------
#. Pobierz i zainstaluj najnowszą wersję Pythona
#. Podczas instalacji pozostaw domyślne opcje
#. Wykonaj w terminalu ``python3 --version`` - sprawdzanie wersji Python
#. Wykonaj w terminalu ``pip3 --version`` - sprawdzanie wersji managera pakietów ``pip``
#. Wersja Python powinna być zgodna z wymienionymi powyżej
#. Wersja ``pip`` w nie ma większego znaczenia podczas kursu, ale ważne aby polecenie nie wyrzuciło błędu (``pip`` by był poprawnie zainstalowany).

.. note:: Uwaga do starszych wersji Windows:

    * Podczas instalacji Python zaznacz opcję "Dodaj Python do zmiennej ``PATH``"
    * Jest to ważne, gdyż inaczej interpreter nie uruchomi się w trybie poleceń ``cmd``!
    * Jeżeli nie zaznaczysz tej opcji podczas instalacji, trzeba będzie to zrobić ręcznie:

        #. Kliknij przycisk start
        #. Kliknij prawym przyciskiem myszy na "Komputer" i wybierz z menu: "Właściwości"
        #. Z menu po lewej stronie wybierz: "Zaawansowane ustawienia systemu" (wymaga uprawnień administracyjnych)
        #. Na zakładce "Zaawansowane" kliknąć przycisk "Zmienne środowiskowe..." (na dole po prawej)
        #. Z okienka "Zmienne systemowe" (dolne okienko - ważne!) wybrać zmienną ``Path`` (na dole listy) i kliknąć "Edytuj..."
        #. Na końcu pola "Wartość zmiennej" dopisać poniższe wartości
        #. Uwaga, nie kasować tego co już jest tylko dopisać na koniec
        #. Ścieżki muszą być rozdzielone średnikiem ";", tzn. dopisać na końcu pola, za pozostałymi wpisami treść ``;ścieżka1;ścieżka2``
       #. Ścieżki do dopisania:

            * ``%USERPROFILE%\AppData\Local\Programs\Python\Python38\``
            * ``%USERPROFILE%\AppData\Local\Programs\Python\Python38\Scripts\``

        #. Po wprowadzeniu modyfikacji kliknij "OK", następnie "OK" dla okienka ze zmiennymi środowiskowymi oraz "OK" w okienku "Właściwości systemu"
        #. Trzeba zamknąć i uruchomić ``cmd`` ponownie
        #. Starsze wersje Windows wymagają wylogowania użytkownika i zalogowania się ponownie

    * Można to też zrobić z poziomu ``cmd``: ``setx PATH "%PATH%;ścieżka1;ścieżka2"``
    * Instrukcja z obrazkami: https://www.computerhope.com/issues/ch000549.htm
