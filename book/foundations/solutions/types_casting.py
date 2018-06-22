"""
#. Użytkownik za pomocą wprowadza odległości w metrach
#. Użytkownik wprowadza tylko dane typu ``int`` lub ``float``
#. Dane przy wyświetlaniu muszą być przekonwertowane do typów podanych poniżej
#. Napisz program który przekonwertuje odległości i wyświetli je w formacie zgodnie z szablonem:

.. code-block:: python

    print(f'Meters: {meters}')  # int
    print(f'Kilometers: {...}')  # int
    print(f'Miles: {...}')  # float
    print(f'Nautical Miles: {...}')  # float
    print(f'All: {...}, {...}, {...}, {...}')  # int, int, float, float

:Założenia:
    * Nazwa pliku: ``types_casting.py``
    * Szacunkowa długość kodu: 3 linie
    * Maksymalny czas na zadanie: 5 min

:Co zadanie sprawdza?:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Konwersja typów
    * Operacje matematyczne na zmiennych
    * Wczytywanie tekstu od użytkownika

:Podpowiedź:
    * 1000 m = 1 km
    * 1608 m = 1 mila
    * 1852 m = 1 mila morska
"""

meters = float(input('Distance [m]: '))

km = int(meters / 1000)
miles = float(meters / 1608)
nm = float(meters / 1852)

print(f'Meters: {meters}')
print(f'Kilometers: {km}')  # int
print(f'Miles: {miles}')  # float
print(f'Nautical Miles: {nm}')  # float
print(f'All: {m}, {km}, {miles}, {nm}')  # int, int, float, float
