class Figura:
    def pole(self):
        raise NotImplementedError

    def obwod(self):
        raise NotImplementedError


class Trojkat(Figura):
    def pole(self):
        self.a * self.h

    def obwod(self):
        pass