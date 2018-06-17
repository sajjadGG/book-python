class OtwieralneSzyby:
    def otworz_szyby(self):
        self.szyby = 'otwarte'

    def zamknij_szyby(self):
        self.szyby = 'zamkniete'

class OtwieralnyDach:
    def otorz_dach(self):
        self.dach = 'otwarty'

    def zamknij_dach(self):
        self.dach = 'zamkniety'

class UmieTrabic:
    def zatrab(self):
        print('biip')

class Pojazd:
    kola = None
    szyby = None
    dach = None


class Samochod(Pojazd, UmieTrabic, OtwieralneSzyby):
    kola = 4

    def wlacz_swiatla(self, *args, **kwargs):
        print('włączam światła')


class Cabrio(Samochod, OtwieralnyDach):
    def wlacz_swiatla(self, *args, **kwargs):
        print('Podnieś obudowę lamp')
        print('Puść muzyzkę')
        super().wlacz_swiatla(*args, **kwargs)
        print('Zatrąb')


class Motor(Pojazd, UmieTrabic):
    kola = 2


car = Cabrio()

car.otworz_szyby()
car.szyby
# otwarte

car.zamknij_szyby()
car.szyby
# zamkniete

car.wlacz_swiatla()