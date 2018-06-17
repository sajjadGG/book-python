class Pojazd:
    marka = None
    kierowca = 'Jose Jimenez'
    kola = 4

    def zatrab(self):
        print('piiip')

    def kto_kieruje(self):
        print(self.kierowca)

    def horn(self):
        return self.zatrab()


auto = Pojazd()

auto.zatrab()
# piiip

auto.kto_kieruje()
# Jose Jimenez

auto.kierowca
# Jose Jimenez