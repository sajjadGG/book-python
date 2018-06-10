WIEK_PELNOLETNIOSCI = 18


wiek = input('Podaj wiek: ')


if int(float(wiek)) >= WIEK_PELNOLETNIOSCI:
    print('Pelnoletni')
else:
    print('Niepelnoletni')