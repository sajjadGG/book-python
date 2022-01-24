Install
=======


Wymagania szkolenia
-------------------
Podczas szkolenia będziemy wykorzystywali najnowsze wersje Pythona, środowiska
PyCharm, oraz GIT, a także serwis Github i arkusz kalkulacyjny Google Sheet.

* Python w wersji 3.8, 3.9, 3.10 (preferowany: 3.10)
  [`pobierz <https://www.python.org/downloads/>`_]

* PyCharm 2021.3 lub nowszy (dowolnie Community lub Professional)
  [`pobierz <https://www.jetbrains.com/pycharm/download/>`_]

* Git w wersji 2.33 lub nowszy
  [`pobierz <https://git-scm.com/download/>`_]

* Darmowe konto na Github
  [`załóż <https://github.com/join>`_]


Checklista przygotowania do szkolenia
-------------------------------------
Poniżej znajduje się krótka checklista, która pozwoli sprawdzić czy
uczestnik jest odpowiednio przygotowany do szkolenia. Przygotowanie środowiska
przed szkoleniem zaoszczędzi dużo czasu.

1. Zainstalowany Python w wersji 3.8, 3.9 lub 3.10 (preferowany)
2. Zainstalowany GIT w wersji 2.33 lub nowszej
3. Zainstalowany PyCharm Community Edition w wersji 2021.3 lub nowszej
4. Założone darmowe konto na Github
5. Zklonowane repozytorium kodu z Github (link poda prowadzący)
6. Mam dostęp do edycji arkusza kalkulacyjnego (link poda prowadzący)
7. Mam nazwaną swoim imieniem kolumnę w arkuszu oraz wypełniłem w
   swojej kolumnie ankietę (żółte wiersze od 3 do 16 na górze arkusza)

Wyjaśnienia zasadności każdego z punktów oraz szczegółowe informacje znajdują
się poniżej.


Wymagania dodatkowe dla szkoleń Data Science
--------------------------------------------
Dla szkolenia:

    * Python w Data Science,
    * Python w Analizie Danych,
    * Python w Analizie Numerycznej,

Preferowaną wersją Python jest 3.9. **Dodatkowo** konieczna będzie
instalacja następujących pakietów:

    * ``jupyter``
    * ``jupyterlab``
    * ``numpy``
    * ``pandas``
    * ``matplotlib``
    * ``requests``
    * ``lxml``
    * ``html5lib``
    * ``beautifulsoup4``
    * ``xlrd``
    * ``scipy``

Jeżeli korzystasz z Anakondy, to te pakiety masz już zainstalowane. Jeżeli
masz czystego Pythona, to można je doinstalować wykonując polecenie w
systemie operacyjnym:

.. code-block:: console

    pip3 install --upgrade \
    jupyter \
    jupyterlab \
    numpy \
    pandas \
    matplotlib \
    requests \
    lxml \
    html5lib \
    beautifulsoup4 \
    xlrd \
    scipy

Do instalacji pakietów konieczny jest dostęp do internetu oraz uprawnienia
na komputerze do instalacji pakietów za pomocą ``pip``.


Wymagania dodatkowe dla szkoleń Machine Learning
------------------------------------------------
Dla szkolenia:

    * Python Machine Learning

Preferowaną wersją Python jest 3.9. **Dodatkowo** (łącznie z tymi z używanymi w
Data Science) konieczna będzie instalacja następujących pakietów:

    * ``scikit-learn``
    * ``statsmodels``
    * ``seaborn``
    * ``bokeh``
    * ``tensorflow``
    * ``pytorch``
    * ``keras``

Jeżeli korzystasz z Anakondy, to te pakiety masz już zainstalowane. Jeżeli
masz czystego Pythona, to można je doinstalować wykonując polecenie w
systemie operacyjnym:

.. code-block:: console

    pip3 install --upgrade
    scikit-learn \
    statsmodels \
    seaborn \
    bokeh \
    tensorflow \
    pytorch \
    keras

Do instalacji pakietów konieczny jest dostęp do internetu oraz uprawnienia
na komputerze do instalacji pakietów za pomocą ``pip``.


Dostępność i punktualność podczas szkolenia
-------------------------------------------
Każdy dzień zaczyna się i kończy punktualnie. Proszę o przybycie minutę
lub dwie wcześniej. Nie planowane są także krótsze zajęcia. Z tego powodu
proszę o takie zagospodarowanie czasu, aby nie rozłączać się przed końcem
szkolenia.

Proszę o zapewnienie 100% dostępności podczas szkolenia. Bardzo często podczas
szkolenia uczestnicy są rozpraszani przez komunikatory, e-maile z pracy, pilne
spotkania czy rozmowy. Bardzo negatywnie wpływa to na efektywność szkolenia.
Powoduje to rosnące zaległości uczestników, która czasami ciągną się
już do samego końca szkolenia.


Czy można korzystać ze swojego komputera?
-----------------------------------------
Tak. Można korzystać ze swojego komputera i dowolnego systemu operacyjnego.
Podczas szkolenia mogą pojawić się niewielkie różnice między systemami
operacyjnymi i wersjami Pythona. Zawsze będzie to wspomniane w zadaniu.


Czy można korzystać z pakietu Anaconda?
---------------------------------------
Tak. Python może być zainstalowany albo za pomocą oficjalnej dystrybucji albo
z pakietu Anaconda. Wybór dystrybucji Python nie będzie miał wpływu na
przebieg szkolenia.


