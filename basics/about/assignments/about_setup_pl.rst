Setup Środowiska
================


Co będzie potrzebne?
--------------------
* Python 3.8, lub 3.9 (preferowany) [#DownloadPython]_
* PyCharm 2021 lub nowszy (bez znaczenia czy Community czy Professional) [#DownloadPyCharm]_
* GIT w wersji 2.4 lub nowszy [#DownloadGit]_
* Konto na Github (potwierdzone mailem)


Setup Github
------------
Github jest najpopularniejszym na świecie miejscem wymiany kodu źródłowego,
który od 2018 roku Github należy do Microsoft [#MicrosoftAcquireGithub]_.
Python, Kernel Linuxa oraz wiele projektów open source, np. .NET, Swift, Django
są rozwijane na Github. Założenie i posiadanie konta jest darmowe. Będzie
konieczne do sprawnego przeprowadzenia szkolenia. Konieczne będzie podanie
adresu email (użyj prywatnego lub firmowego). Maila będzie trzeba zweryfikować
klikając w link aktywacyjny

1. Jeżeli nie masz konta na Github to proszę załóż je
2. Wpisz swój username z Github w arkuszu kalkulacyjnym zadań
3. Zaczekaj aż trener nada Ci uprawnienia do repozytorium
4. Wejdź na swojego maila i zaakceptuj zaproszenie do repozytorium
5. Sprawdź czy na głównej stronie repozytorium widać pliki
6. Zapisz `100%` we arkuszu zadań w wierszu z tym zadaniem


Setup IDE
---------
PyCharm jest środowiskiem programistycznym, w którym będziemy programować.
Podczas szkolenia trener będzie korzystał tylko z tego środowiska. Nie będzie
czasu na rozwiązywanie problemów z innymi środowiskami programistycznymi, więc
proszę o instalację PyCharm w najnowszej dostępnej wersji. Bez znaczenia czy
Community czy Professional. Wersja Professional jest płatna i ma więcej
funkcjonalności (np. debugger JavaScript). Ale nie będziemy z nich korzystać
podczas szkolenia. Wersja Community w zupełności nam wystarczy.

1. Uruchom PyCharm
   a. Nie twórz projektu
   b. Jeżeli projekt otworzył Ci się automatycznie, to
      `File -> Close Project in Current Window`
   c. Na ekranie głównym w lewym górnym rogu jest numer wersji PyCharm
2. W arkuszu zadań zapisz wersję PyCharm z której korzystasz
   a. Format zapisu, np. `2021.1 CE` lub `2021.1 PRO` itp.
   b. `CE` - Community Edition
   c. `PRO` - Professional
3. Zapisz `100%` we arkuszu zadań w wierszu z tym zadaniem


Setup Repo
----------
Repozytorium posłuży nam do wymiany kodu źródłowego. Trener będzie w nim
umieszczał treści ćwiczeń do samodzielnego wykonania podczas szkolenia.
Nie będziemy pracowali na gałęziach! Wszyscy uczestnicy będą wrzucali kod do
jednego brancha do swoich katalogów. Dzięki oddzielnym katalogom dla każdego
uczestnika unikniemy konfliktów w Git. Do końca szkolenia w tym katalogu
będziesz tworzył/tworzyła rozwiązania do wszystkich zadań.

1. Wykorzystaj link do repozytorium uzyskany w zadaniu `Setup Github`
2. Stwórz projekt w Twoim IDE wykorzystując opcję:
    a. `Create from VCS` dla PyCharm 2020.3 lub nowszego
    b. `Get from Version Control` dla wcześniejszych wersji PyCharm
3. Kliknij "clone" i zaczekaj na pobranie repozytorium
    a. Jeżeli zostaniesz zapytany o autoryzację wybierz "Use Token..."
    b. Powinno Cię przekierować na stronę Github:
       https://github.com/settings/tokens/new
    c. Wszystkie opcje powinny być zaznaczone prawidłowo - nic nie zmieniaj
    d. Na dole strony zaakceptuj formularz i wygeneruj token
    d. Skopiuj token i wklej do PyCharm
    e. Zwróć uwagę, by nie skopiować spacji na końcu tokena (częsty błąd)
4. Po założeniu projektu załóż w nim katalog:
    a. W tym katalogu będziesz przechowywał kod tworzony podczas szkolenia
    b. Katalog ma mieć nazwę jak Twoje imie i pierwsza litera nazwiska,
       np. `JanT`, `MarkW` lub `MelissaL`
    c. Nie używaj żadnych białych znaków (spacji)
    d. Nie używaj żadnych innych znaków specjalnych
    d. Nie używaj żadnych akcentów, znaków diakrytycznych itp.
5. Zapisz `100%` we arkuszu zadań w wierszu z tym zadaniem


    1. W swoim katalogu stwórz plik `about_python.py`
    2.
    3. Użyj kodu z sekcji "Given" (patrz poniżej)
    4. Uruchom kod swoim IDE (prawy klawisz myszy na kodzie -> "Run File in Python Console")
    5. Jaka wersja Python jest zainstalowana?
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)
    7. Zapisz rezultat (numer wersji) we współdzielonym arkuszu kalkulacyjnym
    8. Zapisz `100%` we arkuszu zadań w wierszu z tym zadaniem


Doctest
-------
Doctest to mechanizm uruchamiania testów w Pythonie. Wyglądem przypomina
sesję Pythona w konsoli. Każda z linii kodu zaczyna się od ``>>>``. Ewentualnie
linie mogą zaczynać się od ``...`` jeżeli są kontynuacją poprzedniej linii.
Linie poniżej wyświetlają oczekiwany wynik. Doctesty muszą znajdować się w
pierwszym wieloliniowym ciągu znaków w pliku, funkcji lub klasie. Przykład:

    """
    >>> x = 1
    >>> y = 2
    >>> x + y
    3
    """

1. W swoim katalogu stwórz plik `about_python.py`
    a. Jeżeli wyskoczy pytanie czy dodać plik do repozytorium GIT,
       zaznacz checkbox "Always add" i wybierz "Yes"
2. Skopiuj treść następującego listingu do swojego kodu:

    """
    >>> import sys
    >>> sys.version_info > (3, 7, 0)
    True
    """

3. Upewnij się, że:
    a. Skopiowałeś/aś również trzy znaki cudzysłowu ``"""`` na początku i końcu
    b. Tło testów zmieniło kolor na żółty lub zielony w zależności od skórki
2. Uruchom doctesty z tego pliku
    a. Górne menu -> Run -> Run... -> `Doctest in about_python`
    b. Prawy przycisk myszy na testach -> Run 'Doctests in about_python'
2. Wszystkie testy muszą przechodzić
3. Zwróć uwagę na linijkę z komentarzem `# doctest: +NORMALIZE_WHITESPACE`
    a. To jest tzw. flaga sterująca doctest
    b. Pozwala na zignorowanie łamań linii i spacji w listach, tuplach, dictach, itp
    c. Spróbuj usunąć ten zapis (nie modyfikuj wyniku) i zobacz czy testy nadal przechodzą
4. Zapisz `100%` we współdzielonym arkuszu kalkulacyjnym w wierszu zadania


Tests:
    >>> import sys
    >>> sys.version_info > (3, 7, 0)
    True
"""



References
----------
.. [#DownloadPython] https://www.python.org/downloads/
.. [#DownloadGit] https://git-scm.com/download
.. [#DownloadPyCharm] https://www.jetbrains.com/pycharm/download/
.. [#GithubSignin]


.. [#MicrosoftAcquireGithub] Microsoft News Center. Microsoft to acquire GitHub for $7.5 billion
    URL: https://news.microsoft.com/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/
    Year: 2018
    Retrieved: 2021-04-19
