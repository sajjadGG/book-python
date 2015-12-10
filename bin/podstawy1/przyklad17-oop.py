class Pojazd:
    kola = None

    def zostaw_slad(self):
        print(self.kola / 2)

    def zatrab(self):
        raise NotImplementedError

    def ssanie(self):
        import warnings
        warnings.warn('Używaj ssania automatycznego', PendingDeprecationWarning)

    @property
    def ile_sladow(self):
        return self.kola / 2


class Motor(Pojazd):
    kola = 2


    def zatrab(self):
        print('bip\a')


class Osobowy(Pojazd):
    kola = 4


class Ciezarowka(Pojazd):
    kola = 6

    def zostaw_slad(self):
        print(2)

    def zatrab(self):
        print('buuuuup\a\a\a')


class Quad(Motor, Osobowy):
    pass



moj_pojazd = Ciezarowka()

# moj_pojazd.zatrab()

# moj_pojazd.ssanie()



print(moj_pojazd.ile_sladow)