Monitorowanie postępu
---------------------
W arkuszu kalkulacyjnym (link poda prowadzący) w pierwszym wierszu
proszę każdego uczestnika o wpisanie swojego imienia i pierwszej
litery nazwiska (zamiast Uczestnik 1, 2 itd). Każda osoba powinna mieć
swoją kolumnę. Arkusz umożliwi nam współpracę podczas zajęć oraz
monitorowanie postępu prac. Arkusz będzie na bieżąco aktualizowany przez
prowadzącego a także przez uczestników.

Dostęp do arkusza a także uprawnienia do edycji NIE WYMAGAJĄ posiadania
konta Google! Natomiast proszę zwrócić uwagę, że niektórzy pracodawcy blokują
dostęp do usług Google. Proszę aby wszyscy uczestnicy upewnili się, że z
komputera z którego będą korzystali w lokalizacji gdzie będą podczas szkolenia
sprawdzili czy mają dostęp i czy mogą go edytować. Jest to konieczne dla
przeprowadzenia szkolenia.


Środowisko programistyczne
--------------------------
Podczas szkolenia trener będzie korzystał z PyCharm jako środowisko
programistyczne (IDE). Podczas szkolenia NIE będziemy korzystali
z funkcjonalności wersji Professional i wersja darmowa w zupełności
wystarczy.

Jeżeli wybierzesz aby podczas szkolenia również korzystać z PyCharm,
to nie będzie miało znaczenia czy jest to wersja Community (darmowa)
czy Professional (płatna). Proszę tylko aby upewnić się, że jest aktualna,
gdyż projekt szybko ewoluuje i dużo opcji się zmienia.

Można korzystać z innego IDE, ale proszę zaznajomić się z nim przed
szkoleniem. Podczas szkolenia nie będzie czasu na rozwiązywanie
problemów z innymi IDE! Proszę również zaznajomić się z obsługą rebase
dla operacji git push i git pull (zwróć uwagę, że jest to rebase a nie
merge!) oraz uruchamianiem i analizą wyników dla doctestów (wszystkie
zadania będą je miały) jak również opcjami refactoringu, który
będziemy wykonywali w każdym zadaniu.


Materiały do szkolenia
----------------------
Materiały do szkolenia są dostępne przed szkoleniem, a także po jego
zakończeniu. Ze względu na niemalże codzienne aktualizacje oraz
objętość (około 4700 stron przy eksporcie do PDF) materiały są
dostępne wyłącznie online.

Wszystkie listingi w materiałach mają testy (ponad 13 tys.). Również
wszystkie zadania, których jest ponad 500 są w pełni otestowane, a ich
rozwiązania są dostępne przez cały czas dla uczestników. Uczestnicy będą
mieli do rozwiązania tylko określoną liczbę zadań, a część z nich będzie
przeznaczona do wykonania samodzielnie w domu (dla chętnych, wieczorami
lub po szkoleniu). Podczas szkolenia nie będzie wymaganych zadań domowych.
Od uczestników nie wymagana jest dostępność poza godzinami szkolenia.


Czy mogę korzystać z innego IDE niż PyCharm?
--------------------------------------------
Tak. Podczas szkolenia trener będzie korzystał z PyCharm Professional jako
środowisko programistyczne (IDE). Można korzystać z innego IDE, ale
proszę zaznajomić się z nim przed szkoleniem. Podczas szkolenia nie będzie
czasu na rozwiązywanie problemów technicznych z innymi IDE! Jeżeli
wybierzesz PyCharm, to nie będzie miało znaczenia czy jest to wersja
Community (darmowa) czy Professional (płatna). Podczas szkolenia nie
będziemy korzystali z funkcjonalności wersji Professional i wersja darmowa
w zupełności wystarczy.


Czy konieczne jest konto na Github?
-----------------------------------
Tak. Proszę o zainstalowanie Git i założenie darmowego konta na Github oraz
potwierdzenie odnośnika aktywacyjnego na mailu. Podczas szkolenia będziemy
pracowali na jednym repozytorium, a wszystkie zadania do wykonania również
tam będą umieszczane. Korzystanie z Github zaoszczędzi bardzo dużo żmudnej
i podatnej na błędy pracy.

Odnośnik do repozytorium zostanie przekazany przez prowadzącego. Na początku
szkolenia, przed rozpoczęciem pracy repozytorium będzie publicznie dostępne
tylko do odczytu. W momencie otrzymania loginów Github wszystkich uczestników,
zakres widoczności repozytorium zostanie zmieniony na Private, tak aby
uczestnicy komfortowo mogli wysyłać rozwiązania zadań i nie obawiali
się o swoją prywatność.

Przed szkoleniem proszę o pobranie za pomocą opcji "Get from VCS" w PyCharm
repozytorium. Opcja jest dostępna na ekranie wyboru projektu - pierwszy ekran
po uruchomieniu programu. Jeżeli automatycznie otworzył się domyślny projekt,
to konieczne jest jego zamknięcie przez wybranie z menu aplikacji:
`File -> Close Project`.

Przed szkoleniem proszę o weryfikację czy klonowanie repozytorium z Github
działa, gdyż niektórzy pracodawcy blokują dostęp do Github. Najczęściej jest
to podczas korzystania z VPN. Upewnij się proszę, czy po rozłączeniu z VPNem
uda się pobrać repozytorium. Czasami zdarza się wręcz przeciwna sytuacja.
Dostęp do repozytorium jest zablokowany, gdy komputer nie łączy się przez VPN.

Proszę o rozwiązanie tych problemów przed szkoleniem. To bardzo ważne. Czasami
wymaga to wysłania zlecenia do działu wsparcia IT, a to trwa kilka dni.
Podczas szkolenia nic z tym nie będzie można zrobić. Github jest NIEZBĘDNY
do przekazania zadań oraz ich rozwiązań!
