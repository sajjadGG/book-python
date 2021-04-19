"""
GIT
---
0. Github jest najpopularniejszym na świecie miejscem wymiany kodu źródłowego,
   który od 2018 roku Github należy do Microsoft [1]. Python, Kernel Linuxa
   oraz wiele projektów open source, np. .NET, Swift, Django są rozwijane
   na Github.
1. Jeżeli nie masz konta na Github to proszę je załóż
   a. Założenie i posiadanie konta jest darmowe
   b. Będzie konieczne do sprawnego przeprowadzenia szkolenia
   c. Konieczne będzie podanie adresu email (użyj prywatnego lub firmowego)
   d. Maila będzie trzeba zweryfikować klikając w link aktywacyjny
2. Wpisz swój username z Github w arkuszu kalkulacyjnym zadań
    3. Zaczekaj aż trener nada Ci uprawnienia do repozytorium
    4. Wejdź na swojego maila i zaakceptuj zaproszenie do repozytorium
    5. Sprawdź czy widać pliki w repozytorium
    6. Upewnij się, że w repozytorium jest plik `.gitignore`
        a. Widzisz jego zawartość
        b. Ostatnia linia powinna zawierać `.idea/`
    7. Nie zmieniaj pliku `.gitignore`
    8. Zapisz `100%` we arkuszu zadań w wierszu z tym zadaniem



    1. Wejdź na ekran wersji PyCharm
        a. Górne menu -> File -> About PyCharm
        b. Górne menu -> Help -> About PyCharm
    2. W arkuszu zadań (w sekcji nagłówkowej) zapisz wersję PyCharm z której korzystasz
    3. Format zapisu, np. `CE 2020.3` lub `PRO 2020.2` itp.
        a. `CE` - Community Edition
        b. `PRO` - Professional
    4. Zapisz `100%` we arkuszu zadań w wierszu z tym zadaniem


    1. Trener poda Ci link do repozytorium GIT
    2. Stwórz projekt w Twoim IDE wykorzystując opcję:
        a. `Create from VCS` dla PyCharm 2020.3 lub nowszego
        b. `Get from Version Control` dla wcześniejszych wersji PyCharm
    3. Kliknij "clone" i zaczekaj na pobranie repozytorium
        a. Jeżeli zostaniesz zapytany o autoryzację wybierz "Use Token..."
        b. Powinno Cię przekierować na stronę Github: https://github.com/settings/tokens/new
        c. Nazwij token "PyCharm" i upewnij się, że sekcje "repo" and "gist" są zaznaczone
        d. Skopiuj token i wklej do PyCharm
    4. Po założeniu projektu załóż w nim katalog:
        a. W tym katalogu będziesz przechowywał kod tworzony podczas szkolenia
        b. Katalog ma mieć nazwę jak Twoje imie i pierwsza litera nazwiska,
           np. `JanT`, `MarkW` lub `MelissaL`
        c. Nie używaj żadnych białych znaków (spacji) ani żadnych innych znaków specjalnych
        d. Nie używaj żadnych akcentów, znaków diakrytycznych lub znaków specyficznych dla języka
    5. Do końca szkolenia w tym katalogu będziesz tworzył rozwiązania do wszystkich zadań
    6. Dzięki oddzielnym katalogom dla każdego uczestnika unikniemy konfliktów w Git
    7. Zapisz `100%` we arkuszu zadań w wierszu z tym zadaniem


    1. W swoim katalogu stwórz plik `about_python.py`
    2. Jeżeli wyskoczy pytanie czy dodać plik do repozytorium GIT, zaznacz checkbox "Always add" i wybierz "Yes"
    3. Użyj kodu z sekcji "Given" (patrz poniżej)
    4. Uruchom kod swoim IDE (prawy klawisz myszy na kodzie -> "Run File in Python Console")
    5. Jaka wersja Python jest zainstalowana?
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)
    7. Zapisz rezultat (numer wersji) we współdzielonym arkuszu kalkulacyjnym
    8. Zapisz `100%` we arkuszu zadań w wierszu z tym zadaniem


    1. Uruchom doctesty z tego pliku
        a. Górne menu -> Run -> Run... -> Doctest in about_setup_doctest
        b. Prawy przycisk myszy -> Run 'Doctests in about_setup_doctest'
    2. Wszystkie testy muszą przechodzić
    3. Zwróć uwagę na linijkę z komentarzem `# doctest: +NORMALIZE_WHITESPACE`
        a. To jest tzw. flaga sterująca doctest
        b. Pozwala na zignorowanie łamań linii i spacji w listach, tuplach, dictach, itp
        c. Spróbuj usunąć ten zapis (nie modyfikuj wyniku) i zobacz czy testy nadal przechodzą
    4. Zapisz `100%` we współdzielonym arkuszu kalkulacyjnym w wierszu zadania

References:
    [1] Microsoft News Center
        Microsoft to acquire GitHub for $7.5 billion
        URL: https://news.microsoft.com/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/
        Year: 2018
        Retreived: 2021-04-19

Tests:
    >>> import sys
    >>> sys.version_info > (3, 7, 0)
    True
"""
