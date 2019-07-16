from datetime import date, datetime
from random import randint

YEAR = 365.2524


class Klient:
    def __init__(self, imie, nazwisko, data_urodzenia=None, czy_zonaty=None, czy_praca=None, czy_dzieci=None, konta=()):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia
        self.czy_zonaty = czy_zonaty
        self.czy_praca = czy_praca
        self.czy_dzieci = czy_dzieci
        self.konta = list(konta)

    def wiek(self):
        wiek = (datetime.now().date() - self.data_urodzenia)
        return round(wiek.days / YEAR)

    def wylicz_scoring_kredytowy(self):
        score = 0

        if self.czy_zonaty:
            score += 10
        if self.czy_praca:
            score += 200
        if self.czy_dzieci:
            score -= 50

        score += self.wiek() * 10
        score += len(self.konta) * 20
        score += sum(x.saldo for x in self.konta)

        return score


class Konto:
    TYP = None

    def __init__(self, saldo=0.0, waluta='PLN'):
        self.saldo = saldo
        self.waluta = waluta
        self.numer = randint(0, 1e24)
        self.oprocentowanie = None


class KontoFirmowe(Konto):
    TYP = 'Firmowe'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.oprocentowanie = 1.0


class KontoWalutowe(Konto):
    TYP = 'Walutowe'

    def __init__(self, waluta, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.oprocentowanie = 1.19


class KontoOszczednosciowe(Konto):
    TYP = 'Oszczędnościowe'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.oprocentowanie = 0.0


twardowski = Klient(
    imie='Jan',
    nazwisko='Twardowski',
    data_urodzenia=date(1970, 1, 1),
    czy_dzieci=True,
    czy_praca=True,
    czy_zonaty=True,
    konta=[
        KontoOszczednosciowe(),
        KontoOszczednosciowe(),
        KontoWalutowe('EUR'),
    ]
)

if __name__ == '__main__':
    twardowski.wylicz_scoring_kredytowy()
