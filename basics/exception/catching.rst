.. testsetup::

    # Simulate user input (for test automation)
    from unittest.mock import MagicMock
    input = MagicMock(side_effect=[''])

    from pathlib import Path
    Path('/tmp/myfile.txt').unlink(missing_ok=True)


Exception Catching
==================
* ``try``
* ``except``
* ``else``
* ``finally``
* ``try`` is required and then one of the others blocks


Catch Exception
---------------
* Catch single exception

>>> def database_connect():
...     raise ConnectionError('Cannot connect to database')
>>>
>>>
>>> try:
...     database_connect()
... except ConnectionError:
...     print('Connection Error')
Connection Error


Catch Exception with Details
----------------------------
* Catch single exception

>>> def database_connect():
...     raise ConnectionError('Cannot connect to database')
>>>
>>>
>>> try:
...     database_connect()
... except ConnectionError as error:
...     print(f'Connection Error: {error}')
Connection Error: Cannot connect to database


Catch Different Exceptions
--------------------------
* Catch exceptions with different handling

>>> def database_connect():
...     raise ConnectionError('Cannot connect to database')
>>>
>>>
>>> try:
...     database_connect()
... except ConnectionRefusedError:
...     print('Connection Refused')
... except ConnectionAbortedError:
...     print('Connection Aborted')
... except ConnectionError:
...     print('Connection Error')
Connection Error


Catch Multiple Exception
------------------------
* Catch exceptions with the same handling

>>> def database_connect():
...     raise ConnectionError('Cannot connect to database')
>>>
>>>
>>> try:
...     database_connect()
... except (ConnectionRefusedError, ConnectionAbortedError):
...     print('Cannot establish connection')
... except ConnectionError:
...     print('Connection Error')
Connection Error


Else
----
* ``else`` is executed when no exception occurred

>>> def database_connect():
...     raise ConnectionError('Cannot connect to database')
>>>
>>>
>>> try:
...     db = database_connect()
... except ConnectionError:
...     print('Connection Error')
... else:
...     print('Connection Established')
...     db.query('SELECT * FROM users')
Connection Error


Finally
-------
* ``finally`` is executed always (even if there was exception)

``finally`` is executed always (even if there was exception). Typically it is
used to close file, connection or transaction to database:

>>> def database_connect():
...     raise ConnectionError('Cannot connect to database')
>>>
>>>
>>> try:
...     db = database_connect()
... except ConnectionError:
...     print('Connection Error')
... else:
...     print('Connection Established')
...     db.query('SELECT * FROM users')
... finally:
...     print('Connection Closed')
Connection Error
Connection Closed


Pokemon Exception Handling
--------------------------
* "Gotta catch 'em all"
* ``Ctrl-C`` raises ``KeyboardInterrupt``
* Operating system shutdown raises ``SystemExit``

One cannot simply kill program with ``Ctrl-C``:

>>> # doctest: +SKIP
... while True:
...     try:
...         number = float(input('Type number: '))
...     except:
...         continue

One can kill program with ``Ctrl-C``:

>>> # doctest: +SKIP
... while True:
...     try:
...         number = float(input('Type number: '))
...     except Exception:
...         continue


Exception Chain
---------------
>>> def database_connect():
...     raise ConnectionError
>>>
>>>
>>> try:
...     database_connect()
... except ConnectionError as error:
...     raise RuntimeError('Failed to open database') from error  # doctest: +SKIP
Traceback (most recent call last):
ConnectionError
<BLANKLINE>
The above exception was the direct cause of the following exception:
<BLANKLINE>
Traceback (most recent call last):
RuntimeError: Failed to open database


Exception Chain Silencing
-------------------------
>>> def database_connect():
...     raise ConnectionError
>>>
>>>
>>> try:
...     database_connect()
... except ConnectionError:
...     raise RuntimeError('Failed to open database') from None
Traceback (most recent call last):
RuntimeError: Failed to open database


Recap
-----
>>> try:
...     'Expression to evaluate'
... except TypeError:
...     'Catch single exception'
... except ValueError as error:
...     'Catch single exception and use it as "error" variable'
... except (IndexError, KeyError):
...     'Catch multiple exceptions'
... except Exception:
...     'Catch any other exceptions'
... else:
...     'What to do if no exception occurs'
... finally:
...     'What to do either if exception occurs or not'
'Expression to evaluate'
'What to do if no exception occurs'
'What to do either if exception occurs or not'


Use Case - 0x01
---------------
>>> def database_connect():
...     print('Connecting...')
>>>
>>>
>>> try:
...     db = database_connect()
... except ConnectionError:
...     print('Sorry, no internet connection')
... except PermissionError:
...     print('Sorry, permission denied')
... except Exception:
...     print('Sorry, unknown error')
... else:
...     print('Connection established')
...     print('Executing query...')
... finally:
...     print('Disconnect from database')
Connecting...
Connection established
Executing query...
Disconnect from database


Use Case - 0x02
---------------
>>> try:
...     with open(r'/tmp/my-file.txt') as file:
...         print(file.read())
... except FileNotFoundError:
...     print('File does not exist')
... except PermissionError:
...     print('Permission denied')
File does not exist


