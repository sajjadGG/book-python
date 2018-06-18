class Samochod:
    def __init__(self, marka, kola=4):
        self.marka = marka
        self.kola = kola

    def __str__(self):
        return f'Marka: {self.marka} i ma {self.kola} koła'

    def __repr__(self):
        return f'Samochod(marka={self.marka}, kola={self.kola})'


auto = Samochod(marka='mercedes', kola=3)
print(auto)
# Marka: mercedes i ma 3 koła

auta = [
    Samochod(marka='mercedes', kola=3),
    Samochod(marka='maluch', kola=4),
    Samochod(marka='fiat', kola=4),
]
print(auta)
# Samochod(marka='mercedes', kola=3),
# Samochod(marka='maluch', kola=4),
# Samochod(marka='fiat', kola=4),
