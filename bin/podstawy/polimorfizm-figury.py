class Figura:
    dlugosc_boku = None

    def __init__(self, dlugosc_boku):
        self.dlugosc_boku = dlugosc_boku

    def oblicz_obwod(self):
        raise NotImplementedError


class Kolo(Figura):
    pass


class Kwadrat(Figura):
    def oblicz_obwod(self):
        return 4 * self.dlugosc_boku


class TrojkatRownoboczny(Figura):
    def oblicz_obwod(self):
        return 3 * self.dlugosc_boku


class PieciokatForemny(Figura):
    def oblicz_obwod(self):
        return 5 * self.dlugosc_boku


foo = Kolo(dlugosc_boku=4)
print(foo.oblicz_obwod())
