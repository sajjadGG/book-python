"""
#. Wczytaj od użytkownika imię
#. Użytkownik wprowadza tylko dane typu ``str``
#. Za pomocą f-string formatting wyświetl na ekranie ``'My name "IMIE".\nI hope you\'re ok!'``, gdzie IMIE to wartość którą podał
#. Zwróć uwagę na znaki cudzysłowia i nowych linii
#. Tekst wyświetlony na ekranie ma mieć zamienione wszystkie spacje na ``_``
#. Nie korzystaj z dodawania stringów ``str + str``

:Założenia:
    * Nazwa pliku: ``types_input.py``
    * Szacunkowa długość kodu: 3 linie
    * Maksymalny czas na zadanie: 5 min

:Co zadanie sprawdza?:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika
"""

name = input('Type your name: ')
output = f'My name "{name}".\nI hope you\'re ok!'
print(output.replace(' ', '_'))