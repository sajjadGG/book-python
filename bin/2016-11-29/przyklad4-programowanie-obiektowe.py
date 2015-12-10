class OtwieralnyDach:
    def __init__(self, *args, **kwargs):
        print('Otwieralny dach')

    def otworz_dach(self):
        pass

    def zamknij_dach(self):
        pass


class Trabiacy:
    def __init__(self, *args, **kwargs):
        print('Trabiacy')

    def zatrab(self):
        pass


class WymienialnySilnik():
    def __init__(self, *args, **kwargs):
        print('Wymienialny silnik')

    def wymien_silnik(self):
        pass


class Pojazd:

    def __init__(self, kola=4, *args, **kwargs):
        self.kola = kola
        print('Pojazd')


class Motor(Pojazd, WymienialnySilnik):

    def __init__(self, kola=2, *args, **kwargs):
        print('motor')
        self.kola = kola


class Samochod(Pojazd, Trabiacy):
    def __init__(self, *args, **kwargs):
        print('Samochod')



class Cabriolet(Pojazd, Trabiacy, OtwieralnyDach, WymienialnySilnik):

    @staticmethod
    def foo(*, asd):
        print(locals())

    @property
    def _bar(self):
        pass

    @_bar.setter
    def set_bar(self):
        pass


    def __str__(self):
        pass

    def __gt__(self, other):
        if self.km > other.km:
            return True
        else:
            return False


    def __init__(self, muzyczka=True, *args, **kwargs):
        self.muzyczka = muzyczka
        print('cabriolet')
        super(Cabriolet, self).__init__(*args, **kwargs)


c1 = Cabriolet(km=300)
c2 = Cabriolet(km=250)

c1 > c2

Cabriolet._bar


"""
moto = Motor()
maluch = Cabriolet()


OtwieralnyDach.otworz_dach(maluch)
maluch.otworz_dach()

OtwieralnyDach.otworz_dach(moto)
#- moto.otworz_dach()

maluch.otworz_dach()
#- maluch.otworz_dach(moto)
"""

#Cabriolet.foo(asd={'foobar':'bar'})


print('asda', 'czxcz', 'asdasd', sep=';')
