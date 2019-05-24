*******
Threads
*******


Threads vs processes
====================

Process
-------
#. Co to jest proces?
#. Ile może być procesów?
#. Co to jest ``nice``
#. Jak komunikować się między procesami?
#. Ile może być procesów przetwarzanych równolegle na procesorze czterordzeniowym (z i bez Hyper Threading)?

Thread
------
#. Co to jest wątek?
#. Ile wątków może być w ramach procesów?
#. Jak komunikować się między wątkami?
#. Czy współdzielenie pamięci przez wątki jest dobre czy złe?
#. Ile może być wątków przetwarzanych równolegle na procesorze czterordzeniowym (z i bez Hyper Threading)?

Threads vs processes
--------------------
#. Czym się różnią wątki od procesów?


Problemy z wątkami
==================
- Zakleszczania
- Race Condition
- Głodzenie
- Problem 5 filozofów:

    - 5 filozofów (albo rozmyśla, albo je)
    - 5 misek ze spaghetti,
    - 5 widelców,
    - 2 widelce potrzebne aby zjeść,
    - problem zakleszczania

- Problem producenta i konsumenta
- Problem czytelników i pisarzy

``threading``
=============

Delay execution
---------------
* dlaczego nie ``time.sleep()``
* rekurencyjny timer

.. code-block:: python
    :caption: Delay execution

    from threading import Timer


    DELAY_SECONDS = 5.0

    def hello():
        print('Hello world!')


    t = Timer(DELAY_SECONDS, hello)
    t.start()

    print('Main Thread')


Recurrent timer
---------------
.. code-block:: python
    :caption: Recurrent timer

    from threading import Timer


    DELAY_SECONDS = 5.0

    def hello():
        print('Timer Thread')
        Timer(DELAY_SECONDS, hello).start()


    t = Timer(DELAY_SECONDS, hello)
    t.start()

    print('Main Thread')

Tworzenie wątków
================

Synchronizacja wątków
=====================
.. literalinclude:: src/threading-synchronization.py
    :name: listing-threading-synchronization
    :language: python
    :caption: Synchronizacja wątków

Zamykanie wątków
================


Workery
=======
.. literalinclude:: src/threading-worker.py
    :name: listing-threading-worker
    :language: python
    :caption: Model Workerów


Assignments
===========

Wielowątkowość
--------------
* Filename: ``thread_execute.py``
* Lines of code to write: 20 lines
* Estimated time of completion: 30 min

#. Stwórz kolejkę ``queue`` do której dodasz różne polecenia systemowe do wykonania, np.:

    - Lunux/macOS: ``['/bin/ls /etc/', '/bin/echo "test"', '/bin/sleep 2']``,
    - Windows: ``['dir c:\\Users', 'echo "test"', 'type %HOMEPATH%\Desktop\README.txt']``.

#. Następnie przygotuj trzy wątki workerów, które będą wykonywały polecenia z kolejki
#. Wątki powinny być uruchamiane jako ``subprocess.run()`` w systemie operacyjnym z timeoutem równym ``TIMEOUT = 2.0`` sekundy
#. Ilość poleceń może się zwiększać w miarę wykonywania zadania.
#. Wątki mają być uruchomione w tle (ang. ``daemon``)

:Zadanie z gwiazdką:
    #. Wątki powinny być uśpione za pomocą ``Timer`` przez ``DELAY = 5.0`` sekund, a następnie ruszyć do roboty
    #. Parametry rozbij za pomocą ``shlex``
    #. Użyj logowania za pomocą biblioteki ``logging`` tak aby przy wyświetlaniu wyników widoczny był identyfikator procesu i wątku.
