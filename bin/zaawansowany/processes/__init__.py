#!/usr/bin/env python3

import unittest


class Prostokat:

    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

        if self.a <= 0 or self.b <= 0:
            raise ValueError('Dlugosc bokow musi byc liczba naturalna')

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return (self.a + self.b) * 2

    def __str__(self):
        return 'Prostokat(a=%s, b=%s)' % (self.a, self.b)


class ProstokatTest(unittest.TestCase):

    def setUp(self):
        self.prostokat = Prostokat(a=5, b=10)

    def test_obliczania_pola(self):
        self.assertEqual(self.prostokat.pole(), 50)

    def test_obliczania_obwodu(self):
        self.assertEqual(self.prostokat.obwod(), 30)

    def test_ustawienia_bokow(self):
        with self.assertRaises(TypeError):
            Prostokat(a=0)
        with self.assertRaises(TypeError):
            Prostokat(b=0)

    def test_dlugosci_bokow(self):
        with self.assertRaises(ValueError):
            Prostokat(a=-1, b=-2)

    def test_prostokat_to_string(self):
        self.assertEqual(str(self.prostokat), 'Prostokat(a=5.0, b=10.0)')


if __name__ == '__main__':
    unittest.main()

