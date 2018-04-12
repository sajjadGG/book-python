import unittest


class Prostokat:
    def __init__(self, bok_a: [float, int], bok_b: [float, int]) -> None:
        if not isinstance(bok_a, (float, int)) or bok_a <= 0:
            raise ValueError('Długość boku A musi być więszka od 0')

        if not isinstance(bok_b, (float, int)) or bok_b <= 0:
            raise ValueError('Długość boku B musi być więszka od 0')

        self.bok_a = float(bok_a)
        self.bok_b = float(bok_b)

    def pole(self) -> float:
        return self.bok_a * self.bok_b

    def obwod(self) -> float:
        return 2 * (self.bok_a+self.bok_b)

    def __str__(self) -> str:
        return f'Prostokat(a={self.bok_a}, b={self.bok_b})'


class ProstokatTest(unittest.TestCase):

    def setUp(self):
        self.prostokat = Prostokat(bok_a=10, bok_b=20)

    def test_prostokata_bok_nieprawidlowy(self):
        with self.assertRaises(ValueError):
            Prostokat(bok_a='a', bok_b=20)

        with self.assertRaises(ValueError):
            Prostokat(bok_a=20, bok_b='b')

    def test_prostokata_bok_zero(self):
        with self.assertRaises(ValueError):
            Prostokat(bok_a=0, bok_b=20)

        with self.assertRaises(ValueError):
            Prostokat(bok_a=20, bok_b=0)

    def test_prostokata_bok_ujemny(self):
        with self.assertRaises(ValueError):
            Prostokat(bok_a=-3, bok_b=20)

        with self.assertRaises(ValueError):
            Prostokat(bok_a=20, bok_b=-3)

    def test_ustawienia_bokow(self):
        with self.assertRaises(TypeError):
            Prostokat(bok_a=0)

        with self.assertRaises(TypeError):
            Prostokat(bok_b=0)

    def test_tworzenie_prostokata(self):
        self.assertEqual(self.prostokat.bok_a, 2)
        self.assertEqual(self.prostokat.bok_b, 3.0)

    def test_pola(self):
        self.assertEqual(self.prostokat.pole(), 6)

    def test_obwod(self):
        self.assertEqual(self.prostokat.obwod(), 10)

    def test_prostokat_to_string(self):
        self.assertEqual(str(self.prostokat), 'Prostokat(a=2.0, b=3.0)')


if __name__ == '__main__':
    unittest.main()
