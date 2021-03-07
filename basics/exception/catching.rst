Exception Catching
==================

.. testsetup::

    from pathlib import Path
    Path('/tmp/myfile.txt').unlink(missing_ok=True)


Catching Exceptions
-------------------
* ``try``
* ``except``
* ``else``
* ``finally``
* ``try`` is required and then one of the others blocks

    >>> try:
    ...     'Try to execute'
    ... except Exception:
    ...     'What to do if exception occurs'
    ... else:
    ...     'What to do if no exception occurs'
    ... finally:
    ...     'What to do either if exception occurs or not'
    'Try to execute'
    'What to do if no exception occurs'
    'What to do either if exception occurs or not'

Catch single exception:

    >>> def apollo13():
    ...    raise RuntimeError('Oxygen tank explosion')
    >>>
    >>>
    >>> try:
    ...     apollo13()
    ... except RuntimeError:
    ...     print('Houston we have a problem')
    Houston we have a problem

Catch many exceptions with the same handling:

    >>> def apollo13():
    ...    raise RuntimeError('Oxygen tank explosion')
    >>>
    >>>
    >>> try:
    ...     apollo13()
    ... except (RuntimeError, TypeError, NameError):
    ...     print('Houston we have a problem')
    Houston we have a problem

Catch many exceptions with different handling:

    >>> try:
    ...    with open(r'/tmp/my-file.txt') as file:
    ...         print(file.read())
    ... except FileNotFoundError:
    ...     print('File does not exist')
    ... except PermissionError:
    ...     print('Permission denied')
    File does not exist

Exceptions logging:

    >>> import logging
    >>>
    >>>
    >>> def apollo13():
    ...     raise RuntimeError('Oxygen tank explosion')
    >>>
    >>> try:
    ...     apollo13()
    ... except RuntimeError as err:
    ...     logging.error(err)
    ... #stderr: ERROR:root:Oxygen tank explosion


Else and Finally
----------------
* ``else`` is executed when no exception occurred
* ``finally`` is executed always (even if there was exception)

``else`` is executed when no exception occurred:

    >>> def apollo11():
    ...     print('Try landing on the Moon')
    >>>
    >>> try:
    ...     apollo11()
    ... except Exception:
    ...     print('Abort')
    ... else:
    ...     print('Landing a man on the Moon')
    Try landing on the Moon
    Landing a man on the Moon

``finally`` is executed always (even if there was exception):
Used to close file, connection or transaction to database:

    >>> try:
    ...     file = open('/tmp/myfile.txt')
    ... except Exception:
    ...     print('Error, file cannot be open')
    ... finally:
    ...     print('Close file')
    Error, file cannot be open
    Close file

    >>> def apollo11():
    ...    print('Try landing on the Moon')
    >>>
    >>> try:
    ...    apollo11()
    ... except Exception:
    ...    print('Abort')
    ... finally:
    ...    print('Returning safely to the Earth')
    Try landing on the Moon
    Returning safely to the Earth

    >>> def apollo11():
    ...    print('Program P63 - Landing Manoeuvre Approach Phase')
    ...    raise RuntimeError('1201 Alarm')
    ...    raise RuntimeError('1202 Alarm')
    ...    print('Contact lights')
    ...    print('The Eagle has landed!')
    ...    print("That's one small step for [a] man, one giant leap for mankind.")
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


Pokemon Exception Handling
--------------------------
* "Gotta catch 'em all"
* ``Ctrl-C`` raises ``KeyboardInterrupt``

User cannot simply kill program with ``Ctrl-C``:

    >>> # doctest: +SKIP
    ... while True:
    ...    try:
    ...        number = float(input('Type number: '))
    ...    except:
    ...        continue

User can kill program with ``Ctrl-C``:

    >>> # doctest: +SKIP
    ... while True:
    ...     try:
    ...         number = float(input('Type number: '))
    ...     except Exception:
    ...         continue


Assignments
-----------
.. literalinclude:: assignments/controlflow_exception_a.py
    :caption: :download:`Solution <assignments/controlflow_exception_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/controlflow_exception_b.py
    :caption: :download:`Solution <assignments/controlflow_exception_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/controlflow_exception_c.py
    :caption: :download:`Solution <assignments/controlflow_exception_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/controlflow_exception_d.py
    :caption: :download:`Solution <assignments/controlflow_exception_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/controlflow_exception_e.py
    :caption: :download:`Solution <assignments/controlflow_exception_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/controlflow_exception_f.py
    :caption: :download:`Solution <assignments/controlflow_exception_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/controlflow_exception_g.py
    :caption: :download:`Solution <assignments/controlflow_exception_g.py>`
    :end-before: # Solution
