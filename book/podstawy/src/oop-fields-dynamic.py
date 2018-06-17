class Pojazd:
    def __init__(self, marka, kola=4):
        self.marka = marka
        self.kola = kola
        self.kierowca = 'Max Peck'  # tak się raczej nie robi


mercedes = Pojazd(marka='mercedes', kola=6)
print(mercedes.kola)

tir = Pojazd(marka='scania', kola=18)
print(tir.kola)