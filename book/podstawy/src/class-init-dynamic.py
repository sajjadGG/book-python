class Kontakt:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


kontakt = Kontakt(imie='Jose', nazwisko='Jimenez')
print(kontakt.imie)
# Jose