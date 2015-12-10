class Figura:
    def __init__(self, kolor='czerwony'):
        self.kolor = kolor

    def oblicz_pole(self):
        raise NotImplementedError

    def oblicz_obwod(self):
        raise NotImplementedError

    @staticmethod
    def czy_jestem_figura():
        return True


class Czworokat:
    ilosc_bokow = 4


class Kwadrat(Figura, Czworokat):
    def __init__(self, dlugosc_boku=8,
                 pozycja_x=0, pozycja_y=0, *args, **kwargs):
        self.dlugosc_boku = dlugosc_boku
        self.pozycja_x = pozycja_x
        self.pozycja_y = pozycja_y

        super(Kwadrat, self).__init__(*args, **kwargs)

    def __str__(self):
        return 'Jestem kwadratem o boku {bok} i polu {pole}. Mam obwod {obwod}.'.format(
                bok=self.dlugosc_boku,
                pole=self.oblicz_pole(),
                obwod=self.oblicz_obwod(),
        )

    def oblicz_pole(self):
        return self.dlugosc_boku ** 2

    def oblicz_obwod(self):
        return self.dlugosc_boku * 4

    @property
    def pole(self):
        return self.oblicz_pole()

    @property
    def wierzcholoki(self):
        return self.ilosc_bokow


kwadrat_o_boku_4 = Kwadrat(dlugosc_boku=4, kolor='zielony')
kwadrat_o_boku_6 = Kwadrat(dlugosc_boku=6, pozycja_x=90)
kwadrat_o_boku_8 = Kwadrat(pozycja_x=90, pozycja_y=100)
kwadrat_o_boku_12 = Kwadrat()

print(kwadrat_o_boku_6.wierzcholoki)

print(Figura.czy_jestem_figura())



# print('Pole: %d' % Kwadrat().oblicz_pole())
# print('Obwód: %d' % Kwadrat().obwod())
