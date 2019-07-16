************
Polymorphism
************


Switch
======
.. code-block:: python
    :caption: Switch moves business logic to the execution place

    agency = 'NASA'

    if agency == 'NASA':
        print('Howdy from NASA')
    elif agency == 'Roscosmos':
        print('Privyet z Roscosmos')
    elif agency == 'ESA':
        print('Guten Tag aus ESA')
    else:
        raise NotImplementedError


.. literalinclude:: src/oop-polymorphism-function.py
    :language: python
    :caption: Polymorphism on Function

.. literalinclude:: src/oop-polymorphism-class.py
    :language: python
    :caption: Polymorphism on Classes
