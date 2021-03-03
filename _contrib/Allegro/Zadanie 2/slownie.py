#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Mateusz Harasymczuk
    http://www.matt.harasymczuk.pl
    matt@harasymczuk.pl
    
    Napisz funkcję, która będzie konwertować liczbę na odpowiadającą
    jej postać słowną. Przyjmij za ograniczenia liczby mniejsze
    od miliarda i do dwóch miejsc po przecinku.
    
    Przykład Ciąg: Słownie:    1. 1234,56 tysiąc dwieście trzydzieści cztery i pięćdziesiąt sześć setnych    2. 900099000,9 dziewięćset milionów dziewięćdziesiąt dziewięć tysięcy i dziewięć dziesiątych
"""


# dict is composed from LSD number and words
# lsd = least significant digit, not psychedelic drug :}
WORDS = {
    0.01:[u"setnych"],
    0.1:[u"dziesiętnych"],
    0:[u"zero", u"jeden", u"dwa", u"trzy", u"cztery", u"pięć", u"sześć", u"siedem", u"osiem", u"dziewięć"],
    1:[u"", u"jedenaście", u"dwanaście", u"trzynaście", u"czternaście", u"piętnaście", u"szesnaście", u"siedemnaście", u"osiemnaście", u"dziewiętnaście"],
    2:[u"", u"dziesięć", u"dwadzieścia", u"trzydzieści", u"czterdzieści", u"pięćdziesiąt", u"sześćdziesiąt", u"siedemdziesiąt", u"osiemdziesiąt", u"dziewięćdziesiąt"],
    3:[u"", u"sto", u"dwieście", u"trzysta", u"czterysta", u"pięćset", u"sześćset", u"siedemset", u"osiemset", u"dziewięćset"],
    4:[u"", u"tysiąc", u"tysięcy", u"tysiące"],
    6:[u"", u"milion", u"miliony", u"milionów"],
}

import logging
#logging.basicConfig(level=logging.DEBUG)

def get_word(word, lsd):
    """ name is self explaining :} """
    out = WORDS[lsd][word]
    
    logging.debug("get_word(word='%d', lsd='%d') returns '%s'" % (word, lsd, out))
    return out


def limit(num):
    decimal_places = 2
    max = 10**9
    """check if num fits within boundaries"""
    out = float(num)
    out = round(num, decimal_places)
    
    if out > max:
        raise OverflowError
        
    logging.debug("boundaries(num='%.2f') returns '%.2f'" % (num, out))
    return out


def triple2words(num, lsd):
    """ converts number triple to words
    
    num = number to parse
    lsd = least significant digit, not psychedelic drug :}
    it is used to determine in which list we should search in order to get
    proper word
    
    h, m, l == high, medium, low of num list
    """
    num = str(num)
    out = u""
    
    if lsd:
        name = get_word(2, lsd=lsd)
    else:
        name = u""
    
    if len(num) == 3:
        h, m, l = num
        h = get_word(int(h), lsd=3)
        m = get_word(int(m), lsd=2)
        l = get_word(int(l), lsd=0)
        out = "%s %s %s %s " % (h, m, l, name)
    elif len(num) == 2:
        h, l = num
        h = get_word(int(h), lsd=2)
        l = get_word(int(l), lsd=0)
        out = "%s %s %s " % (h, l, name)
    elif len(num) == 1:
        h = num[0]
        h = get_word(int(h), lsd=0)
        out = "%s %s " % (h, name)
    
    
    logging.debug("triple2words(num='%s', lsd='%d') returns '%s'" % (num, lsd, out))
    return out


def decimal2words(num):
    """ converts decimail remainder """
    if len(num) == 2:
        deci, centi = num
        deci = get_word(int(deci), lsd=2)
        centi = get_word(int(centi), lsd=0)
        name = get_word(0, lsd=0.01)
        out = "i %s %s %s" % (deci, centi, name)
    elif len(num) == 1:
        deci = num[0]
        deci = get_word(int(deci), lsd=2)
        name = get_word(1, lsd=0.1)
        out = "i %s %s" % (deci, name)
    else:
        out = ""
    
    logging.info("decimal2words(num='%s') returns '%s'" % (num, out))
    return out


def words(num):
    """converts number into words

    following names are SI (International System of Units) prefixes
    http://en.wikipedia.org/wiki/SI_prefix#List_of_SI_prefixes
    """
    out = u""
    num = str(num)
    integer = num.split(".")[0]
    decimal = num.split(".")[1]
    
    mega = int(integer[0:3])
    kilo = int(integer[3:6])
    hecto = int(integer[6:9])
    
    logging.debug("mega: %s" % mega)
    logging.debug("kilo: %s" % kilo)
    logging.debug("hecto: %s" % hecto)
    logging.debug("decimal: %s" % decimal)
    
    out += triple2words(mega, lsd=6)
    out += triple2words(kilo, lsd=4)
    out += triple2words(hecto, lsd=0)
    out += decimal2words(decimal)
    
    logging.info("words(num='%s') returns '%s'" % (num, out))
    return out   


if __name__ == "__main__":
    #num = raw_input("Type num: ")
    num = 23456789.1234
    num = limit(num)
    print words(num)