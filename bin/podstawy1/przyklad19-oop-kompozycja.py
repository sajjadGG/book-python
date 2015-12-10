class OtwieralneSzyby:
    def otworz_szyby(self):
        raise NotImplementedError


class OtwieralnyDach:
    def otorz_dach(self):
        raise NotImplementedError


class UmieTrabic:
    def zatrab(self):
        print('\bbiip')


class Pojazd:
    kola = None


class Samochod(Pojazd, UmieTrabic, OtwieralneSzyby):
    kola = 4

    def wlacz_swiatla(self, *args, **kwargs):
        print('włączam światła')


class Cabrio(Samochod, OtwieralnyDach):
    def wlacz_swiatla(self, *args, **kwargs):
        print('Podnieś obudowę lamp')
        print('Puść muzyzkę')
        super(Cabrio, self).wlacz_swiatla(*args, **kwargs)
        print('Zatrąb')


class Motor(Pojazd, UmieTrabic):
    kola = 2



c = Cabrio()
c.wlacz_swiatla()
