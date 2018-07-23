.. _Control Flow Statements:

***********************
Control Flow Statements
***********************


Conditional Statements
======================

``if``
------
* Instrukcje warunkowe pozwalają kierować wykonywanymi instrukcjami pod pewnym warunkiem
* Jeżeli kod wpisany po słowie kluczowym ``if`` wykona się jako wartość prawdziwa (niezerowa, nie-``None``, itp.), wykonany zostanie kod pod tym słowem kluczowym

.. code-block:: python

    if True:
        print('this is True')


``else``
--------
* Do instrukcji warunkowej można dodać słowo kluczowe ``else``
* Wtedy, jeżeli wartość przy słowie kluczowym ``if`` ewaluuje się jako fałsz, wykonany zostanie kod pod słowem kluczowym ``else``

.. code-block:: python

    if True:
        print('this is True')
    else:
        print('this is False')


.. code-block:: python

    if name == 'José Jiménez':
        print('My name José Jiménez')
    else:
        print('My name is other')


``elif``
--------
* Możliwe jest także sprawdzenie kilku warunków przed przejściem do ``else``
* Do sprawdzenia drugiego i kolejnych warunków służy słowo kluczowe ``elif`` (w wielu innych językach rozwijane jako ``else if``)

.. code-block:: python

    if name == 'José Jiménez':
        print('My name José Jiménez')
    elif name == 'Max Peck':
        print('Your name is Max Peck')
    else:
        print('Your name is neither José Jiménez nor Max Peck')

.. code-block:: python

    if 0 <= k < n:
        print('k in is between [0, n)')

Inline ``if``
-------------
.. code-block:: python

    ip = '127.0.0.1'

    if '.' in ip:
        protocol = 'ipv4'
    else:
        protocol = 'ipv6'

.. code-block:: python

    ip = '127.0.0.1'

    protocol = 'ipv4' if '.' in ip else 'ipv6'


Complex expressions
===================

``and``
-------
.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    if first_name == 'José' and last_name == 'Jiménez':
        print('My name José Jiménez')
    else:
        print('Your name is different')


``or``
------
.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    if first_name == 'José' or first_name == 'Max':
        print('Your name is José or Max')
    else:
        print('Your name is different')


mixed
-----
.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    if (first_name == 'José' and last_name == 'Jiménez')
            or (first_name == 'Max' and last_name == 'Peck'):
        print('Your name is José Jiménez or Max Peck')
    else:
        print('Your name is different')


Control Statements
==================

``in``
------
* Słowo kluczowe ``in`` pozwala na sprawdzenie czy dana wartość zawiera się w zbiorze
* Można wykorzystać czy ``str`` zawiera się w innym ``str``

.. code-block:: python

    usernames = {'José Jiménez', 'Max Peck'}

    if 'José Jiménez' in usernames:
        print(True)
    else:
        print(False)

.. code-block:: python

    text = 'My name José Jiménez'

    if 'José' in text:
        print(True)
    else:
        print(False)

``not``
-------
* ``not`` pozwala zanegować warunek

.. code-block:: python

    name = None

    if not name:
        print('Name is not set')
    else:
        print('Hello my friend')

.. code-block:: python

    usernames = {'José', 'Max', 'Ivan'}

    if 'José' not in usernames:
        print('I do not know you')
    else:
        print('Hello my friend')

Tak nie robimy:

    .. code-block:: python

        usernames = {'José', 'Max', 'Ivan'}
        name = 'José'

        if not name in usernames:  # if (! usernames.contains(name)) {}
            print('I do not know you')
        else:
            print('Hello my friend')


No ``switch`` statement?!
=========================
* Why ``switch`` is bad practise?
* PEP 275 - switch statement

.. code-block:: python

    if name == 'José Jiménez':
        print('My name José Jiménez')
    elif name == 'Ivan Ivanovic':
        print('Your name is Ivan Ivanovic')
    elif name == 'Max Peck':
        print('Your name is Max Peck')
    else:
         print('Your name is other')

.. code-block:: python

    switch = {
        'José Jiménez': 'My name José Jiménez',
        'Ivan Ivanovic': 'Your name is Ivan Ivanovic',
        'Max Peck': 'Your name is Max Peck',
    }

    switch['José Jiménez']
    # 'My name José Jiménez'

.. code-block:: python

    switch = {
        'José Jiménez': 'My name José Jiménez',
        'Ivan Ivanovic': 'Your name is Ivan Ivanovic',
        'Max Peck': 'Your name is Max Peck',
    }

    key = 'Paxi'
    switch.get(key, 'Your name is other')
    # 'Your name is other'

.. code-block:: python

    def switch(key):
        return {
            'José Jiménez': 'My name José Jiménez',
            'Ivan Ivanovic': 'Your name is Ivan Ivanovic',
            'Max Peck': 'Your name is Max Peck',
        }.get(key, 'Your name is other')

    switch('José Jiménez')  # 'My name José Jiménez'
    switch('Paxi')          # 'Your name is other'


Assignments
===========

Conditioning on user input
--------------------------
#. Napisz program, który poprosi użytkownika o wiek
#. Użytkownik będzie podawał tylko i wyłącznie ``int`` lub ``float``
#. Następnie sprawdzi pełnoletność i wyświetli informację czy osoba jest "dorosła" czy "niepełnoletnia".

:Założenia:
    * Nazwa pliku: ``control_input.py``
    * Szacunkowa długość kodu: około 6 linii
    * Maksymalny czas na zadanie: 5 min

:Co zadanie sprawdza?:
    * Wczytywanie ciągu znaków od użytkownika
    * Rzutowanie i konwersja typów
    * Instrukcje warunkowe
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Definiowanie zmiennych i stałych w programie
    * Magic Number

