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

# config
DECIMAL_PLACES = 2
MAX = 10**9

DECIMAL = [u"", u"dziesiętnych", u"setnych"]
UNITS = [u"zero", u"jeden", u"dwa", u"trzy", u"cztery", u"pięć", u"sześć", u"siedem", u"osiem", u"dziewięć"]
TENS = [u"", u"dziesięć", u"dwadzieścia", u"trzydzieści", u"czterdzieści", u"pięćdziesiąt", u"sześćdziesiąt", u"siedemdziesiąt", u"osiemdziesiąt", u"dziewięćdziesiąt"]
HUNDREDS = [u"", u"sto", u"dwieście", u"trzysta", u"czterysta", u"pięćset", u"sześćset", u"siedemset", u"osiemset", u"dziewięćset"]
MORE_SINGULAR = [u"", u"tysiąc", u"milion"]
MORE_PLURAL = [u"", u"tysięcy", u"milionów"]


import logging
logging.basicConfig(level=logging.DEBUG)

def boundaries(num):
    """check if it fits withing boundaries"""
    num = float(num)
    num = round(num, DECIMAL_PLACES)
    
    if num > MAX:
        raise OverflowError
        
    return num


def triple2words(num, lsd):
    """ converts number triple to words
    
    num = number to parse
    lsd = least significant digit, not psychedelic drug :}
    it is used to determine in which list we should search in order to get
    proper word
    """
    
    if len(integer) >= 6:
        mega = int(integer[0:3])
        if mega == 1:
            output += "%s " % MORE_SINGULAR[2]
        else:
            output += "%s "% triple(mega)
    
    if len(integer) >= 3:
        kilo = int(integer[3:6])
        if kilo == 1:
            output += "%s " % MORE_SINGULAR[1]
        else:
            output += "%s " % triple(kilo)
    return num


def decimal2words(decimal):
    logging.info("decimal to parse: %s" % decimal)
    if len(decimal) == 2:
        deci = int(decimal[0])
        centi = int(decimal[1])
        return "i %s %s %s" % (TENS[deci], UNITS[centi], DECIMAL[2])
    elif len(decimal) == 1:
        deci = int(decimal[0])
        return "i %s %s" % (UNITS[deci], DECIMAL[1])
    else:
        pass
        
    print output


def words(num):
    """converts number into words

    following names are SI (International System of Units) prefixes
    http://en.wikipedia.org/wiki/SI_prefix#List_of_SI_prefixes
    """
    
    logging.info("number to convert %s" % num)
    output = u""
    
    num = str(num)
    integer = num.split(".")[0]
    decimal = num.split(".")[1]
    
    mega = int(integer[0:3])
    kilo = int(integer[3:6])
    hecto = int(integer[:3])
    
    output += triple2wods(mega, lvl=6)
    output += triple2wods(kilo, lvl=3)
    output += triple2wods(hecto, lvl=1)
    output += decimal2words(decimal)
    
    return output
    
    
    import sys
    sys.exit()
    
    """
    mega = int(num // 10**6)
    kilo = int(num // 10**3) % 10
    hecto = int(num // 10**2) % 10
    deca = int(num // 10**1) % 10
    unit = int(num // 10**0) % 10
    deci = int(num // 10**-1) % 10
    centi = int(num // 10**-2) % 10
    
    # float number precision hack
    if deci:
        if centi:
            centi += 1
        else:
            deci += 1
            
    logging.debug("mega: %s" % mega)
    logging.debug("kilo: %s" % kilo)
    logging.debug("hecto: %s" % hecto)
    logging.debug("deca: %s" % deca)
    logging.debug("unit: %s" % unit)
    logging.debug("deci: %s" % deci)
    logging.debug("centi: %s" % centi)
    """    
    
    
if __name__ == "__main__":
    #num = raw_input("Type num: ")
    num = 900099000.96
    num = boundaries(num)
    print words(num)