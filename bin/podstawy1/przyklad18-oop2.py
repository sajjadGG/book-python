class Samochod:
    def __init__(self, marka, kola=4):
        self.marka = marka
        self.kola = kola

    def __str__(self):
        return 'Marka: {marka} i ma {kola} koła'.format(**self.__dict__)


bryka = Samochod(marka='mercedes', kola=3)
#print(bryka.kola)


print(str(bryka))