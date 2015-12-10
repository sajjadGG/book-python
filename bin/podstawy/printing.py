imie = 'Piotr'
wiek = 18


def get_imie(imie):
    return imie


"""
print('Cześć ' + imie + '!')
print('Cześć %s!' % imie)

print("%s ma %s lat" % (imie, wiek))
print('%s ma %s lat' % (wiek, imie))
print('%s ma %10.1f lat' % (imie, wiek))
print('%s ma %.1f lat' % (imie, wiek))
print('%s ma %d lat' % (get_imie(imie), wiek))

print('%(imie)s ma %(wiek)d lat' % {
    'wiek': wiek,
    'imie': imie,
})

print('Hej, mam na imię %(imie)s.' % locals())
"""

"""
print('{imie} ma {wiek} lat'.format(
        imie=imie,
        wiek=wiek))


print('{wiek} ma {imie} lat'.format(**locals()))
"""

osoby_w_klasie = [
    {'username': 'mharasymczuk', 'czy_wykladowca': True},
    {'username': 'pkuzmiak', 'czy_wykladowca': False},
    {'username': 'awojtaszek', 'czy_wykladowca': False},
    {'username': 'jsenator', 'czy_wykladowca': False},
]


def wykladowca_tak_czy_nie(czy_jest_wykladowca):
    if not czy_jest_wykladowca:
        return 'nie'


"""
for osoba in osoby_w_klasie:
    print('{username} {czy_wykladowca} jest wykładowcą.'.format(
        username=osoba.get('username'),
        czy_wykladowca=wykladowca_tak_czy_nie(osoba.get('czy_wykladowca')) or '',
    ))
"""

"""
for osoba in osoby_w_klasie:
    print('{username} {czy_wykladowca} jest wykładowcą.'.format(
        username=osoba.get('username'),
        czy_wykladowca=not osoba.get('czy_wykladowca') and 'nie' or '',
    ))
"""

"""
ciag_znakow = 'Cześć {imie}, jak się masz? słyszałem, że dziśkończysz {wiek} lat'.format(imie=imie, wiek=wiek)

print(ciag_znakow)
"""

username = 'mharasymczuk'
password = "Python123"
password = "' OR 1=1 --"
password = "' OR 1=1 UNION SELECT id, username, password from users --"
password = "' OR 1=1; DROP TABLE users --"

# podatne na sql injection
sql_query = """

    SELECT id, username, email
    FROM users
    WHERE 'username' = '{username}'
    AND 'password' = '{password}'

""".format(username=username, password=password)

print(sql_query)

# TODO: :)

sql_query = prepare("""
    SELECT id, username, email
    FROM users
    WHERE 'username' = ?
    AND 'password' = ?
""")
