"""
1. Passwords i wczytywanie konfiguracji
2. Wersjonowanie API
3. Print formatting
4. Co jest nie tak z cotangensem?

"""



def wyswietlanie(ciag, range_=30):
    """
    >>> wyswietlanie('asd')
    asd
    asd
    asd
    asd
    """
    for i in range(4):
        print(ciag)



WIEK_PELNOLETNOSCI = 21


def pelnoletni(wiek):
    """
    >>> pelnoletni(2)
    False
    >>> pelnoletni(30)
    True
    """
    if wiek < WIEK_PELNOLETNOSCI:
        return False
    else:
        return True



with open('../../tmp/etc-passwd') as passwd:
    passwd.read()

