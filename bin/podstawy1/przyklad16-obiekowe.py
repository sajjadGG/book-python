class Pojazd:
    kola = None
    kierowca = None
    moc = None
    kolor = None


class Samochod(Pojazd):
    marka = None
    kierowca = {'imie': 'Matt', 'nazwisko': 'Harasymczuk'}

    def __init__(self, kolor=None,
                 kola=4, moc=100, stan='wylaczony'):

        self.moc = moc
        self.kola = kola
        self.stan = stan
        self.kolor = kolor

    def wlacz(self):
        """
        Włącza silnik
        """
        self.stan = 'wlaczony'

    def wylacz(self):
        self.stan = 'wylaczony'

    def jaka_marka(self):
        print(self.marka)

    @staticmethod
    def jedz():
        pass


class Motor(Pojazd):
    kola = 2



class Jeep(Samochod):
    marka = 'jeep'


class Star(Samochod):
    marka = 'star'



# audi = Samochod(marka='audi')
# audi.jaka_marka()
#
# mercedes = Samochod(marka='mercedes')
# mercedes.jaka_marka()
#
# lada = Samochod(marka='lada')
# lada.jaka_marka()



moj_samochod = Jeep()
moj_samochod.jaka_marka()






import sys
sys.exit()

audi.wlacz()
Samochod.wlacz(audi)
audi.jedz()

audi.foobar = 'hej'
print(audi.__dict__)