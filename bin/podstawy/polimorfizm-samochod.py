"""
audi = Pojazd()

switch(audi) {
    case Tir:       print(16);          break
    case Samochod:  print(4);           break
    case Motocykl:  print(2);           break
    default:        print('nie mam');   break
}
"""


class Pojazd:
    ilosc_kol = None

    def zostaw_slad(self):
        print('Ilość śladów, które zostawiam: {}'.format(self.ilosc_kol))


class Monocykl(Pojazd):
    ilosc_kol = 1


class Motocykl(Pojazd):
    ilosc_kol = 2


class Samochod(Pojazd):
    ilosc_kol = 4


class Tir(Pojazd):
    ilosc_kol = 16


audi = Monocykl()
audi.zostaw_slad()
