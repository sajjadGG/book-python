Install
=======


Requirements
------------
* `[Zainstaluj] <https://www.python.org/downloads/>`_
  Python w wersji 3.8 lub 3.9 (preferowany) [#DownloadPython]_

* `[Załóż] <https://github.com/join>`_
  konto na Github (potwierdź konto mailem!) [#GithubJoin]_

* `[Zainstaluj] <https://www.jetbrains.com/pycharm/download/>`_
  PyCharm w wersji 2021.1 lub nowszy
  (bez znaczenia czy Community czy Professional) [#DownloadPyCharm]_

* `[Zainstaluj] <https://git-scm.com/download/>`_
  Git w wersji 2.4 lub nowszy [#DownloadGit]_


FAQ - Najczęściej zadawane pytania
----------------------------------
1. Można korzystać ze swojego komputera i dowolnego systemu operacyjnego

2. Python może być zainstalowany albo za pomocą oficjalnej dystrybucji albo
   z pakietu Anaconda, a wybór dystrybucji Python nie będzie miał wpływu
   na przebieg szkolenia

3. Podczas szkolenia trener będzie korzystał z PyCharm jako środowisko
   programistyczne (IDE). Można korzystać z innego IDE, ale proszę
   zaznajomić się z nim przed szkoleniem. Podczas szkolenia nie będzie
   czasu na rozwiązywanie problemów technicznych z innymi IDE

4. Podczas instalacji PyCharm zaznacz opcję: "powiąż z rozszerzeniem plików
   ``.py``" (nie jest to konieczne ale ułatwia pracę)

5. Proszę o zainstalowanie Git i założenie darmowego konta na Github oraz
   potwierdzenie linka aktywacyjnego na mailu

6. Dla szkolenia z Analizy Numerycznej lub Machine Learning dodatkowo trzeba:

    * Posiadać uprawnienia na komputerze do instalacji pakietów Python za pomocą ``pip``
    * Do instalacji pakietów konieczny jest dostęp do internetu
    * Instalacja: ``pip3 install --upgrade jupyter numpy pandas matplotlib scikit-learn statsmodels seaborn bokeh``


Setup
-----
.. toctree::
    :maxdepth: 1

    install/python.rst
    install/github.rst
    install/ide.rst
    install/project.rst
    install/doctest.rst
    install/git.rst


References
----------
.. [#DownloadPython] Python Software Foundation. Download Python. Year: 2021. Retrieved: 2021-04-19. URL: https://www.python.org/downloads/
.. [#DownloadPyCharm] JetBrains. Download PyCharm. Year: 2021. Retrieved: 2021-04-19. URL: https://www.jetbrains.com/pycharm/download/
.. [#DownloadGit] Download Git. Year: 2021. Retrieved: 2021-04-19. URL: https://git-scm.com/download
.. [#GithubJoin] Github. Join Github. Year: 2021. Retrieved: 2021-04-19. URL: https://github.com/join
