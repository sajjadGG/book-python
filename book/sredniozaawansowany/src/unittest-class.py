import unittest


class Prostokat:
    def __init__(self, a, b):
        if not isinstance(a, (float, int)) or a <= 0:
            raise ValueError('Długość boku A musi być więszka od 0')

        if not isinstance(b, (float, int)) or b <= 0:
            raise ValueError('Długość boku B musi być więszka od 0')

        self.bok_a = float(a)
        self.bok_b = float(a)

    def pole(self):
        return self.bok_a * self.bok_b

    def obwod(self):
        return 2 * (self.bok_a + self.bok_b)

    def __str__(self):
        return f'Prostokat(a={self.bok_a}, b={self.bok_b})'


class ProstokatTest(unittest.TestCase):

    def setUp(self):
        self.prostokat = Prostokat(a=10, b=20)

    def test_prostokata_bok_nieprawidlowy(self):
        with self.assertRaises(ValueError):
            Prostokat(a='a', b=20)

        with self.assertRaises(ValueError):
            Prostokat(a=20, b='b')

    def test_prostokata_bok_zero(self):
        with self.assertRaises(ValueError):
            Prostokat(a=0, b=20)

        with self.assertRaises(ValueError):
            Prostokat(a=20, b=0)

    def test_prostokata_bok_ujemny(self):
        with self.assertRaises(ValueError):
            Prostokat(a=-3, b=20)

        with self.assertRaises(ValueError):
            Prostokat(a=20, b=-3)

    def test_ustawienia_bokow(self):
        with self.assertRaises(TypeError):
            Prostokat(a=0)

        with self.assertRaises(TypeError):
            Prostokat(b=0)

    def test_tworzenie_prostokata(self):
        self.assertEqual(self.prostokat.bok_a, 10)
        self.assertEqual(self.prostokat.bok_b, 20)

    def test_pole(self):
        self.assertEqual(self.prostokat.pole(), 200)

    def test_obwod(self):
        self.assertEqual(self.prostokat.obwod(), 60)

    def test_prostokat_to_string(self):
        self.assertEqual(str(self.prostokat), 'Prostokat(a=5.0, b=10.0)')


if __name__ == '__main__':
    unittest.main()
