def create_or_update():
    return True, [
        {'id': 1, 'imie': 'matt', 'nazwisko': 'harasymczuk'},
        {'id': 2, 'imie': 'matt', 'nazwisko': 'asd'},
    ], 10, str('asd')


czy_utworzone, *args  = create_or_update()

print(czy_utworzone)