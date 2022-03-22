#!/usr/bin/env python

"""
    Mateusz Harasymczuk
    http://www.matt.harasymczuk.pl
    matt@harasymczuk.pl


    Napisz dwuargumentową funkcję, w której pierwszym parametrem będzie ciąg (string),
    a drugim wartość przesunięcia, a zwracać będzie ciąg zaszyfrowany tzw. szyfrem Cezara.
    Szyfr Cezara jest szyfrem przesuwającym, w którym każda litera tekstu szyfrowanego
    zastępowana jest inną literą oddaloną od niej o stałą liczbę pozycji w alfabecie,
    przy czym kierunek zamiany musi być zachowany.

    Przykład 1 (przesunięcie o 3)
    Alfabet: AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ
    Szyfr: CĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻAĄB

    Przykład 2 (przesuniecie o 3)
    Tekst jawny: MĘŻNY BĄDŹ, CHROŃ PUŁK TWÓJ I SZEŚĆ FLAG
    Zaszyfrowany: OHBÓŻ DĆFĄ, EKTRP ŚZŃM YŹSŁ L UAGWĘ INCJ


    UWAGA:
        program dziala zgodnie z przykladami,
        tzn. uwzgledania polskie litery
        i korzysta z danego alfabetu
        z przykladu 1, pozostale znaki
        (np. male litery, przecinki kropki)
        nie sa poddawane konwersji.
        Aby rozszerzyc program o takie mozliwosci nalezy:
        1) zmienic alfabet
        2) uzyc funkcji konwertujacej niezaleznej
            od wielkosci liter

"""


ALPHABET = u'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ'

def encode(plaintext, shift):
    """encode plaintext message using Cesar's Cypher with given shift"""

    length = len(ALPHABET)
    output = u''
    temp = {}

    # generate temporary
    # substitution dict
    for i in range(0, length):
        temp[ ALPHABET[i] ] = ALPHABET[(i + shift) % length]

    # do the conversion
    for char in plaintext:
        if char in temp:
            char = temp[char]
        output += char

    return output


if __name__ == "__main__":
    #msg = raw_input("Type string to encode: ")
    msg = u'MĘŻNY BĄDŹ, CHROŃ PUŁK TWÓJ I SZEŚĆ FLAG'
    print encode(plaintext=msg, shift=3)
