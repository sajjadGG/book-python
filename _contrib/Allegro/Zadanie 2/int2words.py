"""
Mateusz Harasymczuk
http://www.matt.harasymczuk.pl
matt@harasymczuk.pl

Napisz funkcję, która będzie konwertować liczbę na odpowiadającą
jej postać słowną. Przyjmij za ograniczenia liczby mniejsze
od miliarda i do dwóch miejsc po przecinku.

Przykład Ciąg: Słownie:
1. 1234,56 tysiąc dwieście trzydzieści cztery i pięćdziesiąt sześć setnych
2. 900099000,9 dziewięćset milionów dziewięćdziesiąt dziewięć tysięcy i dziewięć dziesiątych
"""


class NumberToWord:
    """converts any given number to words"""

    integer = 0
    decimal = 0
    _positive = True
    _output = u""

    # dict indexes are LSD numbers and words
    # LSD = least significant digit, not psychedelic drug :}
    _WORDS = {
        0.01:[u"setnych"],
        0.1:[u"dziesiętnych"],
        0:[u"zero", u"jeden", u"dwa", u"trzy", u"cztery", u"pięć", u"sześć", u"siedem", u"osiem", u"dziewięć"],
        1:[u"", u"jedenaście", u"dwanaście", u"trzynaście", u"czternaście", u"piętnaście", u"szesnaście", u"siedemnaście", u"osiemnaście", u"dziewiętnaście"],
        2:[u"", u"dziesięć", u"dwadzieścia", u"trzydzieści", u"czterdzieści", u"pięćdziesiąt", u"sześćdziesiąt", u"siedemdziesiąt", u"osiemdziesiąt", u"dziewięćdziesiąt"],
        3:[u"", u"sto", u"dwieście", u"trzysta", u"czterysta", u"pięćset", u"sześćset", u"siedemset", u"osiemset", u"dziewięćset"],
        4:[u"", u"tysiąc", u"tysiące", u"tysięcy" ],
        5:[u"", u"milion", u"miliony", u"milionów" ],
    }


    def _get_word(self, lsd, word):
        """ gets word out of WORDS dict """
        return self._WORDS[lsd][word]


    def __init__(self, num):
        self.integer = int(num)
        self.decimal = int((num * 100) % 100)

        if num < 0:
            self._positive = False


    def __str__(self):
        i = self.integer
        d = self.decimal

        i = self.convert(i)

        if d % 10:
            d = "%s %s" % (self.convert(d), self._get_word(0.01, 0))
        else:
            d = d / 10
            d = "%s %s" % (self.convert(d), self._get_word(0.1, 0))

        return ("%s i %s" % (i, d)).encode("utf-8")


    def _grammar_case(self, num):
        units = num % 10
        tens = (num // 10) % 10

        # jeden tysiąc, milion
        if num == 1:
            key = 1

        # naście tysięcy, milionów
        elif tens == 1 and units > 1:
            key = 3

        # [kilka-dziesiąt/set] or [dwa/trzy/czery] tysiące
        elif  2 <= units <= 4:
            key = 2

        # x tysięcy, milionów
        else:
            key = 3

        return key


    def _triples_to_words(self, num):
        units = num % 10
        tens = (num // 10) % 10
        hundreds = (num // 100) % 10
        words = []

        if hundreds > 0:
            words.append(self._get_word(3, hundreds))
        if tens == 1:
            words.append(self._get_word(1, units))
        else:
            if tens > 0:
                words.append(self._get_word(2, tens))
            if units > 0:
                words.append(self._get_word(0, units))

        return " ".join(words)


    def _split_to_triples(self, num):
        triples = []

        while num > 0:
            triples.append(num % 1000)
            num = num // 1000

        return triples


    def _words_triples(self, triples):
        words = []
        for i, tri in enumerate(triples):
            if tri > 0:
                if i > 0:
                    p = self._grammar_case(tri)
                    name = self._get_word(i + 3, p)
                    words.append("%s %s" % (self._triples_to_words( tri ), name))
                else:
                    words.append(self._triples_to_words( tri ))
        words.reverse()
        return " ".join(words)


    def convert(self, num):
        if not num:
            return self._get_word(lsd=0, word=1)

        num = int(num)
        triples = self._split_to_triples(num)
        return self._words_triples(triples)


def limit(num):
    """ check boundries
    check if num fits within boundaries
    this function is not mandatory
    """
    DECIMAL_PLACES = 2
    MAX = 10**9

    out = float(num)
    out = round(num, DECIMAL_PLACES)

    if out > MAX:
        raise OverflowError

    return out




if __name__ == "__main__":
    num = raw_input("Type num: ")
    #optional check if num is within boundries
    num = limit(num)
    print NumberToWord(num)