Use Case - 0x03
---------------
>>> try:
...     file = open('/tmp/myfile.txt')
... except Exception:
...     print('Error, file cannot be open')
... finally:
...     print('Close file')
Error, file cannot be open
Close file


Use Case - 0x03
---------------
>>> def apollo13():
...     raise RuntimeError('Oxygen tank explosion')
>>>
>>>
>>> try:
...     apollo13()
... except RuntimeError:
...     print('Houston we have a problem')
Houston we have a problem


Use Case - 0x04
---------------
>>> def apollo11():
...     print('Try landing on the Moon')
>>>
>>>
>>> try:
...     apollo11()
... except Exception:
...     print('Abort')
... finally:
...     print('Returning safely to the Earth')
Try landing on the Moon
Returning safely to the Earth


Use Case - 0x05
---------------
>>> def apollo11():
...     print('Program P63 - Landing Manoeuvre Approach Phase')
...     raise RuntimeError('1201 Alarm')
...     raise RuntimeError('1202 Alarm')
...     print('Contact lights')
...     print('The Eagle has landed!')
...     print("That's one small step for [a] man, one giant leap for mankind.")
>>>
>>>
>>> try:
...     apollo11()
... except RuntimeError:
...     print("You're GO for landing")
... except Exception:
...     print('Abort')
... else:
...     print('Landing a man on the Moon')
... finally:
...     print('Returning safely to the Earth')
Program P63 - Landing Manoeuvre Approach Phase
You're GO for landing
Returning safely to the Earth


Assignments
-----------
.. literalinclude:: assignments/exception_catch_a.py
    :caption: :download:`Solution <assignments/exception_catch_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/exception_catch_b.py
    :caption: :download:`Solution <assignments/exception_catch_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/exception_catch_c.py
    :caption: :download:`Solution <assignments/exception_catch_c.py>`
    :end-before: # Solution




.. todo::

    try:
        db = database.connect()
    except ConnectionError:
        print('nie udało się połączyć do bazy danych')
        exit(1)


    login = input('Podaj login: ')
    password = input('Podaj haslo: ')

    try:
        db.authenticate(login, password)
    except PermissionError:
        print('nieprawidłowy login/hasło')
        login = input('Podaj login: ')
        password = input('Podaj haslo: ')
        try:
            db.authenticate(login, password)
        except PermissionError:
            print('nieprawidłowy login/hasło')
            exit(1)

    ###

    def is_adult(age):
        if type(age) not in (int, float):
            raise TypeError('age musi być int lub float')
        if age < 0:
            raise ValueError('age nie może być ujemny')

        if age > 65:
            raise RuntimeError('trochę za dużo wiosen')

        if age >= 18:
            return True
        else:
            return False

    ###

    while age := input('Podaj wiek: '):
        try:
            age = int(age)
            break
        except ValueError:
            print('niepoprawny wiek, wpisz jeszcze raz')
            continue


    ###

    try:
        db.connect(login='admin', haslo='pass', host='localhost', port=99999999)
    except TypeError:
        print('warość parametru port ma niepoprawny typ, możliwy typ to int')
    except ValueError:
        print('wartość parametru port ma niepoprawny zakres, możliwe wartości to 0-65535')
    except ConnectionError:
        print('nie można się połączyć, bo komputer nie jest podpięty do sieci')
    except ConnectionRefusedError:
        print('nie można się połączyć, bo serwer blokuje połączenia z Twojego adresu IP')
    except BrokenPipeError:
        print('połączenie zostało zerwane przez serwer')
    except TimeoutError:
        print('Przekroczono czas oczekiwania na odpowiedź serwera przy połączeniu')

    0-65535


    while True:
        login = input('podaj login: ')
        password = input('podaj hasło: ')

        try:
            db.connect(login, password, host='localhost', port=99999999)
        except TypeError:
            print('warość parametru port ma niepoprawny typ, możliwy typ to int')
            print('wpisz poprawne dane i spróbuj ponownie')
            continue
        except ValueError:
            print('wartość parametru port ma niepoprawny zakres, możliwe wartości to 0-65535')
            print('wpisz poprawne dane i spróbuj ponownie')
            continue
        except ConnectionError:
            print('nie można się połączyć, bo komputer nie jest podpięty do sieci')
            print('podłącz się do sieci i spróbuj ponownie')
            continue

        except ConnectionRefusedError:
            print('nie można się połączyć, bo serwer blokuje połączenia z Twojego adresu IP')
            exit(1)
        except BrokenPipeError:
            print('połączenie zostało zerwane przez serwer')
            exit(1)
        except TimeoutError:
            print('Przekroczono czas oczekiwania na odpowiedź serwera przy połączeniu')
            exit(1)


    try:
        con = db.connect()
        con.execute('wstaw dane')
    except ConnectionError:
        print('nie udało się połączyć')
    except TimeoutError:
        print('za długo polecenie się wykonywało')
    else:
        print('zrobione')
    finally:
        con.close()